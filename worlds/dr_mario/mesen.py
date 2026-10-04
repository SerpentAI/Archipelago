from typing import Dict, List, Optional, Sequence, Tuple

import ctypes
import ctypes.wintypes
import struct
import time

import pymem.process
import pymem.ressources.kernel32
import pymem.ressources.structure

from pymem import Pymem


ctypes.windll.kernel32.CreateRemoteThread.restype = ctypes.wintypes.HANDLE

ctypes.windll.kernel32.CreateRemoteThread.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.wintypes.DWORD,
    ctypes.c_void_p,
]


MESEN_SIZE_OF_IMAGE: int = 0x4741000
MESEN_TIME_DATE_STAMP: int = 0x6A229843

MESEN_EXPORT_RVAS: Dict[str, int] = {
    "ClearCheats": 0x559D0,
    "DisplayMessage": 0x556C0,
    "ExecuteShortcut": 0x55C50,
    "GetMesenVersion": 0x547B0,
    "LoadState": 0x55D10,
    "LoadStateFile": 0x55D90,
    "Pause": 0x55560,
    "RegisterNotificationCallback": 0x55690,
    "ResetLagCounter": 0x65DF0,
    "Resume": 0x55590,
    "SaveState": 0x55CF0,
    "SaveStateFile": 0x55D30,
    "SetCheats": 0x559F0,
    "SetEmulationFlag": 0x53370,
    "TakeScreenshot": 0x551C0,
    "UnregisterNotificationCallback": 0x556B0,
    "WriteLogEntry": 0x55CA0,
}

MESEN_FUNCTION_RVAS: Dict[str, int] = {
    "NesController::InternalSetStateFromInput": 0x19E940,
    "NotificationManager::SendNotification": 0xB3BA0,
}

MESEN_GLOBAL_RVAS: Dict[str, int] = {
    "_emu": 0x46DC798,
    "_listeners": 0x46DC770,
}

MESEN_VIRTUAL_TABLE_RVAS: Dict[str, int] = {
    "NesController": 0x5F2218,
}

MESEN_VIRTUAL_TABLE_OFFSETS: Dict[str, int] = {
    "BaseControlDevice::InternalSetStateFromInput": 0x28,
}

EMULATOR_MEMBER_OFFSETS: Dict[str, int] = {
    "_console": 0x0,
    "_consoleMemory": 0x280,
    "_consoleType": 0x278,
    "_debugger": 0x40,
    "_isRunAheadFrame": 0x150,
    "_notificationManager": 0xA0,
    "_paused": 0x145,
    "_rom.Format": 0x268,
    "_rom.PatchFile._path": 0x1E0,
    "_rom.RomFile._path": 0x158,
    "_settings": 0x88,
}

EMU_SETTINGS_MEMBER_OFFSETS: Dict[str, int] = {
    "_emulation": 0x1568,
    "_flags": 0xBC14,
}

DEBUGGER_MEMBER_OFFSETS: Dict[str, int] = {
    "_waitForBreakResume": 0x21C,
}

INTEROP_NOTIFICATION_LISTENERS_MEMBER_OFFSETS: Dict[str, int] = {
    "_externalNotificationListeners": 0x10,
}

INTEROP_NOTIFICATION_LISTENER_MEMBER_OFFSETS: Dict[str, int] = {
    "_callback": 0x8,
}

NES_CONSOLE_MEMBER_OFFSETS: Dict[str, int] = {
    "_apu": 0x38,
    "_controlManager": 0x50,
    "_cpu": 0x28,
    "_emu": 0x10,
    "_mapper": 0x48,
    "_memoryManager": 0x40,
    "_ppu": 0x30,
    "_region": 0x98,
}

NES_CPU_MEMBER_OFFSETS: Dict[str, int] = {
    "_state": 0xC28,
}

BASE_NES_PPU_MEMBER_OFFSETS: Dict[str, int] = {
    "_control": 0xC0,
    "_cycle": 0x18,
    "_frameCount": 0xA8,
    "_mask": 0xC8,
    "_masterClock": 0x10,
    "_scanline": 0x1C,
    "_statusFlags": 0x360,
    "_tmpVideoRamAddr": 0x22,
    "_videoRamAddr": 0x20,
    "_writeToggle": 0xAF,
    "_xScroll": 0x2B,
}

BASE_MAPPER_MEMBER_OFFSETS: Dict[str, int] = {
    "_chrMemoryAccess": 0x20C68,
    "_chrMemoryOffset": 0x21768,
    "_chrMemoryType": 0x21868,
    "_internalRamMask": 0x50,
    "_mirroringType": 0x18,
    "_originalChrRom": 0x21980,
    "_originalPrgRom": 0x21968,
    "_prgMemoryAccess": 0x20068,
    "_prgMemoryOffset": 0x20F68,
    "_prgMemoryType": 0x21368,
    "_romInfo.Filename": 0x219B8,
    "_romInfo.Format": 0x219D8,
    "_romInfo.HasBattery": 0x219F9,
    "_romInfo.HasChrRam": 0x219F8,
    "_romInfo.Hash": 0x21A04,
    "_romInfo.IsInDatabase": 0x219DD,
    "_romInfo.IsNes20Header": 0x219DC,
    "_romInfo.MapperID": 0x219E4,
    "_romInfo.RomName": 0x21998,
    "_romInfo.SubMapperID": 0x219E6,
}

NES_CONTROL_MANAGER_MEMBER_OFFSETS: Dict[str, int] = {
    "_controlDevices": 0x70,
    "_lagCounter": 0x8C,
    "_pollCounter": 0x88,
}

BASE_CONTROL_DEVICE_MEMBER_OFFSETS: Dict[str, int] = {
    "_connected": 0x49,
    "_port": 0x48,
    "_state": 0x8,
    "_type": 0x44,
}

MEMORY_TYPES: Dict[str, int] = {
    "NesChrRam": 56,
    "NesChrRom": 57,
    "NesInternalRam": 48,
    "NesMapperRam": 52,
    "NesNametableRam": 51,
    "NesPaletteRam": 55,
    "NesPrgRom": 47,
    "NesSaveRam": 50,
    "NesSecondarySpriteRam": 54,
    "NesSpriteRam": 53,
    "NesWorkRam": 49,
}

MEMORY_TYPE_COUNT: int = 93

PRG_MEMORY_TYPE_TO_MEMORY_TYPE: Dict[int, int] = {
    0: MEMORY_TYPES["NesPrgRom"],
    1: MEMORY_TYPES["NesSaveRam"],
    2: MEMORY_TYPES["NesWorkRam"],
    3: MEMORY_TYPES["NesMapperRam"],
}

CHR_MEMORY_TYPE_TO_MEMORY_TYPE: Dict[int, int] = {
    1: MEMORY_TYPES["NesChrRom"],
    2: MEMORY_TYPES["NesChrRam"],
    3: MEMORY_TYPES["NesNametableRam"],
    4: MEMORY_TYPES["NesMapperRam"],
}

CONSOLE_TYPES: Dict[str, int] = {
    "Gameboy": 1,
    "Gba": 5,
    "Nes": 2,
    "PcEngine": 3,
    "Sms": 4,
    "Snes": 0,
    "Ws": 6,
}

CONSOLE_REGIONS: Dict[str, int] = {
    "Auto": 0,
    "Dendy": 3,
    "Ntsc": 1,
    "NtscJapan": 4,
    "Pal": 2,
}

CONSOLE_NOTIFICATION_TYPES: Dict[str, int] = {
    "AfterInitConsole": 23,
    "BeforeEmulationStop": 12,
    "BeforeGameLoad": 18,
    "BeforeGameUnload": 17,
    "CheatsChanged": 20,
    "CodeBreak": 5,
    "DebuggerResumed": 6,
    "EmulationStopped": 11,
    "EventViewerRefresh": 14,
    "ExecuteShortcut": 9,
    "GameLoadFailed": 19,
    "GameLoaded": 0,
    "GamePaused": 3,
    "GameReset": 2,
    "GameResumed": 4,
    "MissingFirmware": 15,
    "NetplayStopped": 24,
    "PpuFrameDone": 7,
    "RefreshSoftwareRenderer": 22,
    "ReleaseShortcut": 10,
    "RequestConfigChange": 21,
    "ResolutionChanged": 8,
    "StateLoaded": 1,
    "SufamiTurboFilePrompt": 16,
    "ViewerRefresh": 13,
}

