#!/usr/bin/env python
"""Parses Diablo II's TXT files and converts them to TOML files."""

__version__ = "0.5.1"

import collections.abc
import csv
import itertools
from argparse import ArgumentParser
from collections import UserDict
from os import PathLike
from typing import (
    Any,
    Collection,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    TextIO,
    Tuple,
    Union,
)

# import qtoml
# import toml


class DuplicateColumnNameError(Exception):
    """Raised when a duplicate column name is found in a TXT file.

    Column names are considered duplicates when they are exactly the same.
    Column names that differ only in casing (e.g. `mycolumn` and `MyColumn`) do
    not cause this exception.

    Attributes:
        name: Duplicate column name.
        index: Index of the duplicate column. This *should* be the greater of
            the two indices of the duplicate columns (though not guaranteed).
        filename: Name of the TXT file, if available.
    """

    def __init__(self, name: str, index: int, filename: Optional[str] = None) -> None:
        super().__init__(name, index, filename)
        self.name = name
        self.index = index
        self.filename = filename


_RowPrototype = Union[Mapping[str, Any], Collection[Any]]


class D2TXTRow(collections.abc.Mapping):
    """
    Represents a single row in a tabbed txt file.
    """

    def __init__(self, d2txt: "D2TXT", row: _RowPrototype) -> None:
        """Creates a row object for D2TXT.

        If `row` is a mapping, each key-value pair is copied to the new row.
        Keys that do not match any column name in `d2txt` are ignored.
        Otherwise, `row` is treated as an iterable of values to insert into each
        cell of the new row.

        Args:
            d2txt: The parent D2TXT object.
            row: Mapping or iterable of values to fill the row with.
        """
        self._d2txt = d2txt
        num_columns = len(d2txt.column_names())

        if isinstance(row, collections.abc.Mapping):
            self._row = [None] * num_columns
            for column_name, value in row.items():
                try:
                    self[column_name] = value
                except KeyError:
                    pass
        else:
            self._row = list(itertools.islice(row, num_columns))
            self._row += [None] * (num_columns - len(self._row))

    def __getitem__(self, key: str) -> Any:
        return self._row[self._d2txt.column_index(key)]

    def __iter__(self) -> Iterator:
        return iter(self._d2txt.column_names())

    def __len__(self) -> int:
        return len(self._row)

    def __setitem__(self, key: str, value: Any) -> None:
        self._row[self._d2txt.column_index(key)] = value


class D2TXTColumnNameView(collections.abc.Sequence):
    """A read-only view of the list of column names in a D2TXT object."""

    def __init__(self, column_names: Sequence[str]) -> None:
        self._column_names = column_names

    def __getitem__(self, index: int) -> str:
        return self._column_names[index]

    def __len__(self) -> int:
        return len(self._column_names)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self._column_names!r}>"


class D2TXT(collections.abc.MutableSequence):
    """
    Represents a tab-separated TXT file used in Diablo 2.
    """

    # pylint: disable=too-many-ancestors

    def __init__(self, column_names: Iterable[str]) -> None:
        """Create a D2TXT object.

        Args:
            column_names: Iterable of unique strings. Column names are
                case-sensitive.

        Raises:
            DuplicateColumnNameError: If a duplicate column name is found.
        """
        self._column_indices = {}
        for index, name in enumerate(column_names):
            if name in self._column_indices:
                raise DuplicateColumnNameError(name=name, index=index)
            self._column_indices[name] = index

        self._column_names = list(self._column_indices)
        self._rows = []

    def __getitem__(self, index: Union[int, slice]) -> Union[D2TXTRow, List[D2TXTRow]]:
        """Returns a row at the given index, or a `list` of rows if slice syntax
        is used."""
        return self._rows[index]

    def __len__(self) -> int:
        return len(self._rows)

    def __setitem__(
        self,
        index: Union[int, slice],
        value: Union[_RowPrototype, Iterable[_RowPrototype]],
    ) -> None:
        """Sets a row at the given index to `value`. If slice syntax is used,
        replaces the rows with each item in `value`."""
        if isinstance(index, slice):
            self._rows[index] = [D2TXTRow(self, row) for row in value]
        else:
            self._rows[index] = D2TXTRow(self, value)

    def __delitem__(self, index: int) -> None:
        """Deletes a row at the given index, or multiple rows if slice syntax
        is used."""
        del self._rows[index]

    def insert(self, index: int, value: _RowPrototype) -> None:
        self._rows.insert(index, D2TXTRow(self, value))

    def column_names(self) -> D2TXTColumnNameView:
        """Returns a read-only view of the list of column names."""
        return D2TXTColumnNameView(self._column_names)

    def column_index(self, column_name: str) -> int:
        """Returns the index of a column.

        Args:
            column_name: Column to search for. Column names are case-sensitive.

        Returns:
            0-based index of the column name.

        Raises:
            KeyError: If the column name does not exist.
        """
        return self._column_indices[column_name]

    @classmethod
    def load_txt(cls, txtfile: Union[str, PathLike, TextIO]) -> "D2TXT":
        """Creates a D2TXT object from a tabbed TXT file.

        Args:
            txtfile: A path string or readable text file object.

        Returns:
            The loaded D2TXT object.

        Raises:
            DuplicateColumnNameError: If a duplicate column name is found.
        """
        try:
            txtfile_fd = open(txtfile, encoding="cp949")
        except TypeError:
            pass
        else:
            with txtfile_fd:
                return cls.load_txt(txtfile_fd)

        txt_reader = csv.reader(
            txtfile, dialect="excel-tab", quoting=csv.QUOTE_NONE, quotechar=None
        )

        try:
            d2txt = cls(next(txt_reader))
        except DuplicateColumnNameError as err:
            raise DuplicateColumnNameError(
                name=err.name, index=err.index, filename=getattr(txtfile, "name", None)
            ) from None
        d2txt.extend(txt_reader)
        return d2txt

    def to_txt(self, txtfile: Union[str, PathLike, TextIO]) -> None:
        """Writes the contents of this object to a TXT file.

        Args:
            txtfile: A path string or writable text file object.
        """
        try:
            txtfile_fd = open(txtfile, mode="w", newline="", encoding="cp949")
        except TypeError:
            pass
        else:
            with txtfile_fd:
                self.to_txt(txtfile_fd)
                return

        txt_writer = csv.writer(
            txtfile, dialect="excel-tab", quoting=csv.QUOTE_NONE, quotechar=None
        )
        txt_writer.writerow(self._column_names)
        txt_writer.writerows(row.values() for row in self._rows)


