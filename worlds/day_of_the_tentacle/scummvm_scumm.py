from typing import Dict, Iterator, List, Optional, Sequence, Tuple

import ctypes
import os
import struct
import time

import pymem.process
import pymem.ressources.kernel32
import pymem.ressources.structure

from pymem import Pymem


# ScummVM 2026.3.0 (win64). Found with string cross-references, .pdata function bounds and capstone.
SCUMMVM_FUNCTION_RVAS: Dict[str, int] = {
    "ScummEngine::addObjectToInventory": 0x227CE0,
    "ScummEngine::clearDrawObjectQueue": 0x225F70,
    "ScummEngine::clearOwnerOf": 0x224F80,
    "ScummEngine::markObjectRectAsDirty": 0x226000,
    "ScummEngine::push": 0x2887D0,
    "ScummEngine::putClass": 0x224B70,
    "ScummEngine::putOwner": 0x224CB0,
    "ScummEngine::putState": 0x224DA0,
}

SCUMMVM_VIRTUAL_TABLE_OFFSETS: Dict[str, int] = {
    "ScummEngine::actorTalk": 0x3A8,
    "ScummEngine::drawVerb": 0x378,
    "ScummEngine::runInputScript": 0x380,
    "ScummEngine::runInventoryScript": 0x260,
}

SCUMM_ENGINE_MEMBER_OFFSETS: Dict[str, int] = {
    "_actorToPrintStrFor": 0x85EE,
    "_actors": 0x3BE0,
    "_bitVars": 0x3CB0,
    "_classData": 0x85E0,
    "_currentScript": 0x704A,
    "_game": 0xD8,
    "_inventory": 0x3BF8,
    "_numBitVariables": 0x3CBC,
    "_numGlobalObjects": 0x3CC4,
    "_numInventory": 0x3CD4,
    "_numVariables": 0x3CB8,
    "_numVerbs": 0x3CCC,
    "_objectOwnerTable": 0x85C0,
    "_objectStateTable": 0x85D0,
    "_opcodes": 0x74B8,
    "_saveLoadDescription": 0x6008,
    "_saveLoadFlag": 0x5FD0,
    "_saveLoadSlot": 0x5FD1,
    "_saveTemporaryState": 0x5FD8,
    "_scriptPointer": 0x7030,
    "_scummStackPos": 0x704C,
    "_scummVars": 0x3CA8,
    "_string[0]": 0x8624,
    "_string[0]._default": 0x8632,
    "_verbs": 0xC8,
    "_vmStack": 0x7050,
    "vm.slot": 0x170,
}

CALL_QUEUE_CODE_OFFSET: int = 0x000
PICKUP_FILTER_CODE_OFFSET: int = 0x400
OWNER_FILTER_CODE_OFFSET: int = 0x600
TALK_ACTOR_LOGGER_CODE_OFFSET: int = 0x700
TALK_EGO_LOGGER_CODE_OFFSET: int = 0x780
MAILBOX_OFFSET: int = 0x800
SENTENCE_LOGGER_CODE_OFFSET: int = 0xB40
PICKUP_DATA_OFFSET: int = 0xC00
TALK_DATA_OFFSET: int = 0xC40
TALK_LOG_OFFSET: int = 0xD00
SENTENCE_LOG_OFFSET: int = 0xF20
PICKUP_TABLE_OFFSET: int = 0x1000
MESSAGE_BUFFER_OFFSET: int = 0x3000
INPUT_BLOCKER_CODE_OFFSET: int = 0x4000
INPUT_DATA_OFFSET: int = 0x4100
SCRIPT_BLOCKER_CODE_OFFSET: int = 0x4200
SCRIPT_DATA_OFFSET: int = 0x4300
SCRIPT_LOG_OFFSET: int = 0x4380
SENTENCE_DATA_OFFSET: int = 0x4400
SCRIPT_BYTES_CALLER_CODE_OFFSET: int = 0x4500
SCRIPT_BYTES_OFFSET: int = 0x4580
QUICK_SCRIPT_BLOCKER_CODE_OFFSET: int = 0x4600
SECOND_QUICK_SCRIPT_BLOCKER_CODE_OFFSET: int = 0x4680
PICKUP_ROOM_TABLE_OFFSET: int = 0x5000

PICKUP_TABLE_SIZE: int = 0x2000
TALK_LOG_CAPACITY: int = 128
SENTENCE_LOG_CAPACITY: int = 32
SENTENCE_BLOCKED_CAPACITY: int = 24
SENTENCE_OBJECT_BITS: int = 12
SCRIPT_LOG_CAPACITY: int = 32
SCRIPT_BLOCKED_CAPACITY: int = 8
INPUT_BLOCKED_CAPACITY: int = 8

MAILBOX_MAGIC: int = 0x4D4D55435350410C
MAILBOX_STATE_IDLE: int = 0
MAILBOX_STATE_PENDING: int = 1
MAILBOX_STATE_DONE: int = 2
MAILBOX_STATE_RUNNING: int = 3

PICKUP_IGNORED: int = 0
PICKUP_INTERCEPTED: int = 1
PICKUP_CHECKED: int = 2

OBJECT_CLASS_UNTOUCHABLE: int = 32

HOOKS: List[Tuple[str, int, int]] = [
    ("o6_breakHere", CALL_QUEUE_CODE_OFFSET, MAILBOX_OFFSET + 0x08),
    ("o6_pickupObject", PICKUP_FILTER_CODE_OFFSET, PICKUP_DATA_OFFSET + 0x00),
    ("o6_getOwner", OWNER_FILTER_CODE_OFFSET, PICKUP_DATA_OFFSET + 0x28),
    ("o6_talkActor", TALK_ACTOR_LOGGER_CODE_OFFSET, TALK_DATA_OFFSET + 0x00),
    ("o6_talkEgo", TALK_EGO_LOGGER_CODE_OFFSET, TALK_DATA_OFFSET + 0x08),
    ("o6_doSentence", SENTENCE_LOGGER_CODE_OFFSET, SENTENCE_DATA_OFFSET + 0x00),
    ("o6_startScript", SCRIPT_BLOCKER_CODE_OFFSET, SCRIPT_DATA_OFFSET + 0x00),
    ("o6_startScriptQuick", QUICK_SCRIPT_BLOCKER_CODE_OFFSET, SCRIPT_DATA_OFFSET + 0x30),
    ("o6_startScriptQuick2", SECOND_QUICK_SCRIPT_BLOCKER_CODE_OFFSET, SCRIPT_DATA_OFFSET + 0x38),
]


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


def build_call_queue_code(cave_address: int) -> bytes:
    return assemble([
        b"\x41\x54",  # push r12
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x57",  # push rdi
        b"\x48\x83\xEC\x28",  # sub rsp, 0x28
        b"\x48\x89\xCB",  # mov rbx, rcx  ; engine
        b"\x48\xBE" + struct.pack("<Q", cave_address + MAILBOX_OFFSET),  # mov rsi, mailbox
        b"\x83\x3E" + struct.pack("<b", MAILBOX_STATE_PENDING),  # cmp dword [rsi], pending
        ("jump", b"\x75", "done"),  # jne done

        b"\xC7\x06" + struct.pack("<i", MAILBOX_STATE_RUNNING),  # mov dword [rsi], running
        b"\x44\x8B\x66\x04",  # mov r12d, [rsi + 0x04]  ; call count
        b"\x48\x8D\x7E\x20",  # lea rdi, [rsi + 0x20]  ; first call record

        ("label", "next_call"),
        b"\x45\x85\xE4",  # test r12d, r12d
        ("jump", b"\x74", "finished"),  # je finished
        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x48\x8B\x57\x08",  # mov rdx, [rdi + 0x08]  ; argument 1
        b"\x4C\x8B\x47\x10",  # mov r8, [rdi + 0x10]  ; argument 2
        b"\x4C\x8B\x4F\x18",  # mov r9, [rdi + 0x18]  ; argument 3
        b"\xFF\x17",  # call [rdi]  ; function
        b"\x48\x89\x47\x20",  # mov [rdi + 0x20], rax  ; result
        b"\x48\x83\xC7\x30",  # add rdi, 0x30  ; next call record
        b"\x41\xFF\xCC",  # dec r12d
        ("jump", b"\xEB", "next_call"),  # jmp next_call

        ("label", "finished"),
        b"\xC7\x06" + struct.pack("<i", MAILBOX_STATE_DONE),  # mov dword [rsi], done

        ("label", "done"),
        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x48\x8B\x46\x08",  # mov rax, [rsi + 0x08]  ; original breakHere
        b"\x48\x83\xC4\x28",  # add rsp, 0x28
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\x41\x5C",  # pop r12
        b"\xFF\xE0",  # jmp rax
    ])