EMULATOR_SHORTCUTS: Dict[str, int] = {
    "DecreaseSpeed": 27,
    "DecreaseVolume": 59,
    "EnableAllLayers": 68,
    "ExecPowerCycle": 36,
    "ExecPowerOff": 38,
    "ExecReloadRom": 37,
    "ExecReset": 35,
    "Exit": 34,
    "FastForward": 0,
    "FdsEjectDisk": 102,
    "FdsInsertDiskNumber": 103,
    "FdsInsertNextDisk": 104,
    "FdsSwitchDiskSide": 101,
    "IncreaseSpeed": 26,
    "IncreaseVolume": 58,
    "InputBarcode": 97,
    "LoadLastSession": 95,
    "LoadState": 17,
    "LoadStateDialog": 94,
    "LoadStateFromFile": 93,
    "LoadStateSlot1": 82,
    "LoadStateSlot10": 91,
    "LoadStateSlot2": 83,
    "LoadStateSlot3": 84,
    "LoadStateSlot4": 85,
    "LoadStateSlot5": 86,
    "LoadStateSlot6": 87,
    "LoadStateSlot7": 88,
    "LoadStateSlot8": 89,
    "LoadStateSlot9": 90,
    "LoadStateSlotAuto": 92,
    "LoadTape": 98,
    "MaxSpeed": 28,
    "MoveToNextStateSlot": 14,
    "MoveToPreviousStateSlot": 15,
    "NextTrack": 61,
    "OpenFile": 96,
    "Pause": 29,
    "PowerCycle": 31,
    "PowerOff": 33,
    "PreviousTrack": 60,
    "RecordTape": 99,
    "ReloadRom": 32,
    "Reset": 30,
    "ResetLagCounter": 69,
    "Rewind": 1,
    "RewindOneMin": 3,
    "RewindTenSecs": 2,
    "RunSingleFrame": 21,
    "SaveState": 16,
    "SaveStateDialog": 81,
    "SaveStateSlot1": 70,
    "SaveStateSlot10": 79,
    "SaveStateSlot2": 71,
    "SaveStateSlot3": 72,
    "SaveStateSlot4": 73,
    "SaveStateSlot5": 74,
    "SaveStateSlot6": 75,
    "SaveStateSlot7": 76,
    "SaveStateSlot8": 77,
    "SaveStateSlot9": 78,
    "SaveStateToFile": 80,
    "SelectSaveSlot1": 4,
    "SelectSaveSlot10": 13,
    "SelectSaveSlot2": 5,
    "SelectSaveSlot3": 6,
    "SelectSaveSlot4": 7,
    "SelectSaveSlot5": 8,
    "SelectSaveSlot6": 9,
    "SelectSaveSlot7": 10,
    "SelectSaveSlot8": 11,
    "SelectSaveSlot9": 12,
    "SetScale10x": 48,
    "SetScale1x": 39,
    "SetScale2x": 40,
    "SetScale3x": 41,
    "SetScale4x": 42,
    "SetScale5x": 43,
    "SetScale6x": 44,
    "SetScale7x": 45,
    "SetScale8x": 46,
    "SetScale9x": 47,
    "StartRecordHdPack": 111,
    "StopRecordHdPack": 112,
    "StopRecordTape": 100,
    "TakeScreenshot": 22,
    "ToggleAlwaysOnTop": 55,
    "ToggleAudio": 57,
    "ToggleBgLayer1": 62,
    "ToggleBgLayer2": 63,
    "ToggleBgLayer3": 64,
    "ToggleBgLayer4": 65,
    "ToggleCheats": 18,
    "ToggleDebugInfo": 56,
    "ToggleFastForward": 19,
    "ToggleFps": 50,
    "ToggleFrameCounter": 52,
    "ToggleFullscreen": 49,
    "ToggleGameTimer": 51,
    "ToggleLagCounter": 53,
    "ToggleOsd": 54,
    "ToggleRecordAudio": 24,
    "ToggleRecordMovie": 25,
    "ToggleRecordVideo": 23,
    "ToggleRewind": 20,
    "ToggleSprites1": 66,
    "ToggleSprites2": 67,
    "VsInsertCoin1": 107,
    "VsInsertCoin2": 108,
    "VsInsertCoin3": 109,
    "VsInsertCoin4": 110,
    "VsServiceButton": 105,
    "VsServiceButton2": 106,
}

EMULATION_FLAGS: Dict[str, int] = {
    "ConsoleMode": 0x10,
    "InBackground": 0x08,
    "MaximumSpeed": 0x04,
    "OutputToStdout": 0x40,
    "Rewind": 0x02,
    "TestMode": 0x20,
    "Turbo": 0x01,
}

CHEAT_TYPES: Dict[str, int] = {
    "NesCustom": 2,
    "NesGameGenie": 0,
    "NesProActionRocky": 1,
}

NES_CONTROLLER_BUTTONS: Dict[str, int] = {
    "A": 7,
    "B": 6,
    "Down": 1,
    "Left": 2,
    "Right": 3,
    "Select": 5,
    "Start": 4,
    "Up": 0,
}

CALLBACK_CODE_OFFSET: int = 0x0000
INPUT_HOOK_CODE_OFFSET: int = 0x0280
REMOTE_CALL_CODE_OFFSET: int = 0x0300
REMOTE_CALL_RESULT_OFFSET: int = 0x0380
ARGUMENT_BUFFER_OFFSET: int = 0x0400
CALLBACK_DATA_OFFSET: int = 0x0C00
EVENT_LOG_OFFSET: int = 0x0D00
WATCH_TABLE_OFFSET: int = 0x1500
WRITE_RECORDS_OFFSET: int = 0x1600
INPUT_OVERRIDES_OFFSET: int = 0x1E00
WRITE_DATA_OFFSET: int = 0x2400
SNAPSHOT_OFFSET: int = 0x6000
CAVE_SIZE: int = 0xE000

ARGUMENT_BUFFER_SIZE: int = 0x800
EVENT_LOG_CAPACITY: int = 128
WATCH_CAPACITY: int = 16
INPUT_OVERRIDE_CAPACITY: int = 4
INPUT_OVERRIDE_SIZE: int = 0x110
WRITE_RECORD_CAPACITY: int = 128
WRITE_DATA_SIZE: int = 0x3C00
SNAPSHOT_SIZE: int = 0x8000

CALLBACK_MAGIC: int = 0x4E454D4553454E41
WRITE_STATE_IDLE: int = 0
WRITE_STATE_PENDING: int = 1
WRITE_STATE_DONE: int = 2


def assemble(parts: Sequence) -> bytes:
    label_positions: Dict[str, int] = dict()
    position: int = 0

    part: object
    for part in parts:
        if isinstance(part, bytes):
            position += len(part)
        elif part[0] == "label":
            label_positions[part[1]] = position
        elif part[0] == "jump":
            position += len(part[1]) + 1
        elif part[0] == "near_jump":
            position += len(part[1]) + 4

    code: bytes = bytes()

    for part in parts:
        if isinstance(part, bytes):
            code += part
        elif part[0] == "jump":
            code += part[1] + struct.pack("<b", label_positions[part[2]] - (len(code) + len(part[1]) + 1))
        elif part[0] == "near_jump":
            code += part[1] + struct.pack("<i", label_positions[part[2]] - (len(code) + len(part[1]) + 4))

    return code


def assemble_6502(parts: Sequence, base_address: int) -> bytes:
    label_positions: Dict[str, int] = dict()
    position: int = 0

    part: object
    for part in parts:
        if isinstance(part, bytes):
            position += len(part)
        elif part[0] == "label":
            label_positions[part[1]] = position
        elif part[0] in ("branch", "low", "high"):
            position += len(part[1]) + 1
        elif part[0] == "absolute":
            position += len(part[1]) + 2

    code: bytes = bytes()

    for part in parts:
        if isinstance(part, bytes):
            code += part
        elif part[0] == "branch":
            distance: int = label_positions[part[2]] - (len(code) + len(part[1]) + 1)

            if not -128 <= distance <= 127:
                raise RuntimeError(f"Branch to {part[2]} is out of range ({distance})")

            code += part[1] + struct.pack("<b", distance)
        elif part[0] == "absolute":
            code += part[1] + struct.pack("<H", base_address + label_positions[part[2]])
        elif part[0] == "low":
            code += part[1] + struct.pack("<B", (base_address + label_positions[part[2]]) & 0xFF)
        elif part[0] == "high":
            code += part[1] + struct.pack("<B", (base_address + label_positions[part[2]]) >> 8)

    return code