# See https://d2mods.info/forum/viewtopic.php?t=43737 for more information
# fmt: off
AURAFILTER_FLAGS = {
    "FindPlayers":          0x00000001,
    "FindMonsters":         0x00000002,
    "FindOnlyUndead":       0x00000004,
    # Ignores missiles with explosion=1 in missiles.txt
    "FindMissiles":         0x00000008,
    "FindObjects":          0x00000010,
    "FindItems":            0x00000020,
    # "Unknown40":          0x00000040,
    # Target units flagged as IsAtt in monstats2.txt
    "FindAttackable":       0x00000080,
    "NotInsideTowns":       0x00000100,
    "UseLineOfSight":       0x00000200,
    # Checked manually by curse skill functions
    "FindSelectable":       0x00000400,
    # "Unknown800":         0x00000800,
    # Targets corpses of monsters and players
    "FindCorpses":          0x00001000,
    "NotInsideTowns2":      0x00002000,
    # Ignores units with SetBoss=1 in MonStats.txt
    "IgnoreBoss":           0x00004000,
    "IgnoreAllies":         0x00008000,
    # Ignores units with npc=1 in MonStats.txt
    "IgnoreNPC":            0x00010000,
    # "Unknown20000":       0x00020000,
    # Ignores units with primeevil=1 in MonStats.txt
    "IgnorePrimeEvil":      0x00040000,
    "IgnoreJustHitUnits":   0x00080000,  # Used by chainlightning
    # Rest are unknown
}
# fmt: on


class _Hex(int):
    """Subclass of int that is always converted to a hexadecimal format string.

    This takes advantage of the way toml.dumps() and qtoml.dumps() handles
    integers: they simply convert them to strings.
    """

    def __str__(self) -> str:
        """Returns a hexadecimal representation of this value."""
        return f"0x{self:X}"


def decode_aurafilter(aurafilter: int) -> Tuple[List[str], _Hex]:
    """Decodes an AuraFilter value into a list of flag names.

    Args:
        aurafilter: Value of AuraFilter field in Skills.txt

    Returns:
        Tuple of (flag_names, unknown_bits).
        `flag_names` is a list containing known aurafilter names.
        `unknown_bits` is an integer containing all unknown bits in aurafilter.

    Raises:
        TypeError: If aurafilter is not an integer.
    """
    af_names = []
    for name, flag in AURAFILTER_FLAGS.items():
        if aurafilter & flag:
            aurafilter &= ~flag
            af_names.append(name)
    return af_names, _Hex(aurafilter)


def encode_aurafilter(flags: List[str]) -> int:
    """Returns an integer made from combining the list of AuraFilter flag names.

    Args:
        flags: List of AuraFilter flag names.

    Returns:
        Integer representing the combination of the given flags.
        If `flags` is empty, returns 0.

    Raises:
        ValueError: If an unknown flag name is encountered.
    """
    aurafilter = 0
    for name in flags:
        try:
            aurafilter |= AURAFILTER_FLAGS[name]
        except KeyError:
            raise ValueError(f"Unknown AuraFilter flag name: {name!r}") from None
    return aurafilter


def range_1(stop: int) -> range:
    """Returns a range that starts at 1 and ends at `stop`, inclusive."""
    return range(1, stop + 1)


ColumnGroupSchema = Union[
    Mapping[str, "ColumnGroupSchema"], Collection["ColumnGroupSchema"], str
]


def yield_column_names(schema: ColumnGroupSchema) -> Iterator[str]:
    """Recursively traverses `schema` and yields member column names."""
    if isinstance(schema, str):
        yield schema
    else:
        seq = schema.values() if isinstance(schema, collections.abc.Mapping) else schema
        for value in seq:
            yield from yield_column_names(value)


# Note: I could use a dataclass here, but they are not available in Python 3.6.
class ColumnGroupRule:
    """Defines a column group rule.

    Attributes:
        alias: Alias of the column group.
        schema: Member columns belonging to the column group. May be a sequence
            of member columns, or a mapping of column aliases to column names,
            or a combination of the two.
    """

    def __init__(self, alias: str, schema: ColumnGroupSchema) -> None:
        self.alias = alias
        self.schema = schema

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"<{class_name}: alias={self.alias!r}, schema={self.schema!r}>"

    def member_names(self) -> Iterator[str]:
        """Returns an iterator of member column names."""
        return yield_column_names(self.schema)


def format_schema(schema: ColumnGroupSchema, param: str) -> ColumnGroupSchema:
    """Returns a new column group schema parameterized with str.format()."""
    if isinstance(schema, str):
        return schema.format(param)
    if isinstance(schema, collections.abc.Mapping):
        return {k.format(param): format_schema(v, param) for k, v in schema.items()}
    return [format_schema(v, param) for v in schema]


def make_colgroup(
    params: Iterable[Union[int, str]], alias: str, schema: ColumnGroupSchema
) -> Iterator[Tuple[str, ColumnGroupSchema]]:
    """Generates column groups by using formatting parameters."""
    return ((alias.format(p), format_schema(schema, p)) for p in params)


def initialize_column_groups(
    *colgroups: Iterable[Tuple[str, ColumnGroupSchema]]
) -> List[ColumnGroupRule]:
    """Initializes the list of column group rules.

    Args:
        colgroups: Tuples of the form (group alias, column group schema).

    Returns:
        List of rules sorted by # of member columns, from greatest to least.
    """
    return sorted(
        (ColumnGroupRule(*colgroup_def) for colgroup_def in colgroups),
        key=lambda colgroup: sum(1 for _ in colgroup.member_names()),
        reverse=True,
    )


