from typing import Any, Dict, List, Optional, Tuple, Type, Union

import dataclasses
import pkgutil
import struct


class PluginParserException(BaseException):
    pass


class PluginParser:
    @staticmethod
    def parse_plugin(plugin_name: str) -> Any:
        try:
            plugin_bytes: bytes = pkgutil.get_data(__name__, f"base/{plugin_name}.esp")
        except Exception:
            return None

        return PluginData.deserialize(plugin_name, plugin_bytes)


# Dataclasses
@dataclasses.dataclass
class PluginData:
    name: str
    tes4_record: "TES4Record"
    grup_records: List["GRUPRecord"]

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, name: str, data: bytes) -> "PluginData":
        offset: int = 0
        size: int = len(data)

        tes4_record: TES4Record = None
        grup_records: List[GRUPRecord] = list()

        while offset < size:
            header_bytes: bytes = data[offset:offset + 8]
            header: MinimalHeader = MinimalHeader.deserialize(header_bytes)

            print(header)

            record_end: int = offset + header.data_size

            if header.signature != "GRUP":
                record_end += 24

            record_bytes: bytes = data[offset:record_end]

            if header.signature == "TES4":
                tes4_record = TES4Record.deserialize(record_bytes)
            elif header.signature == "GRUP":
                print(record_bytes)
                print(len(record_bytes))
                grup_records.append(GRUPRecord.deserialize(record_bytes))
            else:
                pass

            offset = record_end

        return cls(
            name=name,
            tes4_record=tes4_record,
            grup_records=grup_records,
        )


@dataclasses.dataclass
class MinimalHeader:
    signature: str  # 4 characters
    data_size: int  # uint32

    # Read-only. Only used to peek at record types

    @classmethod
    def deserialize(cls, data: bytes) -> "MinimalHeader":
        signature: str = data[0:4].decode("ascii")
        data_size: int = struct.unpack("<I", data[4:8])[0]

        return cls(
            signature=signature,
            data_size=data_size,
        )


@dataclasses.dataclass
class RecordHeader:
    signature: str  # 4 characters
    data_size: int  # uint32
    flags: int  # uint32
    form_id: int  # uint32
    timestamp: int  # uint16
    version_control_info_1: int  # uint16
    form_version: int  # uint16
    version_control_info_2: int  # uint16

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "RecordHeader":
        unpacked_data: Tuple[Any, ...] = struct.unpack("<4sIIIHHHH", data[:24])

        return cls(
            signature=unpacked_data[0].decode("ascii"),
            data_size=unpacked_data[1],
            flags=unpacked_data[2],
            form_id=unpacked_data[3],
            timestamp=unpacked_data[4],
            version_control_info_1=unpacked_data[5],
            form_version=unpacked_data[6],
            version_control_info_2=unpacked_data[7],
        )


@dataclasses.dataclass
class FieldHeader:
    signature: str  # 4 characters
    data_size: int  # uint16

    # Read-only. Only used to peek at fields

    @classmethod
    def deserialize(cls, data: bytes) -> "FieldHeader":
        signature: str = data[0:4].decode("ascii")
        data_size: int = struct.unpack("<H", data[4:6])[0]

        return cls(
            signature=signature,
            data_size=data_size,
        )


@dataclasses.dataclass
class HEDRField:
    version: float  # float
    number_of_records: int  # uint32
    next_available_object_id: int  # uint32

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "HEDRField":
        unpacked_data: Tuple[Any, ...] = struct.unpack("<fII", data[:12])

        return cls(
            version=unpacked_data[0],
            number_of_records=unpacked_data[1],
            next_available_object_id=unpacked_data[2],
        )


@dataclasses.dataclass
class MASTField:
    file_name: str
    data: int  # uint64

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, file_name_size: int, data: bytes) -> "MASTField":
        file_name: str = data[:file_name_size - 1].decode("ascii")
        data: int = struct.unpack("<Q", data[file_name_size + 6:file_name_size + 6 + 8])[0]

        return cls(
            file_name=file_name,
            data=data,
        )