def build_pickup_filter_code(cave_address: int) -> bytes:
    stack_position: int = SCUMM_ENGINE_MEMBER_OFFSETS["_scummStackPos"]
    first_argument: int = SCUMM_ENGINE_MEMBER_OFFSETS["_vmStack"] - 8

    return assemble([
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x57",  # push rdi
        b"\x48\x83\xEC\x20",  # sub rsp, 0x20
        b"\x48\x89\xCB",  # mov rbx, rcx  ; engine
        b"\x48\xBE" + struct.pack("<Q", cave_address + PICKUP_DATA_OFFSET),  # mov rsi, pickup data

        b"\x8B\x83" + struct.pack("<i", stack_position),  # mov eax, [rbx + stack position]
        b"\x83\xF8\x02",  # cmp eax, 2  ; object and room
        ("jump", b"\x7C", "pass_through"),  # jl pass_through

        b"\x8B\xBC\x83" + struct.pack("<i", first_argument),  # mov edi, [rbx + rax*4 + first argument]  ; object id
        b"\x81\xFF" + struct.pack("<i", PICKUP_TABLE_SIZE),  # cmp edi, table size
        ("jump", b"\x73", "pass_through"),  # jae pass_through

        b"\x48\xBA" + struct.pack("<Q", cave_address + PICKUP_TABLE_OFFSET),  # mov rdx, pickup table
        b"\x80\x3C\x3A" + struct.pack("<b", PICKUP_IGNORED),  # cmp byte [rdx + rdi], ignored
        ("jump", b"\x74", "pass_through"),  # je pass_through

        b"\xC6\x04\x3A" + struct.pack("<b", PICKUP_CHECKED),  # mov byte [rdx + rdi], checked
        b"\x83\xE8\x02",  # sub eax, 2
        b"\x89\x83" + struct.pack("<i", stack_position),  # mov [rbx + stack position], eax  ; pop the arguments

        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x89\xFA",  # mov edx, edi  ; object id
        b"\x41\xB8" + struct.pack("<i", OBJECT_CLASS_UNTOUCHABLE),  # mov r8d, untouchable
        b"\x41\xB9\x01\x00\x00\x00",  # mov r9d, 1
        b"\xFF\x56\x08",  # call [rsi + 0x08]  ; putClass

        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x89\xFA",  # mov edx, edi  ; object id
        b"\x41\xB8\x01\x00\x00\x00",  # mov r8d, 1  ; picked up state
        b"\xFF\x56\x10",  # call [rsi + 0x10]  ; putState

        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x89\xFA",  # mov edx, edi  ; object id
        b"\xFF\x56\x18",  # call [rsi + 0x18]  ; markObjectRectAsDirty

        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\xFF\x56\x20",  # call [rsi + 0x20]  ; clearDrawObjectQueue

        b"\x48\x83\xC4\x20",  # add rsp, 0x20
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xC3",  # ret

        ("label", "pass_through"),
        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x48\x8B\x06",  # mov rax, [rsi]  ; original pickupObject
        b"\x48\x83\xC4\x20",  # add rsp, 0x20
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xFF\xE0",  # jmp rax
    ])


def build_owner_filter_code(cave_address: int) -> bytes:
    stack_position: int = SCUMM_ENGINE_MEMBER_OFFSETS["_scummStackPos"]
    stack_top: bytes = struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["_vmStack"] - 4)

    return assemble([
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x57",  # push rdi
        b"\x48\x83\xEC\x20",  # sub rsp, 0x20
        b"\x48\x89\xCB",  # mov rbx, rcx  ; engine
        b"\x48\xBE" + struct.pack("<Q", cave_address + PICKUP_DATA_OFFSET),  # mov rsi, pickup data

        b"\x8B\x83" + struct.pack("<i", stack_position),  # mov eax, [rbx + stack position]
        b"\x83\xF8\x01",  # cmp eax, 1
        ("near_jump", b"\x0F\x8C", "pass_through"),  # jl pass_through

        b"\x8B\xBC\x83" + stack_top,  # mov edi, [rbx + rax*4 + top]  ; object id
        b"\x81\xFF" + struct.pack("<i", PICKUP_TABLE_SIZE),  # cmp edi, table size
        ("near_jump", b"\x0F\x83", "pass_through"),  # jae pass_through

        b"\x48\xBA" + struct.pack("<Q", cave_address + PICKUP_TABLE_OFFSET),  # mov rdx, pickup table
        b"\x0F\xB6\x0C\x3A",  # movzx ecx, byte [rdx + rdi]
        b"\x85\xC9",  # test ecx, ecx  ; ignored?
        ("near_jump", b"\x0F\x84", "pass_through"),  # je pass_through

        b"\x4C\x8B\x83" + struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["_scriptPointer"]),  # mov r8, [rbx + script pointer]
        b"\x45\x8B\x08",  # mov r9d, [r8]  ; next script bytes
        b"\x41\x81\xE1\xFF\xFF\xFF\x00",  # and r9d, 0xFFFFFF
        b"\x41\x81\xF9\x01\x0F\x00\x00",  # cmp r9d, 0x000F01  ; pushWord 15
        ("near_jump", b"\x0F\x85", "pass_through"),  # jne pass_through

        b"\x83\xF9" + struct.pack("<b", PICKUP_INTERCEPTED),  # cmp ecx, intercepted
        ("jump", b"\x74", "intercepted"),  # je intercepted

        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\xFF\x56\x28",  # call [rsi + 0x28]  ; original getOwner
        b"\x8B\x83" + struct.pack("<i", stack_position),  # mov eax, [rbx + stack position]
        b"\x83\xBC\x83" + stack_top + b"\x0F",  # cmp dword [rbx + rax*4 + top], 15
        ("jump", b"\x75", "done"),  # jne done
        b"\xC7\x84\x83" + stack_top + struct.pack("<i", 0),  # mov dword [rbx + rax*4 + top], 0
        ("jump", b"\xEB", "done"),  # jmp done

        ("label", "intercepted"),
        b"\x49\xBA" + struct.pack("<Q", cave_address + PICKUP_ROOM_TABLE_OFFSET),  # mov r10, pickup room table
        b"\x45\x0F\xB6\x0C\x3A",  # movzx r9d, byte [r10 + rdi]  ; the object's room
        b"\x45\x85\xC9",  # test r9d, r9d
        ("jump", b"\x74", "answer_room"),  # je answer_room
        b"\x4C\x8B\x83" + struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["_scummVars"]),  # mov r8, [rbx + variables]
        b"\x45\x3B\x48\x10",  # cmp r9d, [r8 + 0x10]  ; VAR_ROOM
        ("jump", b"\x74", "answer_room"),  # je answer_room
        b"\x44\x0F\xB6\x9B" + struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["_currentScript"]),  # movzx r11d, byte [rbx + current script]
        b"\x41\x83\xFB\x50",  # cmp r11d, 80  ; script slot count
        ("jump", b"\x73", "answer_room"),  # jae answer_room
        b"\x45\x6B\xDB\x14",  # imul r11d, r11d, 20  ; script slot size
        b"\x46\x0F\xB7\x9C\x1B" + struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["vm.slot"] + 8),  # movzx r11d, word [rbx + r11 + slot number]
        b"\x41\x39\xFB",  # cmp r11d, edi
        ("jump", b"\x75", "answer_room"),  # jne answer_room
        ("jump", b"\xEB", "pass_through"),  # jmp pass_through

        ("label", "answer_room"),
        b"\xC7\x84\x83" + stack_top + struct.pack("<i", 15),  # mov dword [rbx + rax*4 + top], 15

        ("label", "done"),
        b"\x48\x83\xC4\x20",  # add rsp, 0x20
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xC3",  # ret

        ("label", "pass_through"),
        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x48\x8B\x46\x28",  # mov rax, [rsi + 0x28]  ; original getOwner
        b"\x48\x83\xC4\x20",  # add rsp, 0x20
        b"\x5F",  # pop rdi
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xFF\xE0",  # jmp rax
    ])