# List of column group rules
# pylint: disable=line-too-long
# fmt: off
COLUMN_GROUPS = initialize_column_groups(
    # Armor.txt, Misc.txt, Weapons.txt
    ("--AC", {"min": "MinAC", "max": "MaxAC"}),
    *make_colgroup(range_1(3), "--Stat{}", {"stat": "stat{}", "calc": "calc{}"}),
    ("--Damage", {"min": "MinDam", "max": "MaxDam"}),
    ("--2HandDam", {"min": "2HandMinDam", "max": "2HandMaxDam"}),
    ("--MisDam", {"min": "MinMisDam", "max": "MaxMisDam"}),
    ("--Stack", {"min": "MinStack", "max": "MaxStack"}),
    *make_colgroup(
        ["Akara", "Alkor", "Asheara", "Cain", "Charsi", "Drehya", "Drognan", "Elzix", "Fara", "Gheed", "Halbu", "Hralti", "Jamella", "Larzuk", "Lysander", "Malah", "Ormus"],
        "--{}",
        {"min": "{}min", "max": "{}Max", "MagicMin": "{}MagicMin", "MagicMax": "{}MagicMax", "MagicLvl": "{}MagicLvl"},
    ),
    ("--Code", {"normal": "NormCode", "uber": "UberCode", "ultra": "UltraCode"}),
    ("--wClass", {"1hand": "wClass", "2hand": "2HandedWClass"}),
    ("--Inv", {"width": "InvWidth", "height": "InvHeight"}),
    ("--Upgrades", {"nightmare": "NightmareUpgrade", "hell": "HellUpgrade"}),
    # AutoMagic.txt, MagicPrefix.txt, MagicSuffix.txt
    *make_colgroup(range_1(3), "--Mod{}", {"prop": "Mod{}Code", "param": "Mod{}Param", "min": "Mod{}Min", "max": "Mod{}Max"}),
    ("--IType1-7", [f"IType{i}" for i in range_1(7)]),
    ("--EType1-3", [f"EType{i}" for i in range_1(3)]),
    ("--EType1-5", [f"EType{i}" for i in range_1(5)]),  # For MagicPrefix.txt
    ("--Cost", {"divide": "Divide", "multiply": "Multiply", "add": "Add"}),
    # CharStats.txt
    *make_colgroup(range_1(10), "--Item{}", {"code": "Item{}", "loc": "Item{}Loc", "count": "Item{}Count"}),
    # CubeMain.txt
    *make_colgroup(range_1(5), "--Mod{}", {"mod": "mod {}", "chance": "mod {} chance", "param": "mod {} param", "min": "mod {} min", "max": "mod {} max"}),
    *make_colgroup(range_1(5), "--B-Mod{}", {"mod": "b mod {}", "chance": "b mod {} chance", "param": "b mod {} param", "min": "b mod {} min", "max": "b mod {} max"}),
    *make_colgroup(range_1(5), "--C-Mod{}", {"mod": "c mod {}", "chance": "c mod {} chance", "param": "c mod {} param", "min": "c mod {} min", "max": "c mod {} max"}),
    # Gems.txt
    *make_colgroup(range_1(3), "--WeaponMod{}", {"prop": "WeaponMod{}Code", "param": "WeaponMod{}Param", "min": "WeaponMod{}Min", "max": "WeaponMod{}Max"}),
    *make_colgroup(range_1(3), "--HelmMod{}", {"prop": "HelmMod{}Code", "param": "HelmMod{}Param", "min": "HelmMod{}Min", "max": "HelmMod{}Max"}),
    *make_colgroup(range_1(3), "--ShieldMod{}", {"prop": "ShieldMod{}Code", "param": "ShieldMod{}Param", "min": "ShieldMod{}Min", "max": "ShieldMod{}Max"}),
    # Hireling.txt
    ("--Name", {"first": "NameFirst", "last": "NameLast"}),
    *make_colgroup(["HP", "Str", "Dex", "AR", "Resist"], "--{}", {"base": "{}", "/lvl": "{}/Lvl"}),
    ("--Defense", {"base": "Defense", "/lvl": "Def/Lvl"}),
    ("--Damage", {"min": "Dmg-Min", "max": "Dmg-Max", "/lvl": "Dmg/Lvl"}),
    *make_colgroup(
        range_1(6),
        "--Skill{}",
        {"name": "Skill{}", "mode": "Mode{}", "chance": "Chance{}", "chance/lvl": "ChancePerLvl{}", "level": "Level{}", "level/lvl": "LvlPerLvl{}"},
    ),
    # Inventory.txt
    ("--Inv", {"left": "InvLeft", "right": "InvRight", "top": "InvTop", "bottom": "InvBottom"}),
    ("--Grid", {"left": "GridLeft", "right": "GridRight", "top": "GridTop", "bottom": "GridBottom", "x": "GridX", "y": "GridY"}),
    ("--GridBox", {"width": "GridBoxWidth", "height": "GridBoxHeight"}),
    *make_colgroup(
        ("Inv", "rArm", "Torso", "lArm", "Head", "Neck", "rHand", "lHand", "Belt", "Feet", "Gloves"),
        "--{}",
        {"left": "{}Left", "right": "{}Right", "top": "{}Top", "bottom": "{}Bottom", "width": "{}Width", "height": "{}Height"},
    ),
    # ItemTypes.txt
    ("--BodyLoc1-2", ["BodyLoc1", "BodyLoc2"]),
    ("--MaxSock", {"L1": "MaxSock1", "L25": "MaxSock25", "L40": "MaxSock40"}),
    # Levels.txt
    ("--Size-RNH", [{"x": "SizeX", "y": "SizeY"}, {"x": "SizeX(N)", "y": "SizeY(N)"}, {"x": "SizeX(H)", "y": "SizeY(H)"}]),
    ("--Offset", {"x": "OffsetX", "y": "OffsetY"}),
    *make_colgroup(range(8), "--VizAndWarp{}", {"vis": "Vis{}", "warp": "Warp{}"}),
    ("--MonLvl-123", ["MonLvl1", "MonLvl2", "MonLvl3"]),
    ("--MonLvlEx-123", ["MonLvl1Ex", "MonLvl2Ex", "MonLvl3Ex"]),
    ("--MonDen-RNH", ["MonDen", "MonDen(N)", "MonDen(H)"]),
    ("--MonU-RNH", [{"min": "MonUMin", "max": "MonUMax"}, {"min": "MonUMin(N)", "max": "MonUMax(N)"}, {"min": "MonUMin(H)", "max": "MonUMax(H)"}]),
    *make_colgroup(range(8), "--Obj{}", {"grp": "ObjGrp{}", "prb": "ObjPrb{}"}),
    # LvlMaze.txt
    ("--Rooms-RNH", ["Rooms", "Rooms(N)", "Rooms(H)"]),
    ("--Size", {"x": "SizeX", "y": "SizeY"}),
    # LvlPrest.txt
    # ("--Size", {"x": "SizeX", "y": "SizeY"}),  # Also in LvlPrest.txt
    # Missiles.txt
    ("--pDoFunc", {"srv": "pSrvDoFunc", "clt": "pCltDoFunc"}),
    ("--pHitFunc", {"srv": "pSrvHitFunc", "clt": "pCltHitFunc"}),
    *make_colgroup(range_1(3), "--SubMissile{}", {"srv": "SubMissile{}", "clt": "CltSubMissile{}"}),
    *make_colgroup(range_1(4), "--HitSubMissile{}", {"srv": "HitSubMissile{}", "clt": "CltHitSubMissile{}"}),
    ("--SrvCalc1", {"calc": "SrvCalc1", "desc": "*srv calc 1 desc"}),
    *make_colgroup(range_1(5), "--Param{}", {"param": "Param{}", "desc": "*param{} desc"}),
    ("--CltCalc1", {"calc": "CltCalc1", "desc": "*client calc 1 desc"}),
    *make_colgroup(range_1(5), "--CltParam{}", {"param": "CltParam{}", "desc": "*client param{} desc"}),
    ("--SHitCalc1", {"calc": "SHitCalc1", "desc": "*server hit calc 1 desc"}),
    *make_colgroup(range_1(3), "--SrvHitParam{}", {"param": "sHitPar{}", "desc": "*server hit param{} desc"}),
    ("--CHitCalc1", {"calc": "CHitCalc1", "desc": "*client hit calc1 desc"}),
    *make_colgroup(range_1(3), "--CltHitParam{}", {"param": "cHitPar{}", "desc": "*client hit param{} desc"}),
    ("--DmgCalc1", {"calc": "DmgCalc1", "desc": "*damage calc 1"}),
    *make_colgroup(range_1(2), "--DamageParam{}", {"param": "dParam{}", "desc": "*damage param{} desc"}),
    ("--MinDamage0-5", ["MinDamage", "MinLevDam1", "MinLevDam2", "MinLevDam3", "MinLevDam4", "MinLevDam5"]),
    ("--MaxDamage0-5", ["MaxDamage", "MaxLevDam1", "MaxLevDam2", "MaxLevDam3", "MaxLevDam4", "MaxLevDam5"]),
    ("--MinE0-5", ["EMin", "MinELev1", "MinELev2", "MinELev3", "MinELev4", "MinELev5"]),
    ("--MaxE0-5", ["EMax", "MaxELev1", "MaxELev2", "MaxELev3", "MaxELev4", "MaxELev5"]),
    ("--ELen0-3", ["ELen", "ELevLen1", "ELevLen2", "ELevLen3"]),
    ("--RGB", {"red": "Red", "green": "Green", "blue": "Blue"}),
    # MonLvl.txt
    *make_colgroup(
        ["AC", "TH", "HP", "DM", "XP", "L-AC", "L-TH", "L-HP", "L-DM", "L-XP"],
        "--{}-RNH",
        ["{}", "{}(N)", "{}(H)"],
    ),
    # MonProp.txt
    *make_colgroup(range_1(6), "--Prop{}-R", {"prop": "Prop{}", "chance": "Chance{}", "param": "Par{}", "min": "Min{}", "max": "Max{}"}),
    *make_colgroup(range_1(6), "--Prop{}-N", {"prop": "Prop{} (N)", "chance": "Chance{} (N)", "param": "Par{} (N)", "min": "Min{} (N)", "max": "Max{} (N)"}),
    *make_colgroup(range_1(6), "--Prop{}-H", {"prop": "Prop{} (H)", "chance": "Chance{} (H)", "param": "Par{} (H)", "min": "Min{} (H)", "max": "Max{} (H)"}),
    # MonStats.txt
    ("--Spawn", {"place": "PlaceSpawn", "x": "SpawnX", "y": "SpawnY", "mode": "SpawnMode"}),
    ("--Party", {"min": "PartyMin", "max": "PartyMax"}),
    ("--Grp", {"min": "MinGrp", "max": "MaxGrp"}),
    # "--AC-RNH" is already provided by MonLvl.txt
    *make_colgroup(["Level", "Drain", "ColdEffect", "ToBlock", "Exp"], "--{}-RNH", ["{}", "{}(N)", "{}(H)"]),
    ("--AI-R", {"delay": "AIDel", "dist": "AIDist", **{f"p{i}": f"aip{i}" for i in range_1(8)}}),
    ("--AI-N", {"delay": "AIDel(N)", "dist": "AIDist(N)", **{f"p{i}": f"aip{i}(N)" for i in range_1(8)}}),
    ("--AI-H", {"delay": "AIDel(H)", "dist": "AIDist(H)", **{f"p{i}": f"aip{i}(H)" for i in range_1(8)}}),
    *make_colgroup(range_1(8), "--Skill{}", {"name": "Skill{}", "mode": "Sk{}Mode", "level": "Sk{}Lvl"}),
    ("--Res-R", {"phys": "ResDm", "mag": "ResMa", "fire": "ResFi", "ltng": "ResLi", "cold": "ResCo", "pois": "ResPo"}),
    ("--Res-N", {"phys": "ResDm(N)", "mag": "ResMa(N)", "fire": "ResFi(N)", "ltng": "ResLi(N)", "cold": "ResCo(N)", "pois": "ResPo(N)"}),
    ("--Res-H", {"phys": "ResDm(H)", "mag": "ResMa(H)", "fire": "ResFi(H)", "ltng": "ResLi(H)", "cold": "ResCo(H)", "pois": "ResPo(H)"}),
    ("--HP-RNH", [{"min": "MinHP", "max": "MaxHP"}, {"min": "MinHP(N)", "max": "MaxHP(N)"}, {"min": "MinHP(H)", "max": "MaxHP(H)"}]),
    *make_colgroup(
        ["A1", "A2", "S1"],
        "--{}-RNH",
        [{"min": "{}MinD", "max": "{}MaxD", "TH": "{}TH"}, {"min": "{}MinD(N)", "max": "{}MaxD(N)", "TH": "{}TH(N)"}, {"min": "{}MinD(H)", "max": "{}MaxD(H)", "TH": "{}TH(H)"}],
    ),
    *make_colgroup(["El1", "El2", "El3"], "--{}", {"mode": "{}Mode", "type": "{}Type"}),
    *make_colgroup(
        ["El1", "El2", "El3"],
        "--{}-RNH",
        [{"pct": "{}Pct", "min": "{}MinD", "max": "{}MaxD", "dur": "{}Dur"}, {"pct": "{}Pct(N)", "min": "{}MinD(N)", "max": "{}MaxD(N)", "dur": "{}Dur(N)"}, {"pct": "{}Pct(H)", "min": "{}MinD(H)", "max": "{}MaxD(H)", "dur": "{}Dur(H)"}],
    ),
    ("--TreasureClass-R", [f"TreasureClass{i}" for i in range_1(4)]),
    ("--TreasureClass-N", [f"TreasureClass{i}(N)" for i in range_1(4)]),
    ("--TreasureClass-H", [f"TreasureClass{i}(H)" for i in range_1(4)]),
    # MonStats2.txt
    # ("--Size", {"x": "SizeX", "y": "SizeY"}),  # Also in LvlPrest.txt
    ("--Light", {"R": "Light-R", "G": "Light-G", "B": "Light-B"}),
    ("--uTrans-RNH", ("uTrans", "uTrans(N)", "uTrans(H)")),
    *make_colgroup(("HD", "TR", "LG", "RA", "LA", "RH", "SH"), "--{}", {"on": "{}", "v": "{}v"}),
    *make_colgroup(("DT", "NU", "WL", "GH", "BL", "DD", "KB", "SQ", "RN"), "--{}", {"m": "m{}", "d": "d{}"}),
    *make_colgroup(("A1", "A2", "SC", "S3", "S4"), "--{}", {"m": "m{}", "d": "d{}", "mv": "{}mv"}),
    *make_colgroup(("S1", "S2"), "--{}", {"on": "{}", "v": "{}v", "m": "m{}", "d": "d{}", "mv": "{}mv"}),
    ("--ht", {"left": "htLeft", "top": "htTop", "width": "htWidth", "height": "htHeight"}),
    # Objects.txt
    ("--nTgt", {"fx": "nTgtFX", "fy": "nTgtFY", "bx": "nTgtBX", "by": "nTgtBY"}),
    *make_colgroup(["Offset", "Space"], "--{}", {"x": "X{}", "y": "Y{}"}),
    *make_colgroup(
        ("Selectable", "FrameCnt", "FrameDelta", "CycleAnim", "Lit", "BlocksLight", "HasCollision", "Start", "OrderFlag", "Mode", "Parm"),
        "--{}",
        {mode: f"{{}}{index}" for index, mode in enumerate(["NU", "OP", "ON", "S1", "S2", "S3", "S4", "S5"])},
    ),
    ("--Selectable", {"NU": "Selectable0", "OP": "Selectable1"}),
    ("--FrameCnt", {"NU": "FrameCnt0", "OP": "FrameCnt1"}),
    ("--Box", {"left": "Left", "top": "Top", "width": "Width", "height": "Height"}),
    # Overlay.txt
    # ("--Offset", {"x": "xOffset", "y", "yOffset"}),  # Also in Objects.txt
    # ("--RGB", {"red": "Red", "green": "Green", "blue": "Blue"}),  # Also in Missiles.txt
    # Runes.txt
    ("--IType1-6", [f"IType{i}" for i in range_1(6)]),
    # ("--EType1-3", [f"IType{i}" for i in range_1(3)]),  # Also in AutoMagic.txt
    ("--Rune1-6", [f"Rune{i}" for i in range_1(6)]),
    *make_colgroup(range_1(7), "--T1-{}", {"prop": "T1Code{}", "param": "T1Param{}", "min": "T1Min{}", "max": "T1Max{}"}),
    # Sets.txt
    *make_colgroup(range(2, 6), "--P{}A", {"prop": "pCode{}A", "param": "pParam{}A", "min": "pMin{}A", "max": "pMax{}A"}),
    *make_colgroup(range(2, 6), "--P{}B", {"prop": "pCode{}B", "param": "pParam{}B", "min": "pMin{}B", "max": "pMax{}B"}),
    *make_colgroup(range_1(8), "--F{}", {"prop": "fCode{}", "param": "fParam{}", "min": "fMin{}", "max": "fMax{}"}),
    # SetItems.txt
    # *make_colgroup(range_1(9), "--Prop{}", {"prop": "Prop{}", "param": "Par{}", "min": "Min{}", "max": "Max{}"}),  # Also in UniqueItems.txt
    *make_colgroup(range_1(5), "--aProp{}A", {"prop": "aProp{}A", "param": "aPar{}A", "min": "aMin{}A", "max": "aMax{}A"}),
    *make_colgroup(range_1(5), "--aProp{}B", {"prop": "aProp{}B", "param": "aPar{}B", "min": "aMin{}B", "max": "aMax{}B"}),
    # Skills.txt
    ("--StartFunc", {"srv": "SrvStFunc", "clt": "CltStFunc"}),
    ("--DoFunc", {"srv": "SrvDoFunc", "clt": "CltDoFunc"}),
    *make_colgroup(["", "A", "B", "C"], "--Missile{}", {"srv": "SrvMissile{}", "clt": "CltMissile{}"}),
    ("--MissileD", {"clt": "CltMissileD"}),  # No matching server-side missile field, but added for consistency's sake
    *make_colgroup(range_1(6), "--AuraStat{}", {"stat": "AuraStat{}", "calc": "AuraStatCalc{}"}),
    *make_colgroup(range_1(6), "--PassiveStat{}", {"stat": "PassiveStat{}", "calc": "PassiveCalc{}"}),
    *make_colgroup(range_1(3), "--AuraEvent{}", {"event": "AuraEvent{}", "func": "AuraEventFunc{}"}),
    ("--AuraTargetEvent", {"event": "AuraTgtEvent", "func": "AuraTgtEventFunc"}),
    ("--PassiveEvent", {"event": "PassiveEvent", "func": "PassiveEventFunc"}),
    *make_colgroup(range_1(5), "--SumSkill{}", {"skill": "SumSkill{}", "calc": "SumSk{}Calc"}),
    *make_colgroup(range_1(4), "--CltCalc{}", {"calc": "CltCalc{}", "desc": "*cltcalc{} desc"}),
    *make_colgroup(range_1(4), "--Calc{}", {"calc": "Calc{}", "desc": "*calc{} desc"}),
    *make_colgroup(range_1(8), "--Param{}", {"param": "Param{}", "desc": "*Param{} Description"}),
    ("--MinDam0-5", ["MinDam", "MinLevDam1", "MinLevDam2", "MinLevDam3", "MinLevDam4", "MinLevDam5"]),
    ("--MaxDam0-5", ["MaxDam", "MaxLevDam1", "MaxLevDam2", "MaxLevDam3", "MaxLevDam4", "MaxLevDam5"]),
    ("--EMin0-5", ["EMin", "EMinLev1", "EMinLev2", "EMinLev3", "EMinLev4", "EMinLev5"]),
    ("--EMax0-5", ["EMax", "EMaxLev1", "EMaxLev2", "EMaxLev3", "EMaxLev4", "EMaxLev5"]),
    # ("--ELen0-3", ["ELen", "ELevLen1", "ELevLen2", "ELevLen3"]),  # Also in Skills.txt
    ("--Cost", {"multiply": "cost mult", "add": "cost add"}),
    # SkillDesc.txt
    ("--SkillPage", {"page": "SkillPage", "row": "SkillRow", "column": "SkillColumn"}),
    *make_colgroup(range_1(3), "--P{}Dm", {"elem": "P{}DmElem", "min": "P{}DmMin", "max": "P{}DmMax", }),
    *make_colgroup(range_1(6), "--Desc-{}", {"line": "DescLine{}", "textA": "DescTextA{}", "textB": "DescTextB{}", "calcA": "DescCalcA{}", "calcB": "DescCalcB{}"}),
    *make_colgroup(range_1(4), "--Dsc2-{}", {"line": "Dsc2Line{}", "textA": "Dsc2TextA{}", "textB": "Dsc2TextB{}", "calcA": "Dsc2CalcA{}", "calcB": "Dsc2CalcB{}"}),
    *make_colgroup(range_1(7), "--Dsc3-{}", {"line": "Dsc3Line{}", "textA": "Dsc3TextA{}", "textB": "Dsc3TextB{}", "calcA": "Dsc3CalcA{}", "calcB": "Dsc3CalcB{}"}),
    # States.txt
    # ("--Light", {"R": "Light-R", "G": "Light-G", "B": "Light-B"}),  # Also in MonStats2.txt
    # SuperUniques.txt
    # ("--Grp", {"min": "MinGrp", "max": "MaxGrp"}),  # Also in MonStats.txt
    # ("--uTrans-RNH", ("uTrans", "uTrans(N)", "uTrans(H)")),  # Also in MonStats2.txt
    # TreasureClassEx.txt
    *make_colgroup(range_1(10), "--Item{}", {"code": "Item{}", "prob": "Prob{}"}),
    # UniqueItems.txt
    *make_colgroup(range_1(12), "--Prop{}", {"prop": "Prop{}", "param": "Par{}", "min": "Min{}", "max": "Max{}"}),
    # ("--Cost", {"multiply": "cost mult", "add": "cost add"}),  # Also in Skills.txt
)
# fmt: on
# pylint: enable=line-too-long