@dataclasses.dataclass
class TES4Record:
    record_header: RecordHeader
    header: HEDRField
    author: str  # CNAM
    master_files: List[MASTField]
    intv: int  # INTV uint32

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "TES4Record":
        record_header_bytes: bytes = data[0:24]
        record_header: RecordHeader = RecordHeader.deserialize(record_header_bytes)

        offset: int = 24
        size: int = len(data)

        header: HEDRField = None
        author = None
        master_files = list()
        intv = None

        while offset < size:
            field_signature: str = data[offset:offset + 4].decode("ascii")
            field_size: int = struct.unpack("<H", data[offset + 4:offset + 6])[0]

            if field_signature == "HEDR":
                header = HEDRField.deserialize(data[offset + 6:offset + 6 + field_size])
            elif field_signature == "CNAM":
                author = data[offset + 6:offset + 6 + field_size - 1].decode("ascii")
            elif field_signature == "MAST":
                adjacent_field_signature: str = data[offset + 6 + field_size:offset + 6 + field_size + 4].decode("ascii")
                adjacent_field_size: int = struct.unpack("<H", data[offset + 6 + field_size + 4:offset + 6 + field_size + 6])[0]

                if adjacent_field_signature != "DATA":
                    raise PluginParserException(f"Unexpected MAST field without adjacent DATA field")

                master_files.append(
                    MASTField.deserialize(field_size, data[offset + 6:offset + 6 + field_size + 6 + adjacent_field_size])
                )

                field_size += 6 + adjacent_field_size
            elif field_signature == "INTV":
                intv = struct.unpack("<I", data[offset + 6:offset + 6 + field_size])[0]

            offset += 6 + field_size

        return cls(
            record_header=record_header,
            header=header,
            author=author,
            master_files=master_files,
            intv=intv,
        )


@dataclasses.dataclass
class GRUPHeader:
    signature: str  # 4 characters
    data_size: int  # uint32. Includes the header size of 24 bytes. Only type that does so!
    label: str  # 4 characters
    group_type: int  # uint32. Only planning to support type 0 (top types)
    timestamp: int  # uint16
    version_control_info: int  # uint16
    unknown: int  # uint32

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "GRUPHeader":
        unpacked_data: Tuple[Any, ...] = struct.unpack("<4sI4sIHHI", data[:24])

        return cls(
            signature=unpacked_data[0].decode("ascii"),
            data_size=unpacked_data[1],
            label=unpacked_data[2].decode("ascii"),
            group_type=unpacked_data[3],
            timestamp=unpacked_data[4],
            version_control_info=unpacked_data[5],
            unknown=unpacked_data[6],
        )


@dataclasses.dataclass
class GRUPRecord:
    grup_header: GRUPHeader
    records: List[Union["INGRRecord"]]

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "TES4Record":
        grup_header_bytes: bytes = data[0:24]
        grup_header: GRUPHeader = GRUPHeader.deserialize(grup_header_bytes)

        if grup_header.group_type != 0:
            raise PluginParserException(f"Unsupported GRUP type {grup_header.group_type}. Only type 0 is supported.")

        offset: int = 24
        size: int = len(data)

        records: List[Union["INGRRecord"]] = list()

        while offset < size:
            header: MinimalHeader = MinimalHeader.deserialize(data[offset:offset + 8])
            record_end: int = offset + 24 + header.data_size

            records.append(record_type_mapping[grup_header.label].deserialize(data[offset:record_end]))

            offset += 24 + header.data_size

            break

        return cls(
            grup_header=grup_header,
            records=records,
        )


@dataclasses.dataclass
class INGREffectField:
    magic_effect_editor_id: int  # uint32
    magnitude: float  # float
    area_of_effect: int  # uint32
    duration: int  # uint32

    def serialize(self) -> bytes:
        output: bytes = b""

        output += "EFID".encode("ascii")
        output += struct.pack("<H", 4)
        output += struct.pack("<I", self.magic_effect_editor_id)

        output += "EFIT".encode("ascii")
        output += struct.pack("<H", 12)
        output += struct.pack("<fII", self.magnitude, self.area_of_effect, self.duration)

        return output

    @classmethod
    def deserialize(cls, data: bytes) -> "INGREffectField":
        offset: int = 0
        size: int = len(data)

        magic_effect_editor_id = None
        magnitude = None
        area_of_effect = None
        duration = None

        while offset < size:
            field_header = FieldHeader.deserialize(data[offset:offset + 6])
            end_of_field: int = offset + 6 + field_header.data_size

            field_data: bytes = data[offset + 6:end_of_field]

            if field_header.signature == "EFID":
                magic_effect_editor_id = struct.unpack("<I", field_data)[0]
            elif field_header.signature == "EFIT":
                magnitude, area_of_effect, duration = struct.unpack("<fII", field_data)

            offset = end_of_field

        return cls(
            magic_effect_editor_id=magic_effect_editor_id,
            magnitude=magnitude,
            area_of_effect=area_of_effect,
            duration=duration,
        )