def build_callback_code(cave_address: int) -> bytes:
    console_memory: bytes = struct.pack("<i", EMULATOR_MEMBER_OFFSETS["_consoleMemory"])
    snapshot_end: bytes = struct.pack("<i", SNAPSHOT_OFFSET + SNAPSHOT_SIZE - CALLBACK_DATA_OFFSET)
    write_data_end: bytes = struct.pack("<i", WRITE_DATA_OFFSET + WRITE_DATA_SIZE - CALLBACK_DATA_OFFSET)

    return assemble([
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x57",  # push rdi
        b"\x41\x54",  # push r12
        b"\x41\x55",  # push r13
        b"\x41\x56",  # push r14
        b"\x49\xBE" + struct.pack("<Q", cave_address + CALLBACK_DATA_OFFSET),  # mov r14, callback data
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["PpuFrameDone"]),  # cmp ecx, frame done
        ("near_jump", b"\x0F\x85", "event"),  # jne event

        b"\x49\x8B\x46\x08",  # mov rax, [r14 + 0x08]  ; emulator global
        b"\x48\x8B\x18",  # mov rbx, [rax]  ; emulator
        b"\x48\x85\xDB",  # test rbx, rbx
        ("near_jump", b"\x0F\x84", "done"),  # je done
        b"\x0F\xB6\x83" + struct.pack("<i", EMULATOR_MEMBER_OFFSETS["_isRunAheadFrame"]),  # movzx eax, byte [rbx + run ahead frame]
        b"\x41\x0F\xB6\x4E\x20",  # movzx ecx, byte [r14 + 0x20]  ; previous run ahead frame
        b"\x41\x88\x46\x20",  # mov [r14 + 0x20], al
        b"\x85\xC9",  # test ecx, ecx
        ("near_jump", b"\x0F\x85", "done"),  # jne done
        b"\x49\xFF\x46\x18",  # inc qword [r14 + 0x18]  ; frame count

        b"\x41\x83\x7E\x30" + struct.pack("<b", WRITE_STATE_PENDING),  # cmp dword [r14 + 0x30], pending
        ("near_jump", b"\x0F\x85", "snapshot"),  # jne snapshot
        b"\x45\x8B\x66\x34",  # mov r12d, [r14 + 0x34]  ; write count
        b"\x4D\x8D\xAE" + struct.pack("<i", WRITE_RECORDS_OFFSET - CALLBACK_DATA_OFFSET),  # lea r13, [r14 + write records]

        ("label", "next_write"),
        b"\x45\x85\xE4",  # test r12d, r12d
        ("near_jump", b"\x0F\x84", "writes_done"),  # je writes_done
        b"\x41\x8B\x45\x00",  # mov eax, [r13]  ; memory type
        b"\x83\xF8" + struct.pack("<b", MEMORY_TYPE_COUNT),  # cmp eax, memory type count
        ("jump", b"\x73", "write_failed"),  # jae write_failed
        b"\x48\xC1\xE0\x04",  # shl rax, 4
        b"\x48\x8D\x84\x03" + console_memory,  # lea rax, [rbx + rax + console memory]
        b"\x48\x8B\x38",  # mov rdi, [rax]  ; memory
        b"\x48\x85\xFF",  # test rdi, rdi
        ("jump", b"\x74", "write_failed"),  # je write_failed
        b"\x41\x8B\x4D\x04",  # mov ecx, [r13 + 0x04]  ; offset
        b"\x41\x8B\x55\x08",  # mov edx, [r13 + 0x08]  ; length
        b"\x4C\x8D\x04\x11",  # lea r8, [rcx + rdx]
        b"\x44\x8B\x48\x08",  # mov r9d, [rax + 0x08]  ; memory size
        b"\x4D\x39\xC8",  # cmp r8, r9
        ("jump", b"\x77", "write_failed"),  # ja write_failed
        b"\x41\x8B\x75\x0C",  # mov esi, [r13 + 0x0C]  ; data offset
        b"\x4C\x8D\x04\x16",  # lea r8, [rsi + rdx]
        b"\x49\x81\xF8" + write_data_end,  # cmp r8, write data end
        ("jump", b"\x77", "write_failed"),  # ja write_failed
        b"\x48\x01\xCF",  # add rdi, rcx
        b"\x4C\x01\xF6",  # add rsi, r14
        b"\x89\xD1",  # mov ecx, edx
        b"\xF3\xA4",  # rep movsb
        ("jump", b"\xEB", "write_next"),  # jmp write_next

        ("label", "write_failed"),
        b"\x41\xFF\x46\x38",  # inc dword [r14 + 0x38]  ; write failures

        ("label", "write_next"),
        b"\x49\x83\xC5\x10",  # add r13, 0x10
        b"\x41\xFF\xCC",  # dec r12d
        ("near_jump", b"\xE9", "next_write"),  # jmp next_write

        ("label", "writes_done"),
        b"\x41\xC7\x46\x30" + struct.pack("<i", WRITE_STATE_DONE),  # mov dword [r14 + 0x30], done

        ("label", "snapshot"),
        b"\x45\x8B\x66\x3C",  # mov r12d, [r14 + 0x3C]  ; watch count
        b"\x45\x85\xE4",  # test r12d, r12d
        ("near_jump", b"\x0F\x84", "done"),  # je done
        b"\x41\xFF\x46\x40",  # inc dword [r14 + 0x40]  ; snapshot sequence
        b"\x4D\x8D\xAE" + struct.pack("<i", WATCH_TABLE_OFFSET - CALLBACK_DATA_OFFSET),  # lea r13, [r14 + watch table]

        ("label", "next_watch"),
        b"\x41\x8B\x45\x00",  # mov eax, [r13]  ; memory type
        b"\x83\xF8" + struct.pack("<b", MEMORY_TYPE_COUNT),  # cmp eax, memory type count
        ("jump", b"\x73", "watch_next"),  # jae watch_next
        b"\x48\xC1\xE0\x04",  # shl rax, 4
        b"\x48\x8D\x84\x03" + console_memory,  # lea rax, [rbx + rax + console memory]
        b"\x48\x8B\x30",  # mov rsi, [rax]  ; memory
        b"\x48\x85\xF6",  # test rsi, rsi
        ("jump", b"\x74", "watch_next"),  # je watch_next
        b"\x41\x8B\x4D\x04",  # mov ecx, [r13 + 0x04]  ; offset
        b"\x41\x8B\x55\x08",  # mov edx, [r13 + 0x08]  ; length
        b"\x4C\x8D\x04\x11",  # lea r8, [rcx + rdx]
        b"\x44\x8B\x48\x08",  # mov r9d, [rax + 0x08]  ; memory size
        b"\x4D\x39\xC8",  # cmp r8, r9
        ("jump", b"\x77", "watch_next"),  # ja watch_next
        b"\x41\x8B\x7D\x0C",  # mov edi, [r13 + 0x0C]  ; snapshot offset
        b"\x4C\x8D\x04\x17",  # lea r8, [rdi + rdx]
        b"\x49\x81\xF8" + snapshot_end,  # cmp r8, snapshot end
        ("jump", b"\x77", "watch_next"),  # ja watch_next
        b"\x48\x01\xCE",  # add rsi, rcx
        b"\x4C\x01\xF7",  # add rdi, r14
        b"\x89\xD1",  # mov ecx, edx
        b"\xF3\xA4",  # rep movsb

        ("label", "watch_next"),
        b"\x49\x83\xC5\x10",  # add r13, 0x10
        b"\x41\xFF\xCC",  # dec r12d
        ("jump", b"\x75", "next_watch"),  # jne next_watch
        b"\x49\x8B\x46\x18",  # mov rax, [r14 + 0x18]  ; frame count
        b"\x49\x89\x46\x48",  # mov [r14 + 0x48], rax  ; snapshot frame count
        b"\x41\xFF\x46\x40",  # inc dword [r14 + 0x40]  ; snapshot sequence
        ("near_jump", b"\xE9", "done"),  # jmp done

        ("label", "event"),
        b"\x83\xF9\x20",  # cmp ecx, 32
        ("near_jump", b"\x0F\x83", "done"),  # jae done
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["BeforeGameUnload"]),  # cmp ecx, before game unload
        ("jump", b"\x74", "drop_writes"),  # je drop_writes
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["GameLoaded"]),  # cmp ecx, game loaded
        ("jump", b"\x75", "check_mask"),  # jne check_mask

        ("label", "drop_writes"),
        b"\x41\x83\x7E\x30" + struct.pack("<b", WRITE_STATE_PENDING),  # cmp dword [r14 + 0x30], pending
        ("jump", b"\x75", "check_mask"),  # jne check_mask
        b"\x41\x8B\x46\x34",  # mov eax, [r14 + 0x34]  ; write count
        b"\x41\x89\x46\x38",  # mov [r14 + 0x38], eax  ; write failures
        b"\x41\xC7\x46\x30" + struct.pack("<i", WRITE_STATE_DONE),  # mov dword [r14 + 0x30], done

        ("label", "check_mask"),
        b"\x41\x8B\x46\x2C",  # mov eax, [r14 + 0x2C]  ; event mask
        b"\x0F\xA3\xC8",  # bt eax, ecx
        ("near_jump", b"\x0F\x83", "done"),  # jnc done
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["StateLoaded"]),  # cmp ecx, state loaded
        ("jump", b"\x75", "not_run_ahead_state"),  # jne not_run_ahead_state
        b"\x49\x8B\x46\x08",  # mov rax, [r14 + 0x08]  ; emulator global
        b"\x48\x8B\x00",  # mov rax, [rax]  ; emulator
        b"\x48\x85\xC0",  # test rax, rax
        ("jump", b"\x74", "not_run_ahead_state"),  # je not_run_ahead_state
        b"\x80\xB8" + struct.pack("<i", EMULATOR_MEMBER_OFFSETS["_isRunAheadFrame"]) + b"\x00",  # cmp byte [rax + run ahead frame], 0
        ("near_jump", b"\x0F\x85", "done"),  # jne done

        ("label", "not_run_ahead_state"),
        b"\x45\x31\xC0",  # xor r8d, r8d  ; parameter
        b"\x48\x85\xD2",  # test rdx, rdx
        ("jump", b"\x74", "store_event"),  # je store_event
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["GameLoaded"]),  # cmp ecx, game loaded
        ("jump", b"\x75", "not_game_loaded"),  # jne not_game_loaded
        b"\x44\x0F\xB6\x42\x01",  # movzx r8d, byte [rdx + 1]  ; is power cycle
        ("jump", b"\xEB", "store_event"),  # jmp store_event

        ("label", "not_game_loaded"),
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["ExecuteShortcut"]),  # cmp ecx, execute shortcut
        ("jump", b"\x74", "shortcut"),  # je shortcut
        b"\x83\xF9" + struct.pack("<b", CONSOLE_NOTIFICATION_TYPES["ReleaseShortcut"]),  # cmp ecx, release shortcut
        ("jump", b"\x75", "store_event"),  # jne store_event

        ("label", "shortcut"),
        b"\x44\x8B\x02",  # mov r8d, [rdx]  ; shortcut

        ("label", "store_event"),
        b"\xB8\x01\x00\x00\x00",  # mov eax, 1
        b"\xF0\x41\x0F\xC1\x46\x28",  # lock xadd [r14 + 0x28], eax  ; event count
        b"\x44\x8D\x48\x01",  # lea r9d, [rax + 1]  ; event sequence
        b"\x83\xE0" + struct.pack("<b", EVENT_LOG_CAPACITY - 1),  # and eax, event log capacity - 1
        b"\xC1\xE0\x04",  # shl eax, 4
        b"\x49\x8D\xBC\x06" + struct.pack("<i", EVENT_LOG_OFFSET - CALLBACK_DATA_OFFSET),  # lea rdi, [r14 + rax + event log]
        b"\x66\x89\x4F\x04",  # mov [rdi + 0x04], cx  ; type
        b"\x66\x44\x89\x47\x06",  # mov [rdi + 0x06], r8w  ; parameter
        b"\x49\x8B\x46\x18",  # mov rax, [r14 + 0x18]  ; frame count
        b"\x48\x89\x47\x08",  # mov [rdi + 0x08], rax
        b"\x44\x89\x0F",  # mov [rdi], r9d  ; event sequence

        ("label", "done"),
        b"\x41\x5E",  # pop r14
        b"\x41\x5D",  # pop r13
        b"\x41\x5C",  # pop r12
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xC3",  # ret
    ])