def encode_toml_value(column_name: str, value: Union[int, str]) -> Any:
    """Encodes a value from a TXT cell so that it can be converted to TOML.

    Args:
        column_name: Column name of the cell, used to determine the appropriate
            decoding method.
        value: Value of the cell.

    Returns:
        Encoded value suitable for passing to a TOML dumper.
    """
    # If possible, attempt to convert strings to integers (but not other types)
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            pass

    if column_name.casefold() == "aurafilter":
        try:
            af_flags, unknown_bits = decode_aurafilter(value)
        except TypeError:
            return value
        # Dirty workaround for the lack of heterogeneous arrays in TOML v0.5.0
        # NOTE: Revisit this when uiri/toml adds support for hetero arrays.
        return [af_flags, [unknown_bits]] if unknown_bits else [af_flags]

    return value


def decode_toml_value(column_name: str, value: Any) -> Union[int, str]:
    """Decodes a value loaded from TOML so that it can be stored in D2TXT.

    Args:
        column_name: Column name of the cell, used to determine the appropriate
            encoding method.
        value: Value loaded from TOML.

    Returns:
        Decoded value suitable for passing to D2TXT.
    """
    if column_name.casefold() == "aurafilter":
        try:
            aurafilter = encode_aurafilter(value[0])
        except TypeError:
            return value
        try:
            unknown_bits = value[1][0]
        except (IndexError, TypeError):
            unknown_bits = 0
        return aurafilter | unknown_bits

    return value