@dataclasses.dataclass
class INGRRecord:
    record_header: RecordHeader
    editor_id: str
    vmad_bytes: Optional[bytes]
    obnd_bytes: bytes
    name: str
    keyword_count: Optional[int]  # uint32
    keyword_editor_ids: List[int]  # uint32[keyword_count]
    modl_bytes: bytes
    modt_bytes: Optional[bytes]
    mods_bytes: Optional[bytes]
    icon_bytes: Optional[bytes]
    pickup_sound_editor_id: Optional[int]  # uint32
    drop_sound_editor_id: Optional[int]  # uint32
    value: int  # uint32
    weight: float  # float
    enit_bytes: bytes
    effects: List[INGREffectField]

    def serialize(self) -> bytes:
        pass

    @classmethod
    def deserialize(cls, data: bytes) -> "INGRRecord":
        record_header_bytes: bytes = data[0:24]
        record_header: RecordHeader = RecordHeader.deserialize(record_header_bytes)

        offset: int = 24
        size: int = len(data)

        editor_id = None
        vmad_bytes = None
        obnd_bytes = None
        name = None
        keyword_count = None
        keyword_editor_ids = list()
        modl_bytes = None
        modt_bytes = None
        mods_bytes = None
        icon_bytes = None
        pickup_sound_editor_id = None
        drop_sound_editor_id = None
        value = None
        weight = None
        enit_bytes = None
        effects = list()

        while offset < size:
            field_header = FieldHeader.deserialize(data[offset:offset + 6])
            end_of_field: int = offset + 6 + field_header.data_size

            field_data: bytes = data[offset + 6:end_of_field]

            if field_header.signature == "EDID":
                editor_id = field_data[:-1].decode("ascii")
            elif field_header.signature == "VMAD":
                vmad_bytes = field_data
            elif field_header.signature == "OBND":
                obnd_bytes = field_data
            elif field_header.signature == "FULL":
                name = field_data[:-1].decode("ascii")
            elif field_header.signature == "KSIZ":
                keyword_count = struct.unpack("<I", field_data)[0]
            elif field_header.signature == "KWDA":
                struct_format: str = "<"

                for _ in range(keyword_count or 0):
                    struct_format += "I"

                keyword_data = struct.unpack(struct_format, field_data)
                keyword_editor_ids = list(keyword_data)
            elif field_header.signature == "MODL":
                modl_bytes = field_data
            elif field_header.signature == "MODT":
                modt_bytes = field_data
            elif field_header.signature == "MODS":
                modt_bytes = field_data
            elif field_header.signature == "ICON":
                icon_bytes = field_data
            elif field_header.signature == "YNAM":
                pickup_sound_editor_id = struct.unpack("<I", field_data)[0]
            elif field_header.signature == "ZNAM":
                drop_sound_editor_id = struct.unpack("<I", field_data)[0]
            elif field_header.signature == "DATA":
                value, weight = struct.unpack("<If", field_data)
            elif field_header.signature == "ENIT":
                enit_bytes = field_data
            elif field_header.signature == "EFID":
                # Extend field_data to also cover EFIT
                end_of_field += 6 + 12
                field_data = data[offset:end_of_field]

                effects.append(INGREffectField.deserialize(field_data))

            offset = end_of_field

        return cls(
            record_header=record_header,
            editor_id=editor_id,
            vmad_bytes=vmad_bytes,
            obnd_bytes=obnd_bytes,
            name=name,
            keyword_count=keyword_count,
            keyword_editor_ids=keyword_editor_ids,
            modl_bytes=modl_bytes,
            modt_bytes=modt_bytes,
            mods_bytes=mods_bytes,
            icon_bytes=icon_bytes,
            pickup_sound_editor_id=pickup_sound_editor_id,
            drop_sound_editor_id=drop_sound_editor_id,
            value=value,
            weight=weight,
            enit_bytes=enit_bytes,
            effects=effects,
        )


record_type_mapping: Dict[str, Type[Union[INGRRecord]]] = {
    "INGR": INGRRecord,
}