def build_talk_logger_code(cave_address: int, original_function_offset: int) -> bytes:
    return assemble([
        b"\x49\xBA" + struct.pack("<Q", cave_address + TALK_DATA_OFFSET),  # mov r10, talk data
        b"\x4C\x8B\x81" + struct.pack("<i", SCUMM_ENGINE_MEMBER_OFFSETS["_scriptPointer"]),  # mov r8, [rcx + script pointer]
        b"\x66\x41\x81\x38\xFF\x0A",  # cmp word [r8], 0x0AFF  ; voice marker
        ("jump", b"\x75", "done"),  # jne done

        b"\x41\x0F\xB7\x40\x02",  # movzx eax, word [r8 + 2]  ; voice id, low word
        b"\x41\x0F\xB7\x50\x06",  # movzx edx, word [r8 + 6]  ; voice id, high word
        b"\xC1\xE2\x10",  # shl edx, 16
        b"\x09\xD0",  # or eax, edx

        b"\x41\x8B\x52\x10",  # mov edx, [r10 + 0x10]  ; log count
        b"\x41\x89\xD1",  # mov r9d, edx
        b"\x41\x83\xE1" + struct.pack("<b", TALK_LOG_CAPACITY - 1),  # and r9d, log capacity - 1
        b"\x49\xBB" + struct.pack("<Q", cave_address + TALK_LOG_OFFSET),  # mov r11, talk log
        b"\x43\x89\x04\x8B",  # mov [r11 + r9*4], eax
        b"\xFF\xC2",  # inc edx
        b"\x41\x89\x52\x10",  # mov [r10 + 0x10], edx  ; log count

        ("label", "done"),
        b"\x41\xFF\x62" + struct.pack("<b", original_function_offset),  # jmp [r10 + original talk opcode]
    ])


def build_sentence_logger_code(cave_address: int) -> bytes:
    stack_position: int = SCUMM_ENGINE_MEMBER_OFFSETS["_scummStackPos"]
    stack: int = SCUMM_ENGINE_MEMBER_OFFSETS["_vmStack"]
    object_mask: bytes = struct.pack("<i", (1 << SENTENCE_OBJECT_BITS) - 1)

    return assemble([
        b"\x49\xBA" + struct.pack("<Q", cave_address + SENTENCE_DATA_OFFSET),  # mov r10, sentence data
        b"\x8B\x81" + struct.pack("<i", stack_position),  # mov eax, [rcx + stack position]
        b"\x83\xF8\x04",  # cmp eax, 4  ; verb, object A, unused, object B
        ("jump", b"\x7D", "enough_arguments"),  # jge enough_arguments
        b"\x41\xFF\x22",  # jmp [r10]  ; original doSentence

        ("label", "enough_arguments"),
        b"\x4C\x8D\x04\x81",  # lea r8, [rcx + rax*4]
        b"\x41\x8B\x90" + struct.pack("<i", stack - 16),  # mov edx, [r8 + stack - 16]  ; verb
        b"\xC1\xE2" + struct.pack("<b", SENTENCE_OBJECT_BITS),  # shl edx, object bits
        b"\x45\x8B\x88" + struct.pack("<i", stack - 12),  # mov r9d, [r8 + stack - 12]  ; object A
        b"\x41\x81\xE1" + object_mask,  # and r9d, object mask
        b"\x44\x09\xCA",  # or edx, r9d
        b"\xC1\xE2" + struct.pack("<b", SENTENCE_OBJECT_BITS),  # shl edx, object bits
        b"\x45\x8B\x88" + struct.pack("<i", stack - 4),  # mov r9d, [r8 + stack - 4]  ; object B
        b"\x41\x81\xE1" + object_mask,  # and r9d, object mask
        b"\x44\x09\xCA",  # or edx, r9d  ; packed sentence

        b"\x41\x8B\x42\x08",  # mov eax, [r10 + 0x08]  ; log count
        b"\x41\x89\xC1",  # mov r9d, eax
        b"\x41\x83\xE1" + struct.pack("<b", SENTENCE_LOG_CAPACITY - 1),  # and r9d, log capacity - 1
        b"\x49\xBB" + struct.pack("<Q", cave_address + SENTENCE_LOG_OFFSET),  # mov r11, sentence log
        b"\x43\x89\x14\x8B",  # mov [r11 + r9*4], edx
        b"\xFF\xC0",  # inc eax
        b"\x41\x89\x42\x08",  # mov [r10 + 0x08], eax  ; log count

        b"\x45\x8B\x5A\x0C",  # mov r11d, [r10 + 0x0C]  ; blocked count
        b"\x45\x31\xC9",  # xor r9d, r9d

        ("label", "next_blocked_sentence"),
        b"\x45\x39\xD9",  # cmp r9d, r11d
        ("jump", b"\x7D", "done"),  # jge done
        b"\x43\x8B\x44\xCA\x14",  # mov eax, [r10 + r9*8 + 0x14]  ; blocked sentence mask
        b"\x21\xD0",  # and eax, edx
        b"\x43\x3B\x44\xCA\x10",  # cmp eax, [r10 + r9*8 + 0x10]  ; blocked sentence
        ("jump", b"\x74", "block"),  # je block
        b"\x41\xFF\xC1",  # inc r9d
        ("jump", b"\xEB", "next_blocked_sentence"),  # jmp next_blocked_sentence

        ("label", "block"),
        b"\x83\xA9" + struct.pack("<i", stack_position) + b"\x04",  # sub dword [rcx + stack position], 4
        b"\xC3",  # ret

        ("label", "done"),
        b"\x41\xFF\x22",  # jmp [r10]  ; original doSentence
    ])


def build_script_blocker_code(cave_address: int, original_function_offset: int, popped_besides_the_arguments: int) -> bytes:
    stack_position: int = SCUMM_ENGINE_MEMBER_OFFSETS["_scummStackPos"]
    stack: int = SCUMM_ENGINE_MEMBER_OFFSETS["_vmStack"]

    return assemble([
        b"\x49\xBA" + struct.pack("<Q", cave_address + SCRIPT_DATA_OFFSET),  # mov r10, script data
        b"\x8B\x81" + struct.pack("<i", stack_position),  # mov eax, [rcx + stack position]
        b"\x85\xC0",  # test eax, eax
        ("jump", b"\x7E", "pass_through"),  # jle pass_through
        b"\x4C\x8D\x04\x81",  # lea r8, [rcx + rax*4]
        b"\x45\x8B\x80" + struct.pack("<i", stack - 4),  # mov r8d, [r8 + stack - 4]  ; argument count
        b"\x45\x8D\x48\x02",  # lea r9d, [r8 + 2]  ; the script sits below the arguments and their count
        b"\x44\x39\xC8",  # cmp eax, r9d
        ("jump", b"\x7C", "pass_through"),  # jl pass_through
        b"\x44\x29\xC8",  # sub eax, r9d  ; position of the script number
        b"\x8B\x94\x81" + struct.pack("<i", stack),  # mov edx, [rcx + rax*4 + stack]  ; script number
        b"\x45\x8B\x5A\x0C",  # mov r11d, [r10 + 0x0C]  ; blocked count
        b"\x45\x31\xC9",  # xor r9d, r9d

        ("label", "next_blocked_script"),
        b"\x45\x39\xD9",  # cmp r9d, r11d
        ("jump", b"\x7D", "pass_through"),  # jge pass_through
        b"\x43\x3B\x54\x8A\x10",  # cmp edx, [r10 + r9*4 + 0x10]  ; blocked script
        ("jump", b"\x74", "block"),  # je block
        b"\x41\xFF\xC1",  # inc r9d
        ("jump", b"\xEB", "next_blocked_script"),  # jmp next_blocked_script

        ("label", "block"),
        b"\x41\x8B\x42\x08",  # mov eax, [r10 + 0x08]  ; log count
        b"\x41\x89\xC1",  # mov r9d, eax
        b"\x41\x83\xE1" + struct.pack("<b", SCRIPT_LOG_CAPACITY - 1),  # and r9d, log capacity - 1
        b"\x49\xBB" + struct.pack("<Q", cave_address + SCRIPT_LOG_OFFSET),  # mov r11, script log
        b"\x43\x89\x14\x8B",  # mov [r11 + r9*4], edx
        b"\xFF\xC0",  # inc eax
        b"\x41\x89\x42\x08",  # mov [r10 + 0x08], eax  ; log count
        b"\x41\x83\xC0" + struct.pack("<b", popped_besides_the_arguments),  # add r8d, count, script (and flags)
        b"\x44\x29\x81" + struct.pack("<i", stack_position),  # sub [rcx + stack position], r8d  ; pop everything
        b"\xC3",  # ret

        ("label", "pass_through"),
        b"\x41\xFF\x62" + struct.pack("<b", original_function_offset),  # jmp [r10 + original start script opcode]
    ])