def recase_schema(
    obj: ColumnGroupSchema, uncasefold: Mapping[str, str]
) -> ColumnGroupSchema:
    """Returns a new column group schema with properly recased member names."""
    if isinstance(obj, str):
        return uncasefold[obj.casefold()]
    if isinstance(obj, collections.abc.Mapping):
        return {key: recase_schema(value, uncasefold) for key, value in obj.items()}
    return [recase_schema(value, uncasefold) for value in obj]


def get_matched_colgroups(column_names: Iterable[str]) -> List[ColumnGroupRule]:
    """Return a list of column groups that match the given column names.

    Args:
        Iterable of column name strings to compare with column group rules
        in `COLUMN_GROUPS`. Column names are compared case-insensitively.

    Returns:
        List of applicable column group rules. Each rule's member column names
        are recased to match those in `column_names` without casefolding them.
    """
    casefold_to_normal = {name.casefold(): name for name in column_names}
    matched_colgroups = []

    for group in COLUMN_GROUPS:
        try:
            new_schema = recase_schema(group.schema, casefold_to_normal)
        except KeyError:
            continue
        matched_colgroups.append(ColumnGroupRule(group.alias, new_schema))
        # Remove matched member columns in order to avoid overlapping groups.
        # Example: --MinMaxDam and --MinDam0-5
        for name_cf in group.member_names():
            del casefold_to_normal[name_cf.casefold()]

    return matched_colgroups