def build_input_hook_code(cave_address: int) -> bytes:
    return assemble([
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x48\x83\xEC\x28",  # sub rsp, 0x28
        b"\x48\x89\xCB",  # mov rbx, rcx  ; controller
        b"\x48\xBE" + struct.pack("<Q", cave_address + CALLBACK_DATA_OFFSET),  # mov rsi, callback data
        b"\xFF\x56\x50",  # call [rsi + 0x50]  ; original InternalSetStateFromInput

        b"\x0F\xB6\x43" + struct.pack("<b", BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_port"]),  # movzx eax, byte [rbx + port]
        b"\x83\xF8" + struct.pack("<b", INPUT_OVERRIDE_CAPACITY),  # cmp eax, input override capacity
        ("jump", b"\x73", "done"),  # jae done
        b"\x69\xC0" + struct.pack("<i", INPUT_OVERRIDE_SIZE),  # imul eax, eax, input override size
        b"\x48\x8D\x94\x06" + struct.pack("<i", INPUT_OVERRIDES_OFFSET - CALLBACK_DATA_OFFSET),  # lea rdx, [rsi + rax + input overrides]
        b"\x8B\x0A",  # mov ecx, [rdx]  ; frames remaining
        b"\x85\xC9",  # test ecx, ecx
        ("jump", b"\x74", "done"),  # je done
        b"\x4C\x8B\x43" + struct.pack("<b", BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_state"]),  # mov r8, [rbx + state]  ; state begin
        b"\x4C\x3B\x43" + struct.pack("<b", BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_state"] + 8),  # cmp r8, [rbx + state + 8]  ; state end
        ("jump", b"\x73", "done"),  # jae done
        b"\x41\x0F\xB6\x00",  # movzx eax, byte [r8]  ; buttons
        b"\x0F\xB6\x44\x02\x10",  # movzx eax, byte [rdx + rax + 0x10]  ; input table
        b"\x41\x88\x00",  # mov [r8], al
        b"\x83\xF9\xFF",  # cmp ecx, -1
        ("jump", b"\x74", "done"),  # je done
        b"\x80\x7E\x20\x00",  # cmp byte [rsi + 0x20], 0  ; previous run ahead frame
        ("jump", b"\x75", "done"),  # jne done
        b"\xFF\x0A",  # dec dword [rdx]  ; frames remaining

        ("label", "done"),
        b"\x48\x83\xC4\x28",  # add rsp, 0x28
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xC3",  # ret
    ])


def build_remote_call_code(function_address: int, arguments: Sequence[int], result_address: int) -> bytes:
    padded_arguments: List[int] = (list(arguments) + [0, 0, 0, 0])[:4]

    return assemble([
        b"\x48\x83\xEC\x28",  # sub rsp, 0x28
        b"\x48\xB9" + struct.pack("<Q", padded_arguments[0]),  # mov rcx, argument 1
        b"\x48\xBA" + struct.pack("<Q", padded_arguments[1]),  # mov rdx, argument 2
        b"\x49\xB8" + struct.pack("<Q", padded_arguments[2]),  # mov r8, argument 3
        b"\x49\xB9" + struct.pack("<Q", padded_arguments[3]),  # mov r9, argument 4
        b"\x48\xB8" + struct.pack("<Q", function_address),  # mov rax, function
        b"\xFF\xD0",  # call rax
        b"\x49\xBA" + struct.pack("<Q", result_address),  # mov r10, result
        b"\x49\x89\x02",  # mov [r10], rax
        b"\x48\x83\xC4\x28",  # add rsp, 0x28
        b"\x31\xC0",  # xor eax, eax
        b"\xC3",  # ret
    ])


class MesenNesProcess:
    process: Pymem
    module_base: int

    cave_address: Optional[int]
    event_cursor: Optional[int]
    remote_call_thread: Optional[int]
    remote_call_timeout_seconds: float

    def __init__(self, process: Pymem) -> None:
        self.process = process
        module: Optional[pymem.ressources.structure.MODULEINFO] = pymem.process.module_from_name(self.process.process_handle, "MesenCore.dll")

        if module is None:
            raise RuntimeError("MesenCore.dll is not loaded; is Mesen still starting?")

        self.module_base = module.lpBaseOfDll

        pe_header_offset: int = self.process.read_int(self.module_base + 0x3C)
        time_date_stamp: int = self.process.read_uint(self.module_base + pe_header_offset + 8)

        if module.SizeOfImage != MESEN_SIZE_OF_IMAGE or time_date_stamp != MESEN_TIME_DATE_STAMP:
            raise RuntimeError("This Mesen build is not supported; Mesen 2.2.1 (Windows) is required")

        self.cave_address = None
        self.event_cursor = None
        self.remote_call_thread = None
        self.remote_call_timeout_seconds = 5.0

    def read_mesen_version(self) -> Tuple[int, int, int]:
        version: int = self.process.read_uint(self.module_base + MESEN_EXPORT_RVAS["GetMesenVersion"] + 1)

        return version >> 16, (version >> 8) & 0xFF, version & 0xFF

    def read_emulator_address(self) -> int:
        return self._read_pointer(self.module_base + MESEN_GLOBAL_RVAS["_emu"])

    def is_game_running(self) -> bool:
        try:
            return self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_console"]) != 0
        except Exception:
            return False

    def is_nes_game_running(self) -> bool:
        try:
            return self.is_game_running() and self.read_console_type() == CONSOLE_TYPES["Nes"]
        except Exception:
            return False

    def read_console_type(self) -> int:
        return self.process.read_int(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_consoleType"])

    def read_console_address(self) -> int:
        if not self.is_nes_game_running():
            raise RuntimeError("No NES game is running in Mesen")

        return self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_console"])

    def is_paused(self) -> bool:
        emulator_address: int = self.read_emulator_address()
        debugger_address: int = self._read_pointer(emulator_address + EMULATOR_MEMBER_OFFSETS["_debugger"])

        if debugger_address != 0:
            return bool(self.process.read_uchar(debugger_address + DEBUGGER_MEMBER_OFFSETS["_waitForBreakResume"]))

        return bool(self.process.read_uchar(emulator_address + EMULATOR_MEMBER_OFFSETS["_paused"]))

    def is_debugger_active(self) -> bool:
        return self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_debugger"]) != 0

    def is_run_ahead_frame(self) -> bool:
        return bool(self.process.read_uchar(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_isRunAheadFrame"]))

    def read_emulation_config(self) -> Dict[str, int]:
        settings_address: int = self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_settings"])
        emulation_speed, turbo_speed, rewind_speed, run_ahead_frames = struct.unpack("<4I", self.process.read_bytes(settings_address + EMU_SETTINGS_MEMBER_OFFSETS["_emulation"], 16))

        return {
            "EmulationSpeed": emulation_speed,
            "RewindSpeed": rewind_speed,
            "RunAheadFrames": run_ahead_frames,
            "TurboSpeed": turbo_speed,
        }

    def read_emulation_flags(self) -> List[str]:
        settings_address: int = self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_settings"])
        flags: int = self.process.read_uint(settings_address + EMU_SETTINGS_MEMBER_OFFSETS["_flags"])

        return [name for name in sorted(EMULATION_FLAGS) if flags & EMULATION_FLAGS[name]]

    def read_rom_path(self) -> str:
        return self._read_std_string(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_rom.RomFile._path"])

    def read_patch_path(self) -> str:
        return self._read_std_string(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_rom.PatchFile._path"])

    def read_rom_format(self) -> int:
        return self.process.read_int(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_rom.Format"])

    def read_memory_region(self, memory_type: int) -> Tuple[int, int]:
        if not self.is_game_running():
            raise RuntimeError("No game is running in Mesen")

        return struct.unpack("<QI", self.process.read_bytes(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_consoleMemory"] + memory_type * 16, 12))

    def read_memory_regions(self) -> Dict[int, Tuple[int, int]]:
        if not self.is_game_running():
            raise RuntimeError("No game is running in Mesen")

        table: bytes = self.process.read_bytes(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_consoleMemory"], MEMORY_TYPE_COUNT * 16)
        regions: Dict[int, Tuple[int, int]] = dict()

        memory_type: int
        for memory_type in range(MEMORY_TYPE_COUNT):
            address, size = struct.unpack_from("<QI", table, memory_type * 16)

            if address != 0 and size != 0:
                regions[memory_type] = (address, size)

        return regions

    def read_memory(self, memory_type: int, offset: int, length: int) -> bytes:
        address, size = self.read_memory_region(memory_type)

        if offset < 0 or length < 0 or offset + length > size:
            raise RuntimeError(f"Read of {length} bytes at {offset:#x} is outside memory type {memory_type} ({size:#x} bytes)")

        return self.process.read_bytes(address + offset, length)

    def write_memory(self, memory_type: int, offset: int, data: bytes) -> None:
        address, size = self.read_memory_region(memory_type)

        if offset < 0 or offset + len(data) > size:
            raise RuntimeError(f"Write of {len(data)} bytes at {offset:#x} is outside memory type {memory_type} ({size:#x} bytes)")

        self.process.write_bytes(address + offset, data, len(data))

    def read_rom_hashes(self) -> Dict[str, int]:
        crc32, prg_crc32, prg_chr_crc32 = struct.unpack("<3I", self.process.read_bytes(self._read_mapper_address() + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.Hash"], 12))

        return {
            "Crc32": crc32,
            "PrgChrCrc32": prg_chr_crc32,
            "PrgCrc32": prg_crc32,
        }

    def read_rom_info(self) -> Dict[str, object]:
        mapper_address: int = self._read_mapper_address()

        return {
            "Filename": self._read_std_string(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.Filename"]),
            "Format": self.process.read_int(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.Format"]),
            "HasBattery": bool(self.process.read_uchar(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.HasBattery"])),
            "HasChrRam": bool(self.process.read_uchar(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.HasChrRam"])),
            "IsInDatabase": bool(self.process.read_uchar(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.IsInDatabase"])),
            "IsNes20Header": bool(self.process.read_uchar(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.IsNes20Header"])),
            "MapperID": self.process.read_ushort(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.MapperID"]),
            "MirroringType": self.process.read_int(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_mirroringType"]),
            "RomName": self._read_std_string(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.RomName"]),
            "SubMapperID": self.process.read_uchar(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_romInfo.SubMapperID"]),
        }

    def read_region(self) -> int:
        return self.process.read_int(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_region"])

    def read_original_prg_rom(self) -> bytes:
        return self._read_byte_vector(self._read_mapper_address() + BASE_MAPPER_MEMBER_OFFSETS["_originalPrgRom"])

    def read_original_chr_rom(self) -> bytes:
        return self._read_byte_vector(self._read_mapper_address() + BASE_MAPPER_MEMBER_OFFSETS["_originalChrRom"])

    def read_prg_rom_changes(self) -> List[Tuple[int, bytes, bytes]]:
        original: bytes = self.read_original_prg_rom()
        current: bytes = self.read_memory(MEMORY_TYPES["NesPrgRom"], 0, len(original))

        changes: List[Tuple[int, bytes, bytes]] = list()
        start: Optional[int] = None

        offset: int
        for offset in range(len(original) + 1):
            is_changed: bool = offset < len(original) and original[offset] != current[offset]

            if is_changed and start is None:
                start = offset
            elif not is_changed and start is not None:
                changes.append((start, original[start:offset], current[start:offset]))
                start = None

        return changes

    def read_cpu_memory_map(self) -> List[Optional[Tuple[int, int, int]]]:
        mapper_address: int = self._read_mapper_address()
        first_offset: int = BASE_MAPPER_MEMBER_OFFSETS["_prgMemoryAccess"]
        tables: bytes = self.process.read_bytes(mapper_address + first_offset, BASE_MAPPER_MEMBER_OFFSETS["_prgMemoryType"] + 0x400 - first_offset)
        internal_ram_mask: int = self.process.read_uint(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_internalRamMask"])

        accesses: Tuple[int, ...] = struct.unpack_from("<256i", tables, 0)
        offsets: Tuple[int, ...] = struct.unpack_from("<256i", tables, BASE_MAPPER_MEMBER_OFFSETS["_prgMemoryOffset"] - first_offset)
        types: Tuple[int, ...] = struct.unpack_from("<256i", tables, BASE_MAPPER_MEMBER_OFFSETS["_prgMemoryType"] - first_offset)

        pages: List[Optional[Tuple[int, int, int]]] = list()

        page: int
        for page in range(256):
            if page < 0x20:
                pages.append((MEMORY_TYPES["NesInternalRam"], (page << 8) & internal_ram_mask, 3))
            elif accesses[page] > 0 and types[page] in PRG_MEMORY_TYPE_TO_MEMORY_TYPE:
                pages.append((PRG_MEMORY_TYPE_TO_MEMORY_TYPE[types[page]], offsets[page], accesses[page]))
            else:
                pages.append(None)

        return pages

    def translate_cpu_address(self, address: int) -> Optional[Tuple[int, int]]:
        page: Optional[Tuple[int, int, int]] = self.read_cpu_memory_map()[address >> 8]

        if page is None:
            return None

        return page[0], page[1] + (address & 0xFF)

    def read_cpu_memory(self, address: int, length: int) -> bytes:
        pages: List[Optional[Tuple[int, int, int]]] = self.read_cpu_memory_map()
        data: bytes = bytes()

        while len(data) < length:
            current_address: int = (address + len(data)) & 0xFFFF
            page: Optional[Tuple[int, int, int]] = pages[current_address >> 8]

            if page is None:
                raise RuntimeError(f"CPU address {current_address:#06x} is not mapped to memory")

            chunk_length: int = min(0x100 - (current_address & 0xFF), length - len(data))
            data += self.read_memory(page[0], page[1] + (current_address & 0xFF), chunk_length)

        return data

    def write_cpu_memory(self, address: int, data: bytes) -> None:
        pages: List[Optional[Tuple[int, int, int]]] = self.read_cpu_memory_map()
        position: int = 0

        while position < len(data):
            current_address: int = (address + position) & 0xFFFF
            page: Optional[Tuple[int, int, int]] = pages[current_address >> 8]

            if page is None:
                raise RuntimeError(f"CPU address {current_address:#06x} is not mapped to memory")

            chunk_length: int = min(0x100 - (current_address & 0xFF), len(data) - position)
            self.write_memory(page[0], page[1] + (current_address & 0xFF), data[position:position + chunk_length])

            position += chunk_length

    def read_ppu_memory_map(self) -> List[Optional[Tuple[int, int, int]]]:
        mapper_address: int = self._read_mapper_address()

        accesses: Tuple[int, ...] = struct.unpack("<64i", self.process.read_bytes(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_chrMemoryAccess"], 0x100))
        offsets: Tuple[int, ...] = struct.unpack("<64i", self.process.read_bytes(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_chrMemoryOffset"], 0x100))
        types: Tuple[int, ...] = struct.unpack("<64i", self.process.read_bytes(mapper_address + BASE_MAPPER_MEMBER_OFFSETS["_chrMemoryType"], 0x100))

        pages: List[Optional[Tuple[int, int, int]]] = list()

        page: int
        for page in range(64):
            if page == 0x3F:
                pages.append((MEMORY_TYPES["NesPaletteRam"], 0, 3))
            elif accesses[page] > 0 and types[page] in CHR_MEMORY_TYPE_TO_MEMORY_TYPE:
                pages.append((CHR_MEMORY_TYPE_TO_MEMORY_TYPE[types[page]], offsets[page], accesses[page]))
            else:
                pages.append(None)

        return pages

    def translate_ppu_address(self, address: int) -> Optional[Tuple[int, int]]:
        return self._translate_ppu_address(self.read_ppu_memory_map(), address)

    def read_ppu_memory(self, address: int, length: int) -> bytes:
        pages: List[Optional[Tuple[int, int, int]]] = self.read_ppu_memory_map()
        data: bytes = bytes()

        while len(data) < length:
            current_address: int = (address + len(data)) & 0x3FFF
            target: Optional[Tuple[int, int]] = self._translate_ppu_address(pages, current_address)

            if target is None:
                raise RuntimeError(f"PPU address {current_address:#06x} is not mapped to memory")

            chunk_length: int = 1 if current_address >= 0x3F00 else min(0x100 - (current_address & 0xFF), length - len(data))
            data += self.read_memory(target[0], target[1], chunk_length)

        return data

    def write_ppu_memory(self, address: int, data: bytes) -> None:
        pages: List[Optional[Tuple[int, int, int]]] = self.read_ppu_memory_map()
        position: int = 0

        while position < len(data):
            current_address: int = (address + position) & 0x3FFF
            target: Optional[Tuple[int, int]] = self._translate_ppu_address(pages, current_address)

            if target is None:
                raise RuntimeError(f"PPU address {current_address:#06x} is not mapped to memory")

            chunk_length: int = 1 if current_address >= 0x3F00 else min(0x100 - (current_address & 0xFF), len(data) - position)
            self.write_memory(target[0], target[1], data[position:position + chunk_length])

            position += chunk_length

    def read_cpu_state(self) -> Dict[str, int]:
        cpu_address: int = self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_cpu"])
        cycle_count, program_counter, stack_pointer, a, x, y, status, irq_flag, nmi_flag = struct.unpack("<QH7B", self.process.read_bytes(cpu_address + NES_CPU_MEMBER_OFFSETS["_state"], 17))

        return {
            "A": a,
            "CycleCount": cycle_count,
            "IrqFlag": irq_flag,
            "NmiFlag": nmi_flag,
            "PC": program_counter,
            "PS": status,
            "SP": stack_pointer,
            "X": x,
            "Y": y,
        }

    def read_ppu_state(self) -> Dict[str, int]:
        ppu_address: int = self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_ppu"])
        ppu: bytes = self.process.read_bytes(ppu_address, BASE_NES_PPU_MEMBER_OFFSETS["_statusFlags"] + 3)

        background_pattern_address, sprite_pattern_address, vertical_write, large_sprites, secondary_ppu, nmi_on_vertical_blank = struct.unpack_from("<HH4B", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_control"])
        grayscale, background_mask, sprite_mask, background_enabled, sprites_enabled, intensify_red, intensify_green, intensify_blue = struct.unpack_from("<8B", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_mask"])
        sprite_overflow, sprite_zero_hit, vertical_blank = struct.unpack_from("<3B", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_statusFlags"])

        return {
            "BackgroundEnabled": background_enabled,
            "BackgroundMask": background_mask,
            "BackgroundPatternAddr": background_pattern_address,
            "Cycle": struct.unpack_from("<I", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_cycle"])[0],
            "FrameCount": struct.unpack_from("<I", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_frameCount"])[0],
            "Grayscale": grayscale,
            "IntensifyBlue": intensify_blue,
            "IntensifyGreen": intensify_green,
            "IntensifyRed": intensify_red,
            "LargeSprites": large_sprites,
            "MasterClock": struct.unpack_from("<Q", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_masterClock"])[0],
            "NmiOnVerticalBlank": nmi_on_vertical_blank,
            "Scanline": struct.unpack_from("<h", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_scanline"])[0],
            "ScrollX": ppu[BASE_NES_PPU_MEMBER_OFFSETS["_xScroll"]],
            "SecondaryPpu": secondary_ppu,
            "Sprite0Hit": sprite_zero_hit,
            "SpriteMask": sprite_mask,
            "SpriteOverflow": sprite_overflow,
            "SpritePatternAddr": sprite_pattern_address,
            "SpritesEnabled": sprites_enabled,
            "TmpVideoRamAddr": struct.unpack_from("<H", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_tmpVideoRamAddr"])[0],
            "VerticalBlank": vertical_blank,
            "VerticalWrite": vertical_write,
            "VideoRamAddr": struct.unpack_from("<H", ppu, BASE_NES_PPU_MEMBER_OFFSETS["_videoRamAddr"])[0],
            "WriteToggle": ppu[BASE_NES_PPU_MEMBER_OFFSETS["_writeToggle"]],
        }

    def read_frame_count(self) -> int:
        ppu_address: int = self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_ppu"])

        return self.process.read_uint(ppu_address + BASE_NES_PPU_MEMBER_OFFSETS["_frameCount"])

    def read_controllers(self) -> Dict[int, Tuple[int, bool, List[str]]]:
        control_manager_address: int = self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_controlManager"])
        begin, end = struct.unpack("<QQ", self.process.read_bytes(control_manager_address + NES_CONTROL_MANAGER_MEMBER_OFFSETS["_controlDevices"], 16))

        controllers: Dict[int, Tuple[int, bool, List[str]]] = dict()

        device_pointer: int
        for device_pointer in range(begin, end, 16):
            device_address: int = self._read_pointer(device_pointer)
            port: int = self.process.read_uchar(device_address + BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_port"])
            controller_type: int = self.process.read_int(device_address + BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_type"])
            is_connected: bool = bool(self.process.read_uchar(device_address + BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_connected"]))
            state: bytes = self._read_byte_vector(device_address + BASE_CONTROL_DEVICE_MEMBER_OFFSETS["_state"])

            buttons: List[str] = [name for name in sorted(NES_CONTROLLER_BUTTONS) if NES_CONTROLLER_BUTTONS[name] >> 3 < len(state) and state[NES_CONTROLLER_BUTTONS[name] >> 3] >> (NES_CONTROLLER_BUTTONS[name] & 7) & 1]

            controllers[port] = (controller_type, is_connected, buttons)

        return controllers

    def read_input_counters(self) -> Tuple[int, int]:
        control_manager_address: int = self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_controlManager"])
        poll_counter, lag_counter = struct.unpack("<II", self.process.read_bytes(control_manager_address + NES_CONTROL_MANAGER_MEMBER_OFFSETS["_pollCounter"], 8))

        return poll_counter, lag_counter

    def install_hooks(self) -> None:
        registered_cave_address: Optional[int] = self._find_registered_cave()

        input_slot_address: int = self.module_base + MESEN_VIRTUAL_TABLE_RVAS["NesController"] + MESEN_VIRTUAL_TABLE_OFFSETS["BaseControlDevice::InternalSetStateFromInput"]
        original_input_function: int = self.module_base + MESEN_FUNCTION_RVAS["NesController::InternalSetStateFromInput"]

        if registered_cave_address is not None:
            self.cave_address = registered_cave_address
            expected_callback_code: bytes = build_callback_code(registered_cave_address)
            expected_input_hook_code: bytes = build_input_hook_code(registered_cave_address)

            is_current: bool = self.process.read_bytes(registered_cave_address + CALLBACK_CODE_OFFSET, len(expected_callback_code)) == expected_callback_code
            is_current = is_current and self.process.read_bytes(registered_cave_address + INPUT_HOOK_CODE_OFFSET, len(expected_input_hook_code)) == expected_input_hook_code

            if is_current:
                if self._read_pointer(input_slot_address) == original_input_function:
                    self._write_protected_pointer(input_slot_address, registered_cave_address + INPUT_HOOK_CODE_OFFSET)

                return

            self.uninstall_hooks()

        if self._read_pointer(input_slot_address) != original_input_function:
            raise RuntimeError("NesController input is already hooked by something else; restart Mesen")

        self.cave_address = self.process.allocate(CAVE_SIZE)

        self._write_cave(CALLBACK_CODE_OFFSET, build_callback_code(self.cave_address))
        self._write_cave(INPUT_HOOK_CODE_OFFSET, build_input_hook_code(self.cave_address))
        self._write_cave(CALLBACK_DATA_OFFSET, struct.pack(
            "<QQQQQIIIIIIIIQQ",
            CALLBACK_MAGIC,
            self.module_base + MESEN_GLOBAL_RVAS["_emu"],
            0,
            0,
            0,
            0,
            sum(1 << CONSOLE_NOTIFICATION_TYPES[name] for name in ("BeforeGameUnload", "EmulationStopped", "ExecuteShortcut", "GameLoadFailed", "GameLoaded", "GamePaused", "GameReset", "GameResumed", "StateLoaded")),
            WRITE_STATE_IDLE,
            0,
            0,
            0,
            0,
            0,
            0,
            original_input_function,
        ))

        listener_address: int = self.call_export("RegisterNotificationCallback", self.cave_address + CALLBACK_CODE_OFFSET)

        self.process.write_ulonglong(self.cave_address + CALLBACK_DATA_OFFSET + 0x10, listener_address)
        self._write_protected_pointer(input_slot_address, self.cave_address + INPUT_HOOK_CODE_OFFSET)

    def is_hooked(self) -> bool:
        if self.cave_address is None:
            return False

        input_slot_address: int = self.module_base + MESEN_VIRTUAL_TABLE_RVAS["NesController"] + MESEN_VIRTUAL_TABLE_OFFSETS["BaseControlDevice::InternalSetStateFromInput"]

        try:
            return self._find_registered_cave() == self.cave_address and self._read_pointer(input_slot_address) == self.cave_address + INPUT_HOOK_CODE_OFFSET
        except Exception:
            return False

    def uninstall_hooks(self) -> None:
        cave_address: int = self._require_cave()
        input_slot_address: int = self.module_base + MESEN_VIRTUAL_TABLE_RVAS["NesController"] + MESEN_VIRTUAL_TABLE_OFFSETS["BaseControlDevice::InternalSetStateFromInput"]

        if self._read_pointer(input_slot_address) == cave_address + INPUT_HOOK_CODE_OFFSET:
            self._write_protected_pointer(input_slot_address, self.module_base + MESEN_FUNCTION_RVAS["NesController::InternalSetStateFromInput"])

        self.call_export("UnregisterNotificationCallback", self.process.read_ulonglong(cave_address + CALLBACK_DATA_OFFSET + 0x10))

        self.cave_address = None

    def read_callback_frame_count(self) -> int:
        return self.process.read_ulonglong(self._require_cave() + CALLBACK_DATA_OFFSET + 0x18)

    def set_event_mask(self, notification_types: Sequence[int]) -> None:
        self.process.write_uint(self._require_cave() + CALLBACK_DATA_OFFSET + 0x2C, sum(1 << notification_type for notification_type in set(notification_types)))

    def read_new_events(self) -> List[Tuple[int, int, int]]:
        cave_address: int = self._require_cave()
        count: int = self.process.read_uint(cave_address + CALLBACK_DATA_OFFSET + 0x28)

        if self.event_cursor is None or self.event_cursor > count:
            self.event_cursor = count

        first: int = max(self.event_cursor, count - EVENT_LOG_CAPACITY)
        log: bytes = self.process.read_bytes(cave_address + EVENT_LOG_OFFSET, EVENT_LOG_CAPACITY * 16)

        events: List[Tuple[int, int, int]] = list()

        index: int
        for index in range(first, count):
            sequence, notification_type, parameter, frame_count = struct.unpack_from("<IHHQ", log, (index % EVENT_LOG_CAPACITY) * 16)

            if sequence != index + 1:
                break

            events.append((notification_type, parameter, frame_count))

        self.event_cursor = first + len(events)

        return events

    def queue_memory_writes(self, writes: Sequence[Tuple[int, int, bytes]]) -> None:
        cave_address: int = self._require_cave()

        if self.is_memory_write_pending():
            raise RuntimeError("The previous memory writes have not been applied yet")

        if len(writes) > WRITE_RECORD_CAPACITY:
            raise RuntimeError(f"Too many memory writes queued at once ({len(writes)})")

        records: bytes = bytes()
        data: bytes = bytes()

        memory_type: int
        offset: int
        write_data: bytes
        for memory_type, offset, write_data in writes:
            records += struct.pack("<4I", memory_type, offset, len(write_data), WRITE_DATA_OFFSET - CALLBACK_DATA_OFFSET + len(data))
            data += write_data

        if len(data) > WRITE_DATA_SIZE:
            raise RuntimeError(f"Too much memory write data queued at once ({len(data)} bytes)")

        self._write_cave(WRITE_DATA_OFFSET, data)
        self._write_cave(WRITE_RECORDS_OFFSET, records)
        self._write_cave(CALLBACK_DATA_OFFSET + 0x34, struct.pack("<II", len(writes), 0))
        self.process.write_uint(cave_address + CALLBACK_DATA_OFFSET + 0x30, WRITE_STATE_PENDING)

    def is_memory_write_pending(self) -> bool:
        return self.process.read_uint(self._require_cave() + CALLBACK_DATA_OFFSET + 0x30) == WRITE_STATE_PENDING

    def read_memory_write_failures(self) -> int:
        return self.process.read_uint(self._require_cave() + CALLBACK_DATA_OFFSET + 0x38)

    def wait_for_memory_writes(self, timeout_seconds: float = 1.0) -> bool:
        deadline: float = time.perf_counter() + timeout_seconds

        while self.is_memory_write_pending():
            if time.perf_counter() > deadline:
                return False

            time.sleep(0.005)

        return True

    def cancel_memory_writes(self) -> None:
        self.process.write_uint(self._require_cave() + CALLBACK_DATA_OFFSET + 0x30, WRITE_STATE_IDLE)

    def set_watched_memory(self, watches: Sequence[Tuple[int, int, int]]) -> None:
        cave_address: int = self._require_cave()

        if len(watches) > WATCH_CAPACITY:
            raise RuntimeError(f"At most {WATCH_CAPACITY} memory ranges can be watched")

        if sum(length for _, _, length in watches) > SNAPSHOT_SIZE:
            raise RuntimeError(f"At most {SNAPSHOT_SIZE:#x} bytes can be watched")

        entries: bytes = bytes()
        snapshot_offset: int = SNAPSHOT_OFFSET - CALLBACK_DATA_OFFSET

        memory_type: int
        offset: int
        length: int
        for memory_type, offset, length in watches:
            entries += struct.pack("<4I", memory_type, offset, length, snapshot_offset)
            snapshot_offset += length

        self.process.write_uint(cave_address + CALLBACK_DATA_OFFSET + 0x3C, 0)
        self._write_cave(WATCH_TABLE_OFFSET, entries)
        self.process.write_uint(cave_address + CALLBACK_DATA_OFFSET + 0x3C, len(watches))

    def read_watched_memory(self) -> Optional[Tuple[int, List[bytes]]]:
        cave_address: int = self._require_cave()
        watch_count: int = self.process.read_uint(cave_address + CALLBACK_DATA_OFFSET + 0x3C)
        watches: bytes = self.process.read_bytes(cave_address + WATCH_TABLE_OFFSET, watch_count * 16)
        total_length: int = sum(struct.unpack_from("<4I", watches, index * 16)[2] for index in range(watch_count))

        attempt: int
        for attempt in range(8):
            sequence: int = self.process.read_uint(cave_address + CALLBACK_DATA_OFFSET + 0x40)

            if sequence == 0 or sequence & 1:
                time.sleep(0.001)
                continue

            frame_count: int = self.process.read_ulonglong(cave_address + CALLBACK_DATA_OFFSET + 0x48)
            snapshot: bytes = self.process.read_bytes(cave_address + SNAPSHOT_OFFSET, total_length)

            if self.process.read_uint(cave_address + CALLBACK_DATA_OFFSET + 0x40) != sequence:
                continue

            ranges: List[bytes] = list()
            position: int = 0

            index: int
            for index in range(watch_count):
                length: int = struct.unpack_from("<4I", watches, index * 16)[2]
                ranges.append(snapshot[position:position + length])
                position += length

            return frame_count, ranges

        return None

    def set_controller_input(self, port: int, pressed_buttons: Sequence[str] = (), released_buttons: Sequence[str] = (), swapped_buttons: Sequence[Tuple[str, str]] = (), frame_count: Optional[int] = None) -> None:
        cave_address: int = self._require_cave()

        if not 0 <= port < INPUT_OVERRIDE_CAPACITY:
            raise RuntimeError(f"Controller input can only be set for ports 0 to {INPUT_OVERRIDE_CAPACITY - 1}")

        if frame_count is not None and not 0 < frame_count < 0xFFFFFFFF:
            raise RuntimeError(f"Invalid frame count ({frame_count})")

        table: bytes = bytes()

        buttons: int
        for buttons in range(256):
            mapped_buttons: int = buttons

            first_button: str
            second_button: str
            for first_button, second_button in swapped_buttons:
                first_bit: int = 1 << NES_CONTROLLER_BUTTONS[first_button]
                second_bit: int = 1 << NES_CONTROLLER_BUTTONS[second_button]

                mapped_buttons &= ~(first_bit | second_bit)

                if buttons & first_bit:
                    mapped_buttons |= second_bit

                if buttons & second_bit:
                    mapped_buttons |= first_bit

            button: str
            for button in released_buttons:
                mapped_buttons &= ~(1 << NES_CONTROLLER_BUTTONS[button])

            for button in pressed_buttons:
                mapped_buttons |= 1 << NES_CONTROLLER_BUTTONS[button]

            table += bytes([mapped_buttons])

        override_address: int = cave_address + INPUT_OVERRIDES_OFFSET + port * INPUT_OVERRIDE_SIZE

        self.process.write_uint(override_address, 0)
        self.process.write_bytes(override_address + 0x10, table, len(table))
        self.process.write_uint(override_address, 0xFFFFFFFF if frame_count is None else frame_count)

    def clear_controller_input(self, port: int) -> None:
        self.process.write_uint(self._require_cave() + INPUT_OVERRIDES_OFFSET + port * INPUT_OVERRIDE_SIZE, 0)

    def read_controller_input_frames_remaining(self, port: int) -> Optional[int]:
        frames_remaining: int = self.process.read_uint(self._require_cave() + INPUT_OVERRIDES_OFFSET + port * INPUT_OVERRIDE_SIZE)

        return None if frames_remaining == 0xFFFFFFFF else frames_remaining

    def call_function(self, function_address: int, *arguments: int) -> int:
        cave_address: int = self._require_cave()
        code: bytes = build_remote_call_code(function_address, arguments, cave_address + REMOTE_CALL_RESULT_OFFSET)

        self._wait_for_remote_call()
        self._write_cave(REMOTE_CALL_CODE_OFFSET, code)

        thread: Optional[int] = ctypes.windll.kernel32.CreateRemoteThread(self.process.process_handle, None, 0, cave_address + REMOTE_CALL_CODE_OFFSET, None, 0, None)

        if not thread:
            raise RuntimeError(f"CreateRemoteThread failed for {function_address:#x}")

        wait_result: int = ctypes.windll.kernel32.WaitForSingleObject(thread, int(self.remote_call_timeout_seconds * 1000))

        if wait_result != 0:
            self.remote_call_thread = thread

            raise RuntimeError(f"{function_address:#x} did not return in time ({wait_result:#x})")

        ctypes.windll.kernel32.CloseHandle(thread)

        return self.process.read_ulonglong(cave_address + REMOTE_CALL_RESULT_OFFSET)

    def call_export(self, name: str, *arguments: int) -> int:
        return self.call_function(self.module_base + MESEN_EXPORT_RVAS[name], *arguments)

    def display_message(self, title: str, message: str) -> None:
        cave_address: int = self._require_cave()
        title_bytes: bytes = title.encode("utf-8") + b"\x00"
        message_bytes: bytes = message.encode("utf-8") + b"\x00"

        if len(title_bytes) + len(message_bytes) > ARGUMENT_BUFFER_SIZE:
            raise RuntimeError(f"Message is too long ({len(title_bytes) + len(message_bytes)} bytes)")

        self._wait_for_remote_call()
        self._write_cave(ARGUMENT_BUFFER_OFFSET, title_bytes + message_bytes)
        self.call_export("DisplayMessage", cave_address + ARGUMENT_BUFFER_OFFSET, cave_address + ARGUMENT_BUFFER_OFFSET + len(title_bytes), 0)

    def write_log_entry(self, message: str) -> None:
        self.call_export("WriteLogEntry", self._write_argument_string(message))

    def pause(self) -> None:
        self.call_export("Pause")

    def resume(self) -> None:
        self.call_export("Resume")

    def execute_shortcut(self, shortcut: int, parameter: int = 0) -> None:
        cave_address: int = self._require_cave()

        self._wait_for_remote_call()
        self._write_cave(ARGUMENT_BUFFER_OFFSET, struct.pack("<IIQ", shortcut, parameter, 0))
        self.call_export("ExecuteShortcut", cave_address + ARGUMENT_BUFFER_OFFSET)

    def release_shortcut(self, shortcut: int, parameter: int = 0) -> None:
        cave_address: int = self._require_cave()
        notification_manager_address: int = self._read_pointer(self.read_emulator_address() + EMULATOR_MEMBER_OFFSETS["_notificationManager"])

        self._wait_for_remote_call()
        self._write_cave(ARGUMENT_BUFFER_OFFSET, struct.pack("<IIQ", shortcut, parameter, 0))
        self.call_function(self.module_base + MESEN_FUNCTION_RVAS["NotificationManager::SendNotification"], notification_manager_address, CONSOLE_NOTIFICATION_TYPES["ReleaseShortcut"], cave_address + ARGUMENT_BUFFER_OFFSET)

    def run_single_frame(self) -> None:
        self.execute_shortcut(EMULATOR_SHORTCUTS["RunSingleFrame"])
        self.release_shortcut(EMULATOR_SHORTCUTS["RunSingleFrame"])

    def set_emulation_flag(self, flag: int, is_enabled: bool) -> None:
        self.call_export("SetEmulationFlag", flag, int(is_enabled))

    def reset(self) -> None:
        self.execute_shortcut(EMULATOR_SHORTCUTS["ExecReset"])

    def power_cycle(self) -> None:
        self.execute_shortcut(EMULATOR_SHORTCUTS["ExecPowerCycle"])

    def reload_rom(self) -> None:
        self.execute_shortcut(EMULATOR_SHORTCUTS["ExecReloadRom"])

    def power_off(self) -> None:
        self.execute_shortcut(EMULATOR_SHORTCUTS["ExecPowerOff"])

    def take_screenshot(self) -> None:
        self.call_export("TakeScreenshot")

    def reset_lag_counter(self) -> None:
        self.call_export("ResetLagCounter")

    def save_state(self, slot: int) -> None:
        self.call_export("SaveState", slot)

    def load_state(self, slot: int) -> None:
        self.call_export("LoadState", slot)

    def save_state_to_file(self, path: str) -> None:
        self.call_export("SaveStateFile", self._write_argument_string(path))

    def load_state_from_file(self, path: str) -> None:
        self.call_export("LoadStateFile", self._write_argument_string(path))

    def set_cheats(self, cheats: Sequence[Tuple[int, str]]) -> None:
        cave_address: int = self._require_cave()
        records: bytes = bytes()

        cheat_type: int
        code: str
        for cheat_type, code in cheats:
            encoded_code: bytes = code.encode("ascii")

            if len(encoded_code) > 15:
                raise RuntimeError(f"Cheat code {code} is too long")

            records += struct.pack("<B16s", cheat_type, encoded_code)

        if len(records) > ARGUMENT_BUFFER_SIZE:
            raise RuntimeError(f"Too many cheats at once ({len(cheats)})")

        self._wait_for_remote_call()
        self._write_cave(ARGUMENT_BUFFER_OFFSET, records)
        self.call_export("SetCheats", cave_address + ARGUMENT_BUFFER_OFFSET, len(cheats))

    def clear_cheats(self) -> None:
        self.call_export("ClearCheats")

    def _read_mapper_address(self) -> int:
        return self._read_pointer(self.read_console_address() + NES_CONSOLE_MEMBER_OFFSETS["_mapper"])

    def _translate_ppu_address(self, pages: List[Optional[Tuple[int, int, int]]], address: int) -> Optional[Tuple[int, int]]:
        address &= 0x3FFF

        if address >= 0x3F00:
            palette_address: int = address & 0x1F

            if palette_address & 0x13 == 0x10:
                palette_address &= 0x0F

            return MEMORY_TYPES["NesPaletteRam"], palette_address

        page: Optional[Tuple[int, int, int]] = pages[address >> 8]

        if page is None:
            return None

        return page[0], page[1] + (address & 0xFF)

    def _find_registered_cave(self) -> Optional[int]:
        listeners_address: int = self.module_base + MESEN_GLOBAL_RVAS["_listeners"] + INTEROP_NOTIFICATION_LISTENERS_MEMBER_OFFSETS["_externalNotificationListeners"]
        begin, end = struct.unpack("<QQ", self.process.read_bytes(listeners_address, 16))

        listener_pointer: int
        for listener_pointer in range(begin, end, 16):
            try:
                callback_address: int = self._read_pointer(self._read_pointer(listener_pointer) + INTEROP_NOTIFICATION_LISTENER_MEMBER_OFFSETS["_callback"])
                magic: int = self.process.read_ulonglong(callback_address - CALLBACK_CODE_OFFSET + CALLBACK_DATA_OFFSET)
            except Exception:
                continue

            if magic == CALLBACK_MAGIC:
                return callback_address - CALLBACK_CODE_OFFSET

        return None

    def _write_argument_string(self, text: str) -> int:
        encoded: bytes = text.encode("utf-8") + b"\x00"

        if len(encoded) > ARGUMENT_BUFFER_SIZE:
            raise RuntimeError(f"Argument is too long ({len(encoded)} bytes)")

        self._wait_for_remote_call()
        self._write_cave(ARGUMENT_BUFFER_OFFSET, encoded)

        return self._require_cave() + ARGUMENT_BUFFER_OFFSET

    def _read_std_string(self, address: int) -> str:
        buffer, size, capacity = struct.unpack("<16sQQ", self.process.read_bytes(address, 32))

        if capacity >= 16:
            return self.process.read_bytes(struct.unpack_from("<Q", buffer)[0], size).decode("utf-8", errors="replace")

        return buffer[:size].decode("utf-8", errors="replace")

    def _read_byte_vector(self, address: int) -> bytes:
        begin, end = struct.unpack("<QQ", self.process.read_bytes(address, 16))

        if end <= begin:
            return bytes()

        return self.process.read_bytes(begin, end - begin)

    def _wait_for_remote_call(self) -> None:
        if self.remote_call_thread is None:
            return

        if ctypes.windll.kernel32.WaitForSingleObject(self.remote_call_thread, int(self.remote_call_timeout_seconds * 1000)) != 0:
            raise RuntimeError("The previous remote call is still running")

        ctypes.windll.kernel32.CloseHandle(self.remote_call_thread)
        self.remote_call_thread = None

    def _require_cave(self) -> int:
        if self.cave_address is None:
            raise RuntimeError("Hooks are not installed")

        return self.cave_address

    def _write_cave(self, offset: int, data: bytes) -> None:
        self.process.write_bytes(self._require_cave() + offset, data, len(data))

    def _write_protected_pointer(self, address: int, value: int) -> None:
        previous_protection: ctypes.c_ulong = ctypes.c_ulong(0)

        if not pymem.ressources.kernel32.VirtualProtectEx(self.process.process_handle, ctypes.c_void_p(address), 8, 0x40, ctypes.byref(previous_protection)):
            raise RuntimeError(f"Could not make {address:#x} writable")

        self.process.write_ulonglong(address, value)

        pymem.ressources.kernel32.VirtualProtectEx(self.process.process_handle, ctypes.c_void_p(address), 8, previous_protection.value, ctypes.byref(previous_protection))

    def _read_pointer(self, address: int) -> int:
        return self.process.read_ulonglong(address)