def build_script_bytes_caller_code() -> bytes:
    script_pointer: int = SCUMM_ENGINE_MEMBER_OFFSETS["_scriptPointer"]

    return assemble([
        b"\x53",  # push rbx
        b"\x56",  # push rsi
        b"\x48\x83\xEC\x28",  # sub rsp, 0x28
        b"\x48\x89\xCB",  # mov rbx, rcx  ; engine
        b"\x48\x8B\xB3" + struct.pack("<i", script_pointer),  # mov rsi, [rbx + script pointer]  ; the running script's position
        b"\x48\x89\x93" + struct.pack("<i", script_pointer),  # mov [rbx + script pointer], rdx  ; the bytes the opcode reads
        b"\x48\x89\xD9",  # mov rcx, rbx  ; engine
        b"\x41\xFF\xD0",  # call r8  ; opcode
        b"\x48\x89\xB3" + struct.pack("<i", script_pointer),  # mov [rbx + script pointer], rsi
        b"\x48\x83\xC4\x28",  # add rsp, 0x28
        b"\x5E",  # pop rsi
        b"\x5B",  # pop rbx
        b"\xC3",  # ret
    ])


def build_input_blocker_code(cave_address: int) -> bytes:
    return assemble([
        b"\x49\xBA" + struct.pack("<Q", cave_address + INPUT_DATA_OFFSET),  # mov r10, input data
        b"\x41\x51",  # push r9  ; input mode, which the original needs back
        b"\x89\xD0",  # mov eax, edx  ; input area
        b"\xC1\xE0\x10",  # shl eax, 16
        b"\x45\x0F\xB7\xD8",  # movzx r11d, r8w  ; input value
        b"\x44\x09\xD8",  # or eax, r11d  ; packed input
        b"\x45\x8B\x5A\x08",  # mov r11d, [r10 + 0x08]  ; blocked count
        b"\x45\x31\xC9",  # xor r9d, r9d

        ("label", "next_blocked_input"),
        b"\x45\x39\xD9",  # cmp r9d, r11d
        ("jump", b"\x7D", "pass_through"),  # jge pass_through
        b"\x43\x3B\x44\x8A\x10",  # cmp eax, [r10 + r9*4 + 0x10]  ; blocked input
        ("jump", b"\x74", "block"),  # je block
        b"\x41\xFF\xC1",  # inc r9d
        ("jump", b"\xEB", "next_blocked_input"),  # jmp next_blocked_input

        ("label", "block"),
        b"\x41\x59",  # pop r9
        b"\xC3",  # ret

        ("label", "pass_through"),
        b"\x41\x59",  # pop r9
        b"\x41\xFF\x22",  # jmp [r10]  ; original runInputScript
    ])