def get_sorted_columns_and_groups(
    columns: Collection[str], colgroups: Iterable[ColumnGroupRule]
) -> List[Union[ColumnGroupRule, str]]:
    """Builds a sorted list of column names and column groups.

    Args:
        columns: Collection of column names.
        colgroups: Iterable of usable column group rules.

    Returns:
        Sorted list containing column names and column group rules.
    """
    column_to_index = {name: index for index, name in enumerate(columns)}
    # Build an iterable of tuples of (index, column name or colgroup).
    # Each colgroup is given the same index as its firstmost member column.
    indices_and_colgroups = (
        (min(column_to_index[name] for name in group.member_names()), group)
        for group in colgroups
    )
    # Place colgroups before normal columns to take advantage of stable sort,
    # which ensures that a column group always comes before any of its members.
    combined = itertools.chain(indices_and_colgroups, enumerate(columns))
    return [t[1] for t in sorted(combined, key=lambda t: t[0])]


def pack_colgroup(
    schema: ColumnGroupSchema, toml_row: Mapping[str, Union[int, str, None]]
) -> Union[list, str, UserDict]:
    """Tries to pack all member column values into an appropriate data structure.

    Args:
        schema: The grouping schema to recursively apply.
        toml_row: Mapping of column name to value to extract values from.

    Returns:
        On success, returns a non-empty list, string, or UserDict.
        On failure, returns an empty list, string, or UserDict.
    """
    if isinstance(schema, str):
        return toml_row.get(schema, "")

    if isinstance(schema, collections.abc.Mapping):
        inline_table = UserDict()
        for key, value in schema.items():
            value = pack_colgroup(value, toml_row)
            if value or value == 0:
                inline_table[key] = value
        return inline_table

    array = [pack_colgroup(value, toml_row) for value in schema]
    while array and array[-1] == "":
        array.pop()
    if all(not (value or value == 0) for value in array):
        return []
    if any(isinstance(value, collections.abc.Mapping) for value in array):
        # TOML spec v0.5.0 does not support arrays of mixed types.
        # Therefore, assume that all values are inline tables.
        assert all(isinstance(value, collections.abc.Mapping) for value in array)
    elif any(isinstance(value, int) for value in array) and any(
        isinstance(value, str) for value in array
    ):
        # The array should not have sub-arrays at this point
        assert all(isinstance(value, (int, str)) for value in array)
        # TOML spec v0.5.0 does not support arrays of mixed types.
        # Therefore, convert all numbers to strings.
        return list(map(str, array))
    return array


def make_toml_row(
    txt_row: Mapping[str, Any],
    colgroups: Iterable[ColumnGroupRule],
    columns_with_colgroups: Iterable[Union[ColumnGroupRule, str]],
) -> Dict[str, Any]:
    """Convert a D2TXT row object to a mapping that can be converted to TOML."""
    # Black magic to avoid creating more than one dictionary per row
    toml_row = {}

    # Fill the row dict with colgroups, as well as columns that have value.
    for name_or_colgroup in columns_with_colgroups:
        if isinstance(name_or_colgroup, ColumnGroupRule):
            # Column groups are pre-assigned in their correct positions
            # Rely on preservation of insertion order of dicts Python 3.6+
            toml_row[name_or_colgroup.alias] = None
        else:
            value = txt_row[name_or_colgroup]
            if not (value is None or value == ""):
                toml_row[name_or_colgroup] = encode_toml_value(name_or_colgroup, value)

    # Replace member columns if they can be packed into column groups
    for column_group in colgroups:
        packed_values = pack_colgroup(column_group.schema, toml_row)
        if packed_values:
            toml_row[column_group.alias] = packed_values
            for name in column_group.member_names():
                toml_row.pop(name, None)
        else:
            del toml_row[column_group.alias]

    return toml_row


def deepwrap_userdict(obj) -> ColumnGroupSchema:
    """Returns `obj` wrapped in UserDict to force qtoml to make inline tables."""
    if isinstance(obj, collections.abc.Mapping):
        # UserDict trick does not require multi-level UserDict
        return UserDict(obj)
    if isinstance(obj, collections.abc.Collection) and not isinstance(obj, str):
        return [deepwrap_userdict(value) for value in obj]
    return obj