class ScummVMScummProcess:
    process: Pymem
    module: pymem.ressources.structure.MODULEINFO
    module_base: int
    module_end: int

    engine_address: Optional[int]
    opcode_indexes: Dict[str, int]
    opcode_functor_addresses: Dict[str, int]

    cave_address: Optional[int]
    voice_log_cursor: Optional[int]
    sentence_log_cursor: Optional[int]
    script_log_cursor: Optional[int]

    def __init__(self, process: Pymem, module_name: str) -> None:
        self.process = process
        self.module = pymem.process.module_from_name(self.process.process_handle, module_name)
        self.module_base = self.module.lpBaseOfDll
        self.module_end = self.module_base + self.module.SizeOfImage

        if os.path.getsize(self.module.filename) != 201266688:
            raise RuntimeError(f"{self.module.filename} is not ScummVM 2026.3.0 (win64)")

        self.engine_address = None
        self.opcode_indexes = dict()
        self.opcode_functor_addresses = dict()

        self.cave_address = None
        self.voice_log_cursor = None
        self.sentence_log_cursor = None
        self.script_log_cursor = None

    def locate_engine(self) -> int:
        needles: List[bytes] = [struct.pack("<Q", string_address) for string_address in self._find_string_addresses("o6_pickupObject")]

        if not needles:
            raise RuntimeError("Opcode name 'o6_pickupObject' not found in executable")

        region_base: int
        region_size: int
        for region_base, region_size in self._iterate_private_writable_regions():
            try:
                region: bytes = self.process.read_bytes(region_base, region_size)
            except Exception:
                continue

            needle: bytes
            for needle in needles:
                position: int = region.find(needle)

                while position != -1:
                    description_field_address: int = region_base + position

                    functor: Optional[Tuple[int, int]] = None

                    if description_field_address % 8 == 0:
                        functor = self._read_functor(self.read_pointer(description_field_address - 8))

                    if functor is not None:
                        engine_address: int = functor[0]
                        entry_offset: int = description_field_address - 8 - (engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_opcodes"])

                        if 0 <= entry_offset < 256 * 16 and entry_offset % 16 == 0:
                            self.engine_address = engine_address
                            self._read_opcode_table()

                            return engine_address

                    position = region.find(needle, position + 1)

        raise RuntimeError("SCUMM engine object not found; is a SCUMM game running?")

    def is_engine_current(self) -> bool:
        if self.engine_address is None:
            return False

        table_address: int = self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_opcodes"]

        try:
            return all(
                self.read_pointer(table_address + self.opcode_indexes[opcode_name] * 16) == self.opcode_functor_addresses[opcode_name]
                for opcode_name, _, _ in HOOKS
            )
        except Exception:
            return False

    def install_hooks(self) -> None:
        queue_function: int = self._read_functor_function("o6_breakHere")

        if not self._is_inside_module(queue_function):
            try:
                magic: int = self.process.read_ulonglong(queue_function + MAILBOX_OFFSET + 0x18)
            except Exception:
                magic = 0

            if magic >> 8 != MAILBOX_MAGIC >> 8:
                raise RuntimeError("o6_breakHere is already hooked by something else")

            if magic == MAILBOX_MAGIC:
                self._adopt_cave(queue_function)

                return

            self._restore_hooks(queue_function)

        originals: List[int] = [self._read_functor_function(opcode_name) for opcode_name, _, _ in HOOKS]

        opcode_name: str
        original: int
        for (opcode_name, _, _), original in zip(HOOKS, originals):
            if not self._is_inside_module(original):
                raise RuntimeError(f"{opcode_name} is already hooked by something else")

        input_slot_address: int = self._get_virtual_slot_address("ScummEngine::runInputScript")
        input_original: int = self.read_pointer(input_slot_address)

        if not self._is_inside_module(input_original):
            raise RuntimeError("runInputScript is already hooked by something else")

        self.cave_address = self.process.allocate(0x7000)

        self._write_cave(CALL_QUEUE_CODE_OFFSET, build_call_queue_code(self.cave_address))
        self._write_cave(PICKUP_FILTER_CODE_OFFSET, build_pickup_filter_code(self.cave_address))
        self._write_cave(OWNER_FILTER_CODE_OFFSET, build_owner_filter_code(self.cave_address))
        self._write_cave(TALK_ACTOR_LOGGER_CODE_OFFSET, build_talk_logger_code(self.cave_address, 0x00))
        self._write_cave(TALK_EGO_LOGGER_CODE_OFFSET, build_talk_logger_code(self.cave_address, 0x08))
        self._write_cave(SENTENCE_LOGGER_CODE_OFFSET, build_sentence_logger_code(self.cave_address))
        self._write_cave(SCRIPT_BLOCKER_CODE_OFFSET, build_script_blocker_code(self.cave_address, 0x00, 3))
        self._write_cave(QUICK_SCRIPT_BLOCKER_CODE_OFFSET, build_script_blocker_code(self.cave_address, 0x30, 2))
        self._write_cave(SECOND_QUICK_SCRIPT_BLOCKER_CODE_OFFSET, build_script_blocker_code(self.cave_address, 0x38, 2))
        self._write_cave(SCRIPT_BYTES_CALLER_CODE_OFFSET, build_script_bytes_caller_code())
        self._write_cave(INPUT_BLOCKER_CODE_OFFSET, build_input_blocker_code(self.cave_address))

        self._write_cave(MAILBOX_OFFSET, struct.pack("<IIQQQ", MAILBOX_STATE_IDLE, 0, originals[0], 0, MAILBOX_MAGIC))

        self._write_cave(PICKUP_DATA_OFFSET, struct.pack(
            "<QQQQQQ",
            originals[1],
            self._get_function_address("ScummEngine::putClass"),
            self._get_function_address("ScummEngine::putState"),
            self._get_function_address("ScummEngine::markObjectRectAsDirty"),
            self._get_function_address("ScummEngine::clearDrawObjectQueue"),
            originals[2],
        ))

        self._write_cave(TALK_DATA_OFFSET, struct.pack("<QQI", originals[3], originals[4], 0))
        self._write_cave(SENTENCE_DATA_OFFSET, struct.pack(f"<QII{2 * SENTENCE_BLOCKED_CAPACITY}I", originals[5], 0, 0, *([0] * (2 * SENTENCE_BLOCKED_CAPACITY))))
        self._write_cave(SCRIPT_DATA_OFFSET, struct.pack(f"<QII{SCRIPT_BLOCKED_CAPACITY}IQQ", originals[6], 0, 0, *([0] * SCRIPT_BLOCKED_CAPACITY), originals[7], originals[8]))
        self._write_cave(INPUT_DATA_OFFSET, struct.pack(f"<QI4x{INPUT_BLOCKED_CAPACITY}I", input_original, 0, *([0] * INPUT_BLOCKED_CAPACITY)))

        code_offset: int
        for opcode_name, code_offset, _ in HOOKS:
            self._write_functor_function(opcode_name, self.cave_address + code_offset)

        self._write_protected_pointer(input_slot_address, self.cave_address + INPUT_BLOCKER_CODE_OFFSET)

    def read_pointer(self, address: int) -> int:
        return self.process.read_ulonglong(address)

    def read_c_string(self, address: int, maximum_length: int = 64) -> str:
        try:
            raw_bytes: bytes = self.process.read_bytes(address, maximum_length)
        except Exception:
            return ""

        return raw_bytes.split(b"\x00")[0].decode("ascii", errors="replace")

    def read_game_id(self) -> str:
        game_id_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_game"])

        if not self._is_inside_module(game_id_address):
            return ""

        return self.read_c_string(game_id_address)

    def read_variable(self, index: int) -> int:
        variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_scummVars"])

        return self.process.read_int(variables_address + index * 4)

    def read_variables(self) -> Tuple[int, ...]:
        variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_scummVars"])
        count: int = self.process.read_int(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_numVariables"])

        return struct.unpack(f"<{count}i", self.process.read_bytes(variables_address, count * 4))

    def write_variable(self, index: int, value: int) -> None:
        variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_scummVars"])

        self.process.write_int(variables_address + index * 4, value)

    def read_bit_variable(self, index: int) -> int:
        bit_variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_bitVars"])

        return (self.process.read_uchar(bit_variables_address + (index >> 3)) >> (index & 7)) & 1

    def read_bit_variables(self) -> bytes:
        bit_variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_bitVars"])
        count: int = self.process.read_int(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_numBitVariables"])

        return self.process.read_bytes(bit_variables_address, count // 8)

    def write_bit_variable(self, index: int, value: int) -> None:
        bit_variables_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_bitVars"])
        current: int = self.process.read_uchar(bit_variables_address + (index >> 3))
        mask: int = 1 << (index & 7)

        self.process.write_uchar(bit_variables_address + (index >> 3), (current | mask) if value else (current & ~mask))

    def read_current_room(self) -> int:
        return self.read_variable(4)

    def read_ego(self) -> int:
        return self.read_variable(1)

    def call_on_main_thread(self, calls: Sequence[Tuple[int, ...]], timeout_seconds: float = 5.0) -> List[int]:
        self._ensure_hooks()

        if len(calls) > 16:
            raise RuntimeError(f"Too many calls queued at once ({len(calls)})")

        records: bytes = bytes().join(
            struct.pack("<Qqqqqq", *(tuple(call) + (0,) * (6 - len(call))))
            for call in calls
        )

        mailbox_address: int = self.cave_address + MAILBOX_OFFSET

        self.process.write_bytes(mailbox_address + 0x20, records, len(records))
        self.process.write_uint(mailbox_address + 0x04, len(calls))
        self.process.write_uint(mailbox_address, MAILBOX_STATE_PENDING)

        deadline: float = time.perf_counter() + timeout_seconds

        while self.process.read_uint(mailbox_address) != MAILBOX_STATE_DONE:
            if time.perf_counter() > deadline:
                if self.process.read_uint(mailbox_address) == MAILBOX_STATE_PENDING:
                    self.process.write_uint(mailbox_address, MAILBOX_STATE_IDLE)

                raise RuntimeError("Main thread did not service the call queue in time")

            time.sleep(0.005)

        self.process.write_uint(mailbox_address, MAILBOX_STATE_IDLE)

        results: bytes = self.process.read_bytes(mailbox_address + 0x20, len(records))

        return [struct.unpack_from("<i", results, record_index * 0x30 + 0x20)[0] for record_index in range(len(calls))]

    def call_opcode(self, opcode_name: str, *stack_arguments: int) -> None:
        self._ensure_hooks()

        function_address: int = self._read_functor_function(opcode_name)

        original_function_offset: int
        for _, code_offset, original_function_offset in HOOKS:
            if function_address == self.cave_address + code_offset:
                function_address = self.process.read_ulonglong(self.cave_address + original_function_offset)

        push_address: int = self._get_function_address("ScummEngine::push")
        calls: List[Tuple[int, ...]] = [(push_address, argument) for argument in stack_arguments]

        calls.append((function_address,))

        self.call_on_main_thread(calls)

    def read_running_scripts(self) -> List[int]:
        slots: bytes = self.process.read_bytes(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["vm.slot"], 80 * 20)

        running_scripts: List[int] = list()

        slot: int
        for slot in range(1, 80):
            if slots[slot * 20 + 15] != 0:
                running_scripts.append(struct.unpack_from("<H", slots, slot * 20 + 8)[0])

        return running_scripts

    def start_script(self, script_number: int, *arguments: int) -> None:
        self.call_opcode("o6_startScript", 0, script_number, *arguments, len(arguments))

    def start_object(self, object_id: int, verb: int, *arguments: int) -> None:
        self.call_opcode("o6_startObject", 0, object_id, verb, *arguments, len(arguments))

    def do_sentence(self, verb: int, object_a: int, object_b: int) -> None:
        self.call_opcode("o6_doSentence", verb, object_a, 0, object_b)

    def read_actor_costume(self, actor: int) -> int:
        actors_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_actors"])

        return self.process.read_ushort(self.read_pointer(actors_address + actor * 8) + 0x22)

    def read_actor_room(self, actor: int) -> int:
        actors_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_actors"])

        return self.process.read_uchar(self.read_pointer(actors_address + actor * 8) + 0x24)

    def put_actor(self, actor: int, x: int, y: int, room: int) -> None:
        self.call_opcode("o6_putActorAtXY", actor, x, y, room)

    def animate_actor(self, actor: int, animation: int) -> None:
        self.call_opcode("o6_animateActor", actor, animation)

    def run_actor_operations(self, actor: int, operations: Sequence[Tuple]) -> None:
        self._ensure_hooks()

        sub_opcodes: Dict[str, int] = {
            "costume": 76,
            "default": 83,
            "elevation": 84,
            "palette": 86,
            "talk_color": 87,
            "scale": 92,
            "never_zclip": 93,
            "always_zclip": 94,
            "ignore_boxes": 95,
        }

        script_bytes: bytes = bytes([197] + [sub_opcodes[operation[0]] for operation in operations])

        if len(script_bytes) > 0x80:
            raise RuntimeError(f"Too many actor operations at once ({len(operations)})")

        self._write_cave(SCRIPT_BYTES_OFFSET, script_bytes)

        push_address: int = self._get_function_address("ScummEngine::push")
        caller_address: int = self.cave_address + SCRIPT_BYTES_CALLER_CODE_OFFSET
        actor_ops_address: int = self._read_functor_function("o6_actorOps")
        select_actor: List[Tuple[int, ...]] = [
            (push_address, actor),
            (caller_address, self.cave_address + SCRIPT_BYTES_OFFSET, actor_ops_address),
        ]

        batch: List[Tuple[int, ...]] = list(select_actor)

        index: int
        operation: Tuple
        for index, operation in enumerate(operations, start=1):
            calls: List[Tuple[int, ...]] = [(push_address, argument) for argument in operation[1:]]
            calls.append((caller_address, self.cave_address + SCRIPT_BYTES_OFFSET + index, actor_ops_address))

            if len(batch) + len(calls) > 16:
                self.call_on_main_thread(batch)
                batch = list(select_actor)

            batch.extend(calls)

        self.call_on_main_thread(batch)

    def set_actor_costume(self, actor: int, costume: int) -> None:
        self.run_actor_operations(actor, [("costume", costume)])

    def read_global_object_count(self) -> int:
        return self.process.read_int(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_numGlobalObjects"])

    def read_object_owner(self, object_id: int) -> int:
        table_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_objectOwnerTable"])

        return self.process.read_uchar(table_address + object_id)

    def read_object_owner_table(self) -> bytes:
        table_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_objectOwnerTable"])

        return self.process.read_bytes(table_address, self.read_global_object_count())

    def read_object_state(self, object_id: int) -> int:
        table_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_objectStateTable"])

        return self.process.read_uchar(table_address + object_id)

    def read_object_state_table(self) -> bytes:
        table_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_objectStateTable"])

        return self.process.read_bytes(table_address, self.read_global_object_count())

    def read_object_class_table(self) -> Tuple[int, ...]:
        table_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_classData"])
        count: int = self.read_global_object_count()

        return struct.unpack(f"<{count}I", self.process.read_bytes(table_address, count * 4))

    def read_inventory(self) -> List[int]:
        capacity: int = self.process.read_int(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_numInventory"])
        inventory_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_inventory"])
        slots: Tuple[int, ...] = struct.unpack(f"<{capacity}H", self.process.read_bytes(inventory_address, capacity * 2))

        return [object_id for object_id in slots if object_id != 0]

    def give_object(self, object_id: int, room: int, owner: Optional[int] = None, classes_to_set: Sequence[int] = (), state: Optional[int] = None) -> None:
        if owner is None:
            owner = self.read_ego()

        calls: List[Tuple[int, ...]] = list()

        if object_id not in self.read_inventory():
            calls.append((self._get_function_address("ScummEngine::addObjectToInventory"), object_id, room))

        calls.append((self._get_function_address("ScummEngine::putOwner"), object_id, owner))

        class_number: int
        for class_number in classes_to_set:
            calls.append((self._get_function_address("ScummEngine::putClass"), object_id, class_number, 1))

        if state is not None:
            calls.append((self._get_function_address("ScummEngine::putState"), object_id, state))

        calls.append((self._get_virtual_function_address("ScummEngine::runInventoryScript"), object_id))

        self.call_on_main_thread(calls)

    def remove_object(self, object_id: int) -> None:
        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::clearOwnerOf"), object_id),
            (self._get_function_address("ScummEngine::putOwner"), object_id, 0),
            (self._get_virtual_function_address("ScummEngine::runInventoryScript"), object_id),
        ])

    def write_object_owner(self, object_id: int, owner: int) -> None:
        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::putOwner"), object_id, owner),
        ])

    def transfer_object(self, object_id: int, new_owner: int) -> None:
        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::putOwner"), object_id, new_owner),
            (self._get_virtual_function_address("ScummEngine::runInventoryScript"), object_id),
        ])

    def write_object_state(self, object_id: int, state: int) -> None:
        if self.read_object_state(object_id) == state:
            return

        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::putState"), object_id, state),
            (self._get_function_address("ScummEngine::markObjectRectAsDirty"), object_id),
            (self._get_function_address("ScummEngine::clearDrawObjectQueue"),),
        ])

    def write_object_class(self, object_id: int, class_number: int, is_set: bool) -> None:
        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::putClass"), object_id, class_number, int(is_set)),
        ])

    def set_object_hidden(self, object_id: int, is_hidden: bool, visible_state: int = 0) -> None:
        state: int = 1 if is_hidden else visible_state
        is_untouchable: bool = bool(self.read_object_class_table()[object_id] >> (OBJECT_CLASS_UNTOUCHABLE - 1) & 1)

        if self.read_object_state(object_id) == state and is_untouchable == is_hidden:
            return

        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::putClass"), object_id, OBJECT_CLASS_UNTOUCHABLE, int(is_hidden)),
            (self._get_function_address("ScummEngine::putState"), object_id, state),
            (self._get_function_address("ScummEngine::markObjectRectAsDirty"), object_id),
            (self._get_function_address("ScummEngine::clearDrawObjectQueue"),),
        ])

    def set_object_name(self, object_id: int, name: bytes) -> None:
        self._ensure_hooks()

        if len(name) + 1 > 0x80:
            raise RuntimeError(f"Name is too long ({len(name)} bytes)")

        self._write_cave(SCRIPT_BYTES_OFFSET, name + b"\x00")

        self.call_on_main_thread([
            (self._get_function_address("ScummEngine::push"), object_id),
            (self.cave_address + SCRIPT_BYTES_CALLER_CODE_OFFSET, self.cave_address + SCRIPT_BYTES_OFFSET, self._read_functor_function("o6_setObjectName")),
        ])

    def intercept_pickups(self, object_ids: Sequence[int]) -> None:
        self._ensure_hooks()

        table_address: int = self.cave_address + PICKUP_TABLE_OFFSET
        table: bytes = self.process.read_bytes(table_address, PICKUP_TABLE_SIZE)

        object_id: int
        for object_id in object_ids:
            if table[object_id] == PICKUP_IGNORED:
                self.process.write_uchar(table_address + object_id, PICKUP_INTERCEPTED)

    def release_pickups(self, object_ids: Sequence[int]) -> None:
        self._ensure_hooks()

        table_address: int = self.cave_address + PICKUP_TABLE_OFFSET
        table: bytes = self.process.read_bytes(table_address, PICKUP_TABLE_SIZE)

        object_id: int
        for object_id in object_ids:
            if table[object_id] != PICKUP_IGNORED:
                self.process.write_uchar(table_address + object_id, PICKUP_IGNORED)

    def check_pickups(self, object_ids: Sequence[int]) -> None:
        self._ensure_hooks()

        object_id: int
        for object_id in object_ids:
            self.process.write_uchar(self.cave_address + PICKUP_TABLE_OFFSET + object_id, PICKUP_CHECKED)

    def set_pickup_rooms(self, objects_and_rooms: Sequence[Tuple[int, int]]) -> None:
        self._ensure_hooks()

        table_address: int = self.cave_address + PICKUP_ROOM_TABLE_OFFSET
        table: bytes = self.process.read_bytes(table_address, PICKUP_TABLE_SIZE)

        object_id: int
        room: int
        for object_id, room in objects_and_rooms:
            if table[object_id] != room:
                self.process.write_uchar(table_address + object_id, room)

    def read_intercepted_pickups(self) -> List[int]:
        table: bytes = self.process.read_bytes(self.cave_address + PICKUP_TABLE_OFFSET, PICKUP_TABLE_SIZE)

        return [object_id for object_id, value in enumerate(table) if value == PICKUP_INTERCEPTED]

    def read_checked_pickups(self) -> List[int]:
        table: bytes = self.process.read_bytes(self.cave_address + PICKUP_TABLE_OFFSET, PICKUP_TABLE_SIZE)

        return [object_id for object_id, value in enumerate(table) if value == PICKUP_CHECKED]

    def read_new_voice_ids(self) -> List[int]:
        self._ensure_hooks()

        count: int = self.process.read_uint(self.cave_address + TALK_DATA_OFFSET + 0x10)

        if self.voice_log_cursor is None or self.voice_log_cursor > count:
            self.voice_log_cursor = count

        first: int = max(self.voice_log_cursor, count - TALK_LOG_CAPACITY)
        log: Tuple[int, ...] = struct.unpack(f"<{TALK_LOG_CAPACITY}I", self.process.read_bytes(self.cave_address + TALK_LOG_OFFSET, TALK_LOG_CAPACITY * 4))

        self.voice_log_cursor = count

        return [log[index % TALK_LOG_CAPACITY] for index in range(first, count)]

    def read_new_sentences(self) -> List[Tuple[int, int, int]]:
        self._ensure_hooks()

        count: int = self.process.read_uint(self.cave_address + SENTENCE_DATA_OFFSET + 0x08)

        if self.sentence_log_cursor is None or self.sentence_log_cursor > count:
            self.sentence_log_cursor = count

        first: int = max(self.sentence_log_cursor, count - SENTENCE_LOG_CAPACITY)
        log: Tuple[int, ...] = struct.unpack(f"<{SENTENCE_LOG_CAPACITY}I", self.process.read_bytes(self.cave_address + SENTENCE_LOG_OFFSET, SENTENCE_LOG_CAPACITY * 4))
        object_mask: int = (1 << SENTENCE_OBJECT_BITS) - 1

        self.sentence_log_cursor = count

        sentences: List[Tuple[int, int, int]] = list()

        index: int
        for index in range(first, count):
            packed: int = log[index % SENTENCE_LOG_CAPACITY]

            sentences.append((packed >> (2 * SENTENCE_OBJECT_BITS), (packed >> SENTENCE_OBJECT_BITS) & object_mask, packed & object_mask))

        return sentences

    def block_sentences(self, sentences: Sequence[Tuple[int, int, int]]) -> None:
        self._ensure_hooks()

        if len(sentences) > SENTENCE_BLOCKED_CAPACITY:
            raise RuntimeError(f"At most {SENTENCE_BLOCKED_CAPACITY} sentences can be blocked")

        object_mask: int = (1 << SENTENCE_OBJECT_BITS) - 1
        entries: List[int] = list()

        verb: int
        object_a: int
        object_b: int
        for verb, object_a, object_b in sentences:
            entries.append((verb << (2 * SENTENCE_OBJECT_BITS)) | ((object_a & object_mask) << SENTENCE_OBJECT_BITS) | (object_b & object_mask))
            entries.append(0xFFFFFFFF if object_b else 0xFFFFF000)

        padded_entries: List[int] = entries + [0] * (2 * SENTENCE_BLOCKED_CAPACITY - len(entries))

        self._write_cave(SENTENCE_DATA_OFFSET + 0x0C, struct.pack(f"<I{2 * SENTENCE_BLOCKED_CAPACITY}I", len(sentences), *padded_entries))

    def block_scripts(self, script_numbers: Sequence[int]) -> None:
        self._ensure_hooks()

        if len(script_numbers) > SCRIPT_BLOCKED_CAPACITY:
            raise RuntimeError(f"At most {SCRIPT_BLOCKED_CAPACITY} scripts can be blocked")

        padded_script_numbers: List[int] = list(script_numbers) + [0] * (SCRIPT_BLOCKED_CAPACITY - len(script_numbers))

        self._write_cave(SCRIPT_DATA_OFFSET + 0x0C, struct.pack(f"<I{SCRIPT_BLOCKED_CAPACITY}I", len(script_numbers), *padded_script_numbers))

    def read_new_refused_script_starts(self) -> List[int]:
        self._ensure_hooks()

        count: int = self.process.read_uint(self.cave_address + SCRIPT_DATA_OFFSET + 0x08)

        if self.script_log_cursor is None or self.script_log_cursor > count:
            self.script_log_cursor = count

        first: int = max(self.script_log_cursor, count - SCRIPT_LOG_CAPACITY)
        log: Tuple[int, ...] = struct.unpack(f"<{SCRIPT_LOG_CAPACITY}I", self.process.read_bytes(self.cave_address + SCRIPT_LOG_OFFSET, SCRIPT_LOG_CAPACITY * 4))

        self.script_log_cursor = count

        return [log[index % SCRIPT_LOG_CAPACITY] for index in range(first, count)]

    def block_inputs(self, inputs: Sequence[Tuple[int, int]]) -> None:
        self._ensure_hooks()

        if len(inputs) > INPUT_BLOCKED_CAPACITY:
            raise RuntimeError(f"At most {INPUT_BLOCKED_CAPACITY} inputs can be blocked")

        packed_inputs: List[int] = [(input_area << 16) | (value & 0xFFFF) for input_area, value in inputs]
        padded_inputs: List[int] = packed_inputs + [0] * (INPUT_BLOCKED_CAPACITY - len(packed_inputs))

        self._write_cave(INPUT_DATA_OFFSET + 0x08, struct.pack(f"<I4x{INPUT_BLOCKED_CAPACITY}I", len(packed_inputs), *padded_inputs))

    def read_verb_visible(self, verb_id: int) -> Optional[bool]:
        slot_address: Optional[int] = self._find_verb_slot_address(verb_id)

        if slot_address is None:
            return None

        return self.process.read_uchar(slot_address + 0x18) == 1

    def read_verb_position(self, verb_id: int) -> Optional[Tuple[int, int]]:
        slot_address: Optional[int] = self._find_verb_slot_address(verb_id)

        if slot_address is None:
            return None

        top, left = struct.unpack("<hh", self.process.read_bytes(slot_address, 4))

        return left, top

    def set_verb_visible(self, verb_id: int, is_visible: bool, x: Optional[int] = None, y: Optional[int] = None) -> None:
        slot_address: Optional[int] = self._find_verb_slot_address(verb_id)

        if slot_address is None or self.read_verb_visible(verb_id) == is_visible:
            return

        if x is not None and y is not None:
            self.process.write_bytes(slot_address, struct.pack("<hh", y, x), 4)

        self.process.write_uchar(slot_address + 0x18, 1 if is_visible else 0)

        verbs_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_verbs"])

        self.call_on_main_thread([
            (self._get_virtual_function_address("ScummEngine::drawVerb"), (slot_address - verbs_address) // 0x24, 0, 0),
        ])

    def request_save(self, slot: int, description: str) -> None:
        encoded: bytes = description.encode("ascii") + b"\x00"

        if len(encoded) > 20:
            raise RuntimeError(f"Save description is too long ({len(description)} characters)")

        if self.is_save_or_load_pending():
            raise RuntimeError("Another save or load is already pending")

        string_address: int = self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_saveLoadDescription"]

        self.process.write_bytes(string_address + 0x10, encoded, len(encoded))
        self.process.write_ulonglong(string_address + 0x08, string_address + 0x10)
        self.process.write_uint(string_address, len(encoded) - 1)

        self.process.write_uchar(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_saveTemporaryState"], 0)
        self.process.write_uchar(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_saveLoadSlot"], slot)
        self.process.write_uchar(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_saveLoadFlag"], 1)

    def is_save_or_load_pending(self) -> bool:
        return bool(self.process.read_uchar(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_saveLoadFlag"]))

    def say(self, message: bytes, actor: Optional[int] = None) -> None:
        self._ensure_hooks()

        if actor is None:
            actor = self.read_ego()

        if len(message) + 1 > 0x1000:
            raise RuntimeError(f"Message is too long ({len(message)} bytes)")

        default_string_slot: bytes = self.process.read_bytes(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_string[0]._default"], 14)

        self._write_cave(MESSAGE_BUFFER_OFFSET, message + b"\x00")
        self.process.write_bytes(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_string[0]"], default_string_slot, len(default_string_slot))
        self.process.write_uchar(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_actorToPrintStrFor"], actor)

        self.call_on_main_thread([
            (self._get_virtual_function_address("ScummEngine::actorTalk"), self.cave_address + MESSAGE_BUFFER_OFFSET),
        ])

    def _find_string_addresses(self, text: str) -> List[int]:
        needle: bytes = b"\x00" + text.encode() + b"\x00"
        addresses: List[int] = list()

        with open(self.module.filename, "rb") as executable_file:
            data: bytes = executable_file.read()

        pe_offset: int = struct.unpack_from("<I", data, 0x3C)[0]
        section_count: int = struct.unpack_from("<H", data, pe_offset + 6)[0]
        optional_header_size: int = struct.unpack_from("<H", data, pe_offset + 20)[0]
        section_table_offset: int = pe_offset + 24 + optional_header_size

        sections: List[Tuple[int, int, int]] = list()

        section_index: int
        for section_index in range(section_count):
            virtual_size, virtual_address, raw_size, raw_offset = struct.unpack_from("<IIII", data, section_table_offset + section_index * 40 + 8)

            sections.append((raw_offset, raw_size, virtual_address))

        position: int = data.find(needle)

        while position != -1:
            string_offset: int = position + 1

            for raw_offset, raw_size, virtual_address in sections:
                if raw_offset <= string_offset < raw_offset + raw_size:
                    addresses.append(self.module_base + virtual_address + string_offset - raw_offset)

            position = data.find(needle, position + 1)

        return addresses

    def _iterate_private_writable_regions(self) -> Iterator[Tuple[int, int]]:
        address: int = 0x10000
        information: pymem.ressources.structure.MEMORY_BASIC_INFORMATION = pymem.ressources.structure.MEMORY_BASIC_INFORMATION()

        while address < 0x7FFFFFFF0000:
            result: int = pymem.ressources.kernel32.VirtualQueryEx(
                self.process.process_handle,
                ctypes.c_void_p(address),
                ctypes.byref(information),
                ctypes.sizeof(information),
            )

            if result == 0:
                break

            region_base: int = information.BaseAddress or 0
            region_size: int = information.RegionSize

            if information.State == 0x1000 and information.Type == 0x20000 and information.Protect == 0x04 and region_size <= 0x10000000:
                yield region_base, region_size

            address = region_base + region_size

    def _read_functor(self, functor_address: int) -> Optional[Tuple[int, int]]:
        try:
            virtual_table, target, function_address, adjustment = struct.unpack("<QQQQ", self.process.read_bytes(functor_address, 32))
        except Exception:
            return None

        if not self._is_inside_module(virtual_table) or adjustment != 0:
            return None

        return target, function_address

    def _read_opcode_table(self) -> None:
        table: bytes = self.process.read_bytes(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_opcodes"], 256 * 16)

        self.opcode_indexes = dict()
        self.opcode_functor_addresses = dict()

        index: int
        for index in range(256):
            functor_address, description_address = struct.unpack_from("<QQ", table, index * 16)

            if functor_address == 0 or description_address == 0 or self._read_functor(functor_address) is None:
                continue

            name: str = self.read_c_string(description_address)

            if name not in self.opcode_indexes:
                self.opcode_indexes[name] = index
                self.opcode_functor_addresses[name] = functor_address

    def _read_functor_function(self, opcode_name: str) -> int:
        return self.process.read_ulonglong(self.opcode_functor_addresses[opcode_name] + 16)

    def _write_functor_function(self, opcode_name: str, function_address: int) -> None:
        self.process.write_ulonglong(self.opcode_functor_addresses[opcode_name] + 16, function_address)

    def _is_inside_module(self, address: int) -> bool:
        return self.module_base <= address < self.module_end

    def _adopt_cave(self, cave_address: int) -> None:
        self.cave_address = cave_address
        self.process.write_uint(self.cave_address + MAILBOX_OFFSET, MAILBOX_STATE_IDLE)

        opcode_name: str
        code_offset: int
        original_function_offset: int
        for opcode_name, code_offset, original_function_offset in HOOKS:
            function_address: int = self._read_functor_function(opcode_name)

            if self._is_inside_module(function_address):
                self.process.write_ulonglong(self.cave_address + original_function_offset, function_address)
                self._write_functor_function(opcode_name, self.cave_address + code_offset)

        input_slot_address: int = self._get_virtual_slot_address("ScummEngine::runInputScript")
        input_function: int = self.read_pointer(input_slot_address)

        if self._is_inside_module(input_function):
            self.process.write_ulonglong(self.cave_address + INPUT_DATA_OFFSET, input_function)
            self._write_protected_pointer(input_slot_address, self.cave_address + INPUT_BLOCKER_CODE_OFFSET)

    def _restore_hooks(self, cave_address: int) -> None:
        opcode_name: str
        code_offset: int
        original_function_offset: int
        for opcode_name, code_offset, original_function_offset in HOOKS:
            if self._read_functor_function(opcode_name) == cave_address + code_offset:
                self._write_functor_function(opcode_name, self.process.read_ulonglong(cave_address + original_function_offset))

        input_slot_address: int = self._get_virtual_slot_address("ScummEngine::runInputScript")

        if self.read_pointer(input_slot_address) == cave_address + INPUT_BLOCKER_CODE_OFFSET:
            self._write_protected_pointer(input_slot_address, self.process.read_ulonglong(cave_address + INPUT_DATA_OFFSET))

    def _write_cave(self, offset: int, data: bytes) -> None:
        self.process.write_bytes(self.cave_address + offset, data, len(data))

    def _write_protected_pointer(self, address: int, value: int) -> None:
        previous_protection: ctypes.c_ulong = ctypes.c_ulong(0)

        if not pymem.ressources.kernel32.VirtualProtectEx(self.process.process_handle, ctypes.c_void_p(address), 8, 0x40, ctypes.byref(previous_protection)):
            raise RuntimeError(f"Could not make {address:#x} writable")

        self.process.write_ulonglong(address, value)

        pymem.ressources.kernel32.VirtualProtectEx(self.process.process_handle, ctypes.c_void_p(address), 8, previous_protection.value, ctypes.byref(previous_protection))

    def _get_function_address(self, name: str) -> int:
        return self.module_base + SCUMMVM_FUNCTION_RVAS[name]

    def _get_virtual_slot_address(self, name: str) -> int:
        return self.read_pointer(self.engine_address) + SCUMMVM_VIRTUAL_TABLE_OFFSETS[name]

    def _get_virtual_function_address(self, name: str) -> int:
        return self.read_pointer(self._get_virtual_slot_address(name))

    def _ensure_hooks(self) -> None:
        if not self.is_engine_current():
            self.cave_address = None
            self.locate_engine()

        if self.cave_address is None or self._read_functor_function("o6_breakHere") != self.cave_address + CALL_QUEUE_CODE_OFFSET:
            self.install_hooks()

    def _find_verb_slot_address(self, verb_id: int) -> Optional[int]:
        verbs_address: int = self.read_pointer(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_verbs"])
        verb_count: int = self.process.read_int(self.engine_address + SCUMM_ENGINE_MEMBER_OFFSETS["_numVerbs"])
        slots: bytes = self.process.read_bytes(verbs_address, verb_count * 0x24)

        slot_index: int
        for slot_index in range(verb_count):
            if struct.unpack_from("<H", slots, slot_index * 0x24 + 0x10)[0] == verb_id:
                return verbs_address + slot_index * 0x24

        return None