# def d2txt_to_toml(d2txt: D2TXT) -> str:
#     """Converts a D2TXT object to TOML markup.
#
#     Args:
#         d2txt: D2TXT object to convert.
#
#     Returns:
#         String containing TOML markup.
#     """
#     columns = d2txt.column_names()
#     colgroups = get_matched_colgroups(columns)
#     columns_with_colgroups = get_sorted_columns_and_groups(columns, colgroups)
#
#     toml_rows = [make_toml_row(row, colgroups, columns_with_colgroups) for row in d2txt]
#
#     # Use qtoml.dumps(), because toml does not properly escape backslashes.
#     # Possibly related issues:
#     #   https://github.com/uiri/toml/issues/261
#     #   https://github.com/uiri/toml/issues/201
#     toml_encoder = qtoml.encoder.TOMLEncoder()
#     # UserDict trick described in https://github.com/pastelmind/d2txt/issues/15
#     # This forces qtoml to encode UserDict as inline tables
#     toml_encoder.st[UserDict] = toml_encoder.dump_itable
#
#     toml_header = (
#         "columns = [\n"
#         + "".join(f"  {toml_encoder.dump_value(key)},\n" for key in columns)
#         + "]\n\n"
#     )
#
#     toml_body_data = {}
#     if colgroups:
#         toml_body_data["column_groups"] = {
#             column_group.alias: deepwrap_userdict(column_group.schema)
#             for column_group in columns_with_colgroups
#             if isinstance(column_group, ColumnGroupRule)
#         }
#     toml_body_data["rows"] = toml_rows
#
#     toml_body = toml_encoder.dump_sections(toml_body_data, [], False)
#     return toml_header + toml_body


def unpack_colgroup(
    schema: ColumnGroupSchema, value: Union[Mapping, Collection, str]
) -> Iterator[Tuple[str, Union[int, str]]]:
    """Recursively unpacks a column group, yielding column names and values."""
    if isinstance(value, (int, str)):
        yield schema, value
    elif isinstance(value, collections.abc.Mapping):
        for key, sub_value in value.items():
            yield from unpack_colgroup(schema[key], sub_value)
    else:
        for index, sub_value in enumerate(value):
            yield from unpack_colgroup(schema[index], sub_value)


# def toml_to_d2txt(toml_data: str) -> D2TXT:
#     """Loads a D2TXT file from TOML markup.
#
#     Args:
#         toml_data: String containing TOML markup.
#
#     Returns:
#         D2TXT object loaded from `toml_data`.
#     """
#     # Use toml.loads() because it's ~50% faster than qtoml.loads()
#     toml_data = toml.loads(toml_data)
#     d2txt_data = D2TXT(toml_data["columns"])
#     column_groups = toml_data.get("column_groups", {})
#
#     for toml_row in toml_data["rows"]:
#         # Create and use a D2TXTRow object to catch invalid column names
#         d2txt_data.append([])
#         d2txt_row = d2txt_data[-1]
#
#         for key, value in toml_row.items():
#             try:
#                 schema = column_groups[key]
#             except KeyError:
#                 # Assume that columns in colgroups are not specially encoded
#                 d2txt_row[key] = decode_toml_value(key, value)
#             else:
#                 # Unpack column groups
#                 for column_name, column_value in unpack_colgroup(schema, value):
#                     d2txt_row[column_name] = column_value
#
#     return d2txt_data


def grouper(iterable: Iterable, n: int, fillvalue: Any = None) -> Iterator[tuple]:
    """Collect data into fixed-length chunks or blocks.

    Based on the `grouper()` recipe at
        https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    # pylint: disable=invalid-name
    args = [iter(iterable)] * n
    # pylint: enable=invalid-name
    return itertools.zip_longest(*args, fillvalue=fillvalue)


# def main(argv: List[str] = None) -> None:
#     """Entrypoint of the command line script."""
#     arg_parser = ArgumentParser()
#     arg_subparsers = arg_parser.add_subparsers(dest="command")
#
#     arg_parser_compile = arg_subparsers.add_parser(
#         "compile", help="Compile a TOML file to a tabbed TXT file"
#     )
#     arg_parser_compile.add_argument(
#         "source_target",
#         help="Pair of source file (TOML) and target file (TXT)",
#         metavar="source target",
#         nargs="+",
#     )
#
#     arg_parser_decompile = arg_subparsers.add_parser(
#         "decompile", help="Decompile a tabbed TXT file to a TOML file"
#     )
#     arg_parser_decompile.add_argument(
#         "source_target",
#         help="Pair of source file (TXT) and target file (TOML)",
#         metavar="source target",
#         nargs="+",
#     )
#
#     args = arg_parser.parse_args(argv)
#
#     if args.command is None:
#         arg_parser.print_help()
#     elif args.command == "compile":
#         for source, target in grouper(args.source_target, 2):
#             if not source:
#                 raise ValueError(f"Invalid source file {source!r}")
#             if not target:
#                 raise ValueError(f"Missing target for source {source!r}")
#             with open(source, encoding="utf-8") as toml_file:
#                 d2txt_data = toml_to_d2txt(toml_file.read())
#             d2txt_data.to_txt(target)
#     elif args.command == "decompile":
#         for source, target in grouper(args.source_target, 2):
#             if not source:
#                 raise ValueError(f"Invalid source file {source!r}")
#             if not target:
#                 raise ValueError(f"Missing target for source {source!r}")
#             d2txt_file = D2TXT.load_txt(source)
#             with open(target, mode="w", encoding="utf-8") as toml_file:
#                 toml_file.write(d2txt_to_toml(d2txt_file))
#     else:
#         raise ValueError(f"Unexpected command: {args.command!r}")
#
#
# if __name__ == "__main__":
#     main()
