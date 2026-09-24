from typing import Dict, List, NamedTuple, Optional, Tuple

from pymem import Pymem
from pymem.process import close_handle, list_processes
from pymem.ressources.structure import ProcessEntry32

from .data.game_data import (
    DayOfTheTentacleConditionData,
    character_to_internal_actor_id,
    character_to_portrait_hotkey,
    chron_o_johns_powered_before_the_finale,
    event_to_conditions,
    internal_actor_id_to_character,
    internal_room_id_to_room,
    item_to_internal_granted_flag_id,
    item_to_internal_object_and_room_id,
    item_to_internal_object_ids_hidden_with_it,
    item_to_internal_object_ids_redrawn_without_it,
    items_received_with_state_zero,
    items_removed_when_a_save_is_set_up,
    items_sent_between_characters_by_the_client,
    save_is_set_up_internal_flag_id,
    voice_line_to_internal_voice_id,
)

from .enums import (
    DayOfTheTentacleCharacters,
    DayOfTheTentacleConditionKinds,
    DayOfTheTentacleEvents,
    DayOfTheTentacleItems,
    DayOfTheTentacleRooms,
    DayOfTheTentacleVoiceLines,
)

from .scummvm_scumm import ScummVMScummProcess


class GameState(NamedTuple):
    is_valid: bool

    is_in_intro: Optional[bool] = None
    is_save_set_up: Optional[bool] = None

    room: Optional[DayOfTheTentacleRooms] = None
    character: Optional[DayOfTheTentacleCharacters] = None
    character_rooms: Optional[Dict[DayOfTheTentacleCharacters, Optional[DayOfTheTentacleRooms]]] = None

    events: Optional[Tuple[DayOfTheTentacleEvents, ...]] = None
    granted_items: Optional[Tuple[DayOfTheTentacleItems, ...]] = None
    picked_up_items: Optional[Tuple[DayOfTheTentacleItems, ...]] = None
    held_items: Optional[Tuple[DayOfTheTentacleItems, ...]] = None
    spoken_voice_lines: Optional[Tuple[DayOfTheTentacleVoiceLines, ...]] = None


class GameStateManager:
    process_name: str = "scummvm.exe"
    game_id: str = "tentacle"

    process: Optional[Pymem]
    is_process_running: bool

    scumm_process: Optional[ScummVMScummProcess]

    previous_condition_values: Optional[Tuple[int, ...]]

    characters_with_hidden_portraits: List[DayOfTheTentacleCharacters]
    blocked_sentences: List[Tuple[int, int, int]]
    finale_sentence_waiting_for_the_save: Optional[Tuple[int, int, int]]
    restored_object_ids: List[int]
    consumed_object_ids: List[int]
    object_ids_checked_by_the_client: List[int]
    previous_battery_charge: Optional[int]
    diamond_order_refusal: Optional[bytes]

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.scumm_process = None

        self.previous_condition_values = None

        self.characters_with_hidden_portraits = list()
        self.blocked_sentences = list()
        self.finale_sentence_waiting_for_the_save = None
        self.restored_object_ids = list()
        self.consumed_object_ids = list()
        self.object_ids_checked_by_the_client = list()
        self.previous_battery_charge = None
        self.diamond_order_refusal = None

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            candidate_process_ids: List[int] = list()

            process_entry: ProcessEntry32
            for process_entry in list_processes():
                if process_entry.szExeFile.decode("utf-8").lower() == self.process_name:
                    candidate_process_ids.append(process_entry.th32ProcessID)

            if not len(candidate_process_ids):
                return False

            process_id: int
            for process_id in candidate_process_ids:
                try:
                    process: Pymem = Pymem(process_id)
                except Exception:
                    continue

                try:
                    scumm_process: ScummVMScummProcess = ScummVMScummProcess(process, self.process_name)
                    scumm_process.locate_engine()

                    if scumm_process.read_game_id() == self.game_id:
                        self.process = process
                        self.scumm_process = scumm_process

                        break
                except Exception:
                    pass

                close_handle(process.process_handle)

            if self.process is None:
                return False

            self.scumm_process.install_hooks()

            self.scumm_process.read_new_voice_ids()
            self.scumm_process.read_new_sentences()
            self.scumm_process.read_new_refused_script_starts()

            self.is_process_running = True
        except Exception:
            if self.process is not None:
                close_handle(self.process.process_handle)

            self.process = None
            self.scumm_process = None

            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.scumm_process = None

            self.previous_condition_values = None

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.scumm_process = None

            self.previous_condition_values = None

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def mark_save_as_set_up(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        try:
            self.scumm_process.write_bit_variable(save_is_set_up_internal_flag_id, 1)
        except Exception:
            return False

        return True

    def set_unlocked_characters(self, unlocked_characters: List[DayOfTheTentacleCharacters]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        input_area_verb_click: int = 1
        input_area_key_press: int = 4

        blocked_inputs: List[Tuple[int, int]] = list()

        try:
            active_actor_id: int = self.scumm_process.read_ego()
            active_portrait_verb: int = 102 + active_actor_id

            if active_actor_id in internal_actor_id_to_character and self.scumm_process.read_verb_visible(active_portrait_verb):
                self.scumm_process.set_verb_visible(active_portrait_verb, False)

                if internal_actor_id_to_character[active_actor_id] not in self.characters_with_hidden_portraits:
                    self.characters_with_hidden_portraits.append(internal_actor_id_to_character[active_actor_id])

            character: DayOfTheTentacleCharacters
            for character in DayOfTheTentacleCharacters:
                portrait_verb: int = 102 + character_to_internal_actor_id[character]

                if character not in unlocked_characters:
                    blocked_inputs.append((input_area_verb_click, portrait_verb))
                    blocked_inputs.append((input_area_key_press, character_to_portrait_hotkey[character]))

                    self.scumm_process.set_verb_visible(portrait_verb, False)

                    if character not in self.characters_with_hidden_portraits:
                        self.characters_with_hidden_portraits.append(character)

                    continue

                if character in self.characters_with_hidden_portraits and character_to_internal_actor_id[character] != active_actor_id:
                    if self.scumm_process.read_verb_visible(portrait_verb):
                        self.characters_with_hidden_portraits.remove(character)

                        continue

                    portrait_x: int = 288
                    portrait_ys: List[int] = [152, 176]

                    other_character: DayOfTheTentacleCharacters
                    for other_character in DayOfTheTentacleCharacters:
                        other_portrait_verb: int = 102 + character_to_internal_actor_id[other_character]

                        if other_character != character and self.scumm_process.read_verb_visible(other_portrait_verb):
                            portrait_position: Optional[Tuple[int, int]] = self.scumm_process.read_verb_position(other_portrait_verb)

                            if portrait_position is not None and portrait_position[1] in portrait_ys:
                                portrait_ys.remove(portrait_position[1])

                    if not portrait_ys:
                        continue

                    self.scumm_process.set_verb_visible(portrait_verb, True, portrait_x, portrait_ys[0])
                    self.characters_with_hidden_portraits.remove(character)

            self.scumm_process.block_inputs(blocked_inputs)
        except Exception:
            return False

        return True

    def switch_character(self, character: DayOfTheTentacleCharacters) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        input_script: int = 120
        verb_click: int = 1
        portrait_verb: int = 102 + character_to_internal_actor_id[character]

        try:
            self.scumm_process.start_script(input_script, verb_click, portrait_verb)
        except Exception:
            return False

        return True

    def free_laverne_from_the_tree(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        laverne_in_the_tree_object_id: int = 599
        laverne_actor_id: int = 2
        kennel_room_id: int = 51
        laverne_portrait_flag: int = 177
        object_writes: Tuple[Tuple[int, int, Optional[bool]], ...] = (
            (laverne_in_the_tree_object_id, 0, None),
            (592, 0, True),
            (598, 0, True),
            (600, 1, False),
        )

        try:
            if self.scumm_process.read_object_state(laverne_in_the_tree_object_id) != 1:
                return True

            object_id: int
            state: int
            is_untouchable: Optional[bool]
            for object_id, state, is_untouchable in object_writes:
                self.scumm_process.write_object_state(object_id, state)

                if is_untouchable is not None:
                    self.scumm_process.write_object_class(object_id, 32, is_untouchable)

            self.scumm_process.put_actor(laverne_actor_id, 293, 132, kennel_room_id)
            self.scumm_process.write_bit_variable(laverne_portrait_flag, 1)
        except Exception:
            return False

        return True

    def intercept_item_pickups(self, released_items: List[DayOfTheTentacleItems]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        released_object_ids: List[int] = [item_to_internal_object_and_room_id[item][0] for item in released_items]

        try:
            self.scumm_process.release_pickups(released_object_ids)
            self.scumm_process.intercept_pickups([object_id for object_id, _ in item_to_internal_object_and_room_id.values() if object_id not in released_object_ids])
            self.scumm_process.set_pickup_rooms(list(item_to_internal_object_and_room_id.values()))
        except Exception:
            return False

        return True

    def restore_consumed_items(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        room_owner: int = 15
        parked_owner: int = 14
        character_owners: Tuple[int, ...] = (1, 2, 3)
        starting_object_ids: List[int] = [item_to_internal_object_and_room_id[item][0] for item in items_removed_when_a_save_is_set_up]
        hamster_object_id: int = item_to_internal_object_and_room_id[DayOfTheTentacleItems.HAMSTER][0]

        try:
            consumed_object_ids: List[int] = list()

            object_id: int
            for object_id in self.scumm_process.read_intercepted_pickups():
                if object_id in starting_object_ids:
                    continue

                owner: int = self.scumm_process.read_object_owner(object_id)

                if owner in (room_owner,) + character_owners:
                    continue

                if owner == parked_owner and object_id == hamster_object_id:
                    continue

                if object_id not in self.consumed_object_ids:
                    consumed_object_ids.append(object_id)

                    continue

                self.scumm_process.write_object_owner(object_id, room_owner)

                if object_id not in self.restored_object_ids:
                    self.restored_object_ids.append(object_id)

            self.consumed_object_ids = consumed_object_ids
        except Exception:
            return False

        return True

    def return_retaken_items(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.character is None:
            return False

        consumed_owner: int = 0
        room_owner: int = 15

        try:
            checked_object_ids: List[int] = self.scumm_process.read_checked_pickups()

            item: DayOfTheTentacleItems
            for item in self.game_state.granted_items:
                object_id: int = item_to_internal_object_and_room_id[item][0]

                if object_id not in checked_object_ids or object_id in self.object_ids_checked_by_the_client:
                    continue

                if self.scumm_process.read_object_owner(object_id) != room_owner:
                    continue

                if object_id in self.restored_object_ids:
                    self.scumm_process.write_object_owner(object_id, consumed_owner)
                    self.restored_object_ids.remove(object_id)
                else:
                    self.receive_item(item)
        except Exception:
            return False

        return True

    def check_pickups_left_unreachable(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        hammers_swapped_flag: int = 31
        right_handed_hammer_object_id: int = 149
        blanket_available_flag: int = 11
        washington_progress_variable: int = 216
        quill_pen_taken_progress: int = 6
        blanket_object_id: int = 88
        crank_object_id: int = 401

        try:
            intercepted_object_ids: List[int] = self.scumm_process.read_intercepted_pickups()
            unreachable_object_ids: List[int] = list()

            if self.scumm_process.read_bit_variable(hammers_swapped_flag):
                unreachable_object_ids.append(right_handed_hammer_object_id)

            if self.scumm_process.read_variable(washington_progress_variable) >= quill_pen_taken_progress and not self.scumm_process.read_bit_variable(blanket_available_flag):
                unreachable_object_ids.append(blanket_object_id)

            if DayOfTheTentacleEvents.ATTACHED_CRANK_TO_CRANK_BOX in self.game_state.events:
                unreachable_object_ids.append(crank_object_id)

            object_ids_to_check: List[int] = [object_id for object_id in unreachable_object_ids if object_id in intercepted_object_ids]

            self.scumm_process.check_pickups(object_ids_to_check)
            self.object_ids_checked_by_the_client.extend(object_ids_to_check)
        except Exception:
            return False

        return True

    def receive_item(self, item: DayOfTheTentacleItems) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.character is None:
            return False

        object_id: int
        room_id: int
        object_id, room_id = item_to_internal_object_and_room_id[item]

        classes_to_set: Tuple[int, ...] = (25, 2) if item in (DayOfTheTentacleItems.CRANK, DayOfTheTentacleItems.FLAG) else (25,)

        item_to_flag_id_set_on_receipt: Dict[DayOfTheTentacleItems, int] = {
            DayOfTheTentacleItems.SPAGHETTI: 64,
            DayOfTheTentacleItems.SWISS_BANKBOOK: 38,
        }

        item_to_name_set_on_receipt: Dict[DayOfTheTentacleItems, bytes] = {
            DayOfTheTentacleItems.CHATTERING_TEETH: b"chattering teeth",
            DayOfTheTentacleItems.SPAGHETTI: b"wet soggy noodles",
        }

        inventory_state: Optional[int] = None

        try:
            if object_id in self.scumm_process.read_checked_pickups():
                inventory_state = 0 if item in items_received_with_state_zero else 1

            self.scumm_process.give_object(object_id, room_id, classes_to_set=classes_to_set, state=inventory_state)

            if item in item_to_flag_id_set_on_receipt:
                self.scumm_process.write_bit_variable(item_to_flag_id_set_on_receipt[item], 1)

            if item in item_to_name_set_on_receipt:
                self.scumm_process.set_object_name(object_id, item_to_name_set_on_receipt[item])

            self.scumm_process.write_bit_variable(item_to_internal_granted_flag_id[item], 1)
        except Exception:
            return False

        return True

    def remove_item(self, item: DayOfTheTentacleItems) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        object_id: int = item_to_internal_object_and_room_id[item][0]

        try:
            self.scumm_process.remove_object(object_id)
        except Exception:
            return False

        return True

    def hide_items(self, items: List[DayOfTheTentacleItems]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        try:
            item: DayOfTheTentacleItems
            for item in items:
                self.scumm_process.set_object_hidden(item_to_internal_object_and_room_id[item][0], True)

                object_id: int
                for object_id in item_to_internal_object_ids_hidden_with_it.get(item, tuple()):
                    self.scumm_process.set_object_hidden(object_id, True)

                for object_id in item_to_internal_object_ids_redrawn_without_it.get(item, tuple()):
                    self.scumm_process.write_object_state(object_id, 1)
        except Exception:
            return False

        return True

    def show_items(self, items: List[DayOfTheTentacleItems]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        try:
            checked_object_ids: List[int] = self.scumm_process.read_checked_pickups()

            item: DayOfTheTentacleItems
            for item in items:
                object_id: int = item_to_internal_object_and_room_id[item][0]

                if object_id in checked_object_ids:
                    continue

                self.scumm_process.set_object_hidden(object_id, False)

                for object_id in item_to_internal_object_ids_hidden_with_it.get(item, tuple()):
                    self.scumm_process.set_object_hidden(object_id, False)

                for object_id in item_to_internal_object_ids_redrawn_without_it.get(item, tuple()):
                    self.scumm_process.write_object_state(object_id, 0)
        except Exception:
            return False

        return True

    def block_leaving_the_basement_lab(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        walk_to_verb: int = 11
        stairs_object_id: int = 215

        try:
            self.scumm_process.block_sentences([(walk_to_verb, stairs_object_id, 0)])

            verb: int
            object_a: int
            object_b: int
            for verb, object_a, object_b in self.scumm_process.read_new_sentences():
                if verb == walk_to_verb and object_a == stairs_object_id:
                    self.scumm_process.say(b"Hold on. The plans have to be down here somewhere. I'd better search the lab before I go wandering off.")
        except Exception:
            return False

        return True

    def block_guarded_sentences(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        send_verb: int = 18
        use_verb: int = 7
        push_verb: int = 6
        pull_verb: int = 5
        attached_crank_object_id: int = 584
        blanket_object_id: int = 88
        chimney_object_id: int = 168
        flag_object_id: int = 586
        disguise_flag: int = 16
        washington_progress_variable: int = 216
        laverne_actor_id: int = 2
        finale_flag: int = 186
        contract_object_id: int = 347
        stamp_object_id: int = 439
        mailbox_object_id: int = 24
        dr_fred_object_id: int = 222
        story_stage_variable: int = 223
        dr_fred_in_his_office_story_stage: int = 37
        flag_gun_object_id: int = 252
        cigar_lighter_object_id: int = 187
        novelty_shop_room_id: int = 26

        sentences: List[Tuple[int, int, int]] = [(send_verb, item_to_internal_object_and_room_id[item][0], 0) for item in items_sent_between_characters_by_the_client]

        try:
            if self.scumm_process.read_bit_variable(disguise_flag):
                sentences.append((use_verb, attached_crank_object_id, 0))
                sentences.append((push_verb, attached_crank_object_id, 0))
                sentences.append((pull_verb, attached_crank_object_id, 0))

            if self.scumm_process.read_variable(washington_progress_variable) < 4:
                sentences.append((use_verb, blanket_object_id, chimney_object_id))
                sentences.append((use_verb, chimney_object_id, blanket_object_id))

            if self.scumm_process.read_ego() != laverne_actor_id:
                sentences.append((use_verb, flag_object_id, 0))

            if self.scumm_process.read_variable(story_stage_variable) == dr_fred_in_his_office_story_stage:
                sentences.append((use_verb, contract_object_id, stamp_object_id))
                sentences.append((use_verb, contract_object_id, mailbox_object_id))
                sentences.append((use_verb, contract_object_id, dr_fred_object_id))

            if self.scumm_process.read_current_room() != novelty_shop_room_id:
                sentences.append((use_verb, flag_gun_object_id, cigar_lighter_object_id))
                sentences.append((use_verb, cigar_lighter_object_id, flag_gun_object_id))

            powered_count: int = sum(self.scumm_process.read_bit_variable(flag_id) for flag_id, _ in chron_o_johns_powered_before_the_finale)

            if powered_count == len(chron_o_johns_powered_before_the_finale) - 1 and not self.scumm_process.read_bit_variable(finale_flag):
                flag_id: int
                powering_sentences: Tuple[Tuple[int, int, int], ...]
                for flag_id, powering_sentences in chron_o_johns_powered_before_the_finale:
                    if not self.scumm_process.read_bit_variable(flag_id):
                        sentences.extend(powering_sentences)

            self.scumm_process.block_sentences(sentences)
            self.blocked_sentences = sentences
        except Exception:
            return False

        return True

    def complete_blocked_sentences(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        send_verb: int = 18
        used_with_verb: int = 13
        attached_crank_object_id: int = 584
        blanket_object_id: int = 88
        flag_object_id: int = 586
        laverne_actor_id: int = 2
        undisguised_laverne_costume: int = 303
        save_slot: int = 9
        give_verb: int = 80
        contract_object_id: int = 347
        stamp_object_id: int = 439
        mailbox_object_id: int = 24
        dr_fred_object_id: int = 222
        flag_gun_object_id: int = 252
        cigar_lighter_object_id: int = 187
        contract_state_variable: int = 221
        contract_stamped_state: int = 1
        contract_mailed_state: int = 2
        contract_signed_flag: int = 37
        mailing_script: int = 7
        sent_object_ids: List[int] = [item_to_internal_object_and_room_id[item][0] for item in items_sent_between_characters_by_the_client]

        try:
            verb: int
            object_a: int
            object_b: int
            for verb, object_a, object_b in self.scumm_process.read_new_sentences():
                if not any(verb == blocked_verb and object_a == blocked_a and object_b in (blocked_b, object_b if blocked_b == 0 else None) for blocked_verb, blocked_a, blocked_b in self.blocked_sentences):
                    continue

                if any((verb, object_a, object_b) in powering_sentences or (verb, object_a, 0) in powering_sentences for _, powering_sentences in chron_o_johns_powered_before_the_finale):
                    self.finale_sentence_waiting_for_the_save = (verb, object_a, object_b)
                    self.scumm_process.request_save(save_slot, "AP Before Finale")
                elif verb == send_verb and object_a in sent_object_ids and object_b in internal_actor_id_to_character:
                    self.scumm_process.transfer_object(object_a, object_b)
                elif object_a == attached_crank_object_id:
                    self.scumm_process.set_actor_costume(laverne_actor_id, undisguised_laverne_costume)
                    self.scumm_process.start_object(attached_crank_object_id, used_with_verb, 0, verb)
                elif object_a == blanket_object_id or object_b == blanket_object_id:
                    self.scumm_process.say(b"I don't want to smoke anyone out just yet.")
                elif object_a == flag_object_id:
                    self.scumm_process.say(b"That's Laverne's size, not mine.")
                elif object_a == contract_object_id and object_b == stamp_object_id:
                    self.scumm_process.remove_object(stamp_object_id)
                    self.scumm_process.write_variable(contract_state_variable, contract_stamped_state)
                elif object_a == contract_object_id and object_b == mailbox_object_id:
                    if self.scumm_process.read_variable(contract_state_variable) != contract_stamped_state:
                        self.scumm_process.say(b"I doubt they'll take it without a stamp.")
                    elif not self.scumm_process.read_bit_variable(contract_signed_flag):
                        self.scumm_process.say(b"This is no good. It isn't signed.")
                    else:
                        self.scumm_process.write_variable(contract_state_variable, contract_mailed_state)
                        self.scumm_process.start_script(mailing_script)
                elif (object_a, object_b) in ((flag_gun_object_id, cigar_lighter_object_id), (cigar_lighter_object_id, flag_gun_object_id)):
                    self.scumm_process.say(b"I'd better not play with those here.")
                elif object_a == contract_object_id and object_b == dr_fred_object_id:
                    self.scumm_process.do_sentence(give_verb, dr_fred_object_id, contract_object_id)

            if self.finale_sentence_waiting_for_the_save is not None and not self.scumm_process.is_save_or_load_pending():
                self.scumm_process.do_sentence(*self.finale_sentence_waiting_for_the_save)

                self.finale_sentence_waiting_for_the_save = None
        except Exception:
            return False

        return True

    def block_guarded_scripts(self, diamond_order_refusal: Optional[bytes]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        tree_chopping_script: int = 19
        phone_call_script: int = 49
        diamond_needed_flag: int = 39
        diamond_ordered_flag: int = 331

        scripts: List[int] = [tree_chopping_script]

        self.diamond_order_refusal = diamond_order_refusal

        try:
            if diamond_order_refusal is not None:
                if self.scumm_process.read_bit_variable(diamond_needed_flag) and not self.scumm_process.read_bit_variable(diamond_ordered_flag):
                    scripts.append(phone_call_script)

            self.scumm_process.block_scripts(scripts)
        except Exception:
            return False

        return True

    def complete_refused_scripts(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        tree_chopping_script: int = 19
        phone_call_script: int = 49
        tree_painted_flag: int = 12
        tree_chopped_down_flag: int = 188
        washington_actor_id: int = 8
        object_writes: Tuple[Tuple[int, int, Optional[bool]], ...] = (
            (52, 1, True),
            (57, 1, False),
            (93, 1, None),
            (94, 0, None),
            (36, 1, True),
        )

        try:
            script: int
            for script in self.scumm_process.read_new_refused_script_starts():
                if script == tree_chopping_script:
                    object_id: int
                    state: int
                    is_untouchable: Optional[bool]
                    for object_id, state, is_untouchable in object_writes:
                        self.scumm_process.write_object_state(object_id, state)

                        if is_untouchable is not None:
                            self.scumm_process.write_object_class(object_id, 32, is_untouchable)

                    self.scumm_process.put_actor(washington_actor_id, 0, 0, 0)
                    self.scumm_process.write_bit_variable(tree_painted_flag, 0)
                    self.scumm_process.write_bit_variable(tree_chopped_down_flag, 1)
                    self.scumm_process.call_opcode("o6_stopSound", 17)
                    self.scumm_process.start_script(128)
                elif script == phone_call_script and self.diamond_order_refusal is not None:
                    self.scumm_process.say(self.diamond_order_refusal)
        except Exception:
            return False

        return True

    def keep_laverne_disguised(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        disguise_flag: int = 16
        laverne_actor_id: int = 2
        undisguised_laverne_costume: int = 303
        disguised_laverne_costume: int = 284

        try:
            if not self.scumm_process.read_bit_variable(disguise_flag):
                return True

            if self.scumm_process.read_actor_costume(laverne_actor_id) == undisguised_laverne_costume:
                self.scumm_process.set_actor_costume(laverne_actor_id, disguised_laverne_costume)
        except Exception:
            return False

        return True

    def keep_the_battery_charged(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        battery_charge_variable: int = 215
        on_the_kite_charge: int = 5
        red_lab_room_id: int = 16
        charge_setting_scripts: Tuple[int, ...] = (210, 212)

        try:
            battery_charge: int = self.scumm_process.read_variable(battery_charge_variable)
            previous_battery_charge: Optional[int] = self.previous_battery_charge

            is_charge_being_reset: bool = (
                self.scumm_process.read_current_room() == red_lab_room_id
                and any(script in charge_setting_scripts for script in self.scumm_process.read_running_scripts())
            )

            if is_charge_being_reset and previous_battery_charge is not None and previous_battery_charge >= on_the_kite_charge > battery_charge:
                self.scumm_process.write_variable(battery_charge_variable, previous_battery_charge)

                return True

            self.previous_battery_charge = battery_charge
        except Exception:
            return False

        return True

    def keep_the_coffee_pots_paired(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        coffee_object_id: int = 197
        decaf_coffee_object_id: int = 198
        taken_state: int = 1
        both_taken_state: int = 2

        try:
            pot_states: Tuple[int, int] = (self.scumm_process.read_object_state(coffee_object_id), self.scumm_process.read_object_state(decaf_coffee_object_id))

            if min(pot_states) >= taken_state and pot_states != (both_taken_state, both_taken_state):
                self.scumm_process.write_object_state(coffee_object_id, both_taken_state)
                self.scumm_process.write_object_state(decaf_coffee_object_id, both_taken_state)
        except Exception:
            return False

        return True

    def bring_back_the_name_tag_tentacle(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        main_hall_room_id: int = 52
        contestants_upstairs_flag: int = 103
        name_tag_object_id: int = 533
        tentacle_actor_id: int = 7
        tentacle_object_id: int = 534

        try:
            if self.scumm_process.read_current_room() != main_hall_room_id:
                return True

            if not self.scumm_process.read_bit_variable(contestants_upstairs_flag):
                return True

            if name_tag_object_id in self.scumm_process.read_checked_pickups():
                return True

            if self.scumm_process.read_actor_room(tentacle_actor_id) == main_hall_room_id:
                return True

            self.scumm_process.run_actor_operations(tentacle_actor_id, [
                ("default",),
                ("costume", 263),
                ("talk_color", 217),
                ("palette", 1, 217),
                ("palette", 2, 219),
                ("palette", 4, 222),
                ("palette", 5, 225),
                ("ignore_boxes",),
                ("always_zclip", 2),
            ])

            self.scumm_process.put_actor(tentacle_actor_id, 349, 106, main_hall_room_id)
            self.scumm_process.animate_actor(tentacle_actor_id, 249)
            self.scumm_process.write_object_class(tentacle_object_id, 32, False)
        except Exception:
            return False

        return True

    def show_the_attic_rope_under_a_raised_ted(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        attic_room_id: int = 39
        rope_on_the_bed_flag: int = 329
        hanging_ted_object_id: int = 381
        rope_actor_id: int = 12
        attic_setup_script: int = 212

        try:
            if self.scumm_process.read_current_room() != attic_room_id:
                return True

            is_ted_hanging: bool = not self.scumm_process.read_object_class_table()[hanging_ted_object_id] >> 31 & 1
            is_rope_on_the_bed: bool = bool(self.scumm_process.read_bit_variable(rope_on_the_bed_flag))
            is_rope_drawn: bool = self.scumm_process.read_actor_room(rope_actor_id) == attic_room_id

            if is_ted_hanging and is_rope_on_the_bed and not is_rope_drawn:
                self.scumm_process.run_actor_operations(rope_actor_id, [
                    ("default",),
                    ("costume", 219),
                    ("ignore_boxes",),
                    ("never_zclip",),
                    ("scale", 255),
                    ("elevation", -11),
                ])

                self.scumm_process.animate_actor(rope_actor_id, 250)
                self.scumm_process.put_actor(rope_actor_id, 156, 93, attic_room_id)

            if is_rope_drawn and not is_rope_on_the_bed:
                self.scumm_process.put_actor(rope_actor_id, 0, 0, 0)
                self.scumm_process.start_script(attic_setup_script)
        except Exception:
            return False

        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        try:
            if not self.scumm_process.is_engine_current() or self.scumm_process.read_game_id() != self.game_id:
                self.close_process_handle()
                self.open_process_handle()

                return GameState(is_valid=False)

            story_progress_variable: int = 223
            hoagie_portrait_flag: int = 176
            finale_flag: int = 186

            is_in_intro: bool = self.scumm_process.read_variable(story_progress_variable) == 999 or (
                not self.scumm_process.read_bit_variable(hoagie_portrait_flag) and not self.scumm_process.read_bit_variable(finale_flag)
            )

            internal_room_id: int = self.scumm_process.read_current_room()

            if internal_room_id == 0:
                return GameState(is_valid=False)

            internal_actor_id: int = self.scumm_process.read_ego()

            is_active_character_in_room: bool = self.scumm_process.read_actor_room(internal_actor_id) == internal_room_id or internal_room_id_to_room.get(internal_room_id) == DayOfTheTentacleRooms.PRESENT_VCR_CONTROLS

            variables: Tuple[int, ...] = self.scumm_process.read_variables()
            flags: bytes = self.scumm_process.read_bit_variables()
            object_owners: bytes = self.scumm_process.read_object_owner_table()
            object_states: bytes = self.scumm_process.read_object_state_table()
            object_classes: Tuple[int, ...] = self.scumm_process.read_object_class_table()

            character_rooms: Dict[DayOfTheTentacleCharacters, Optional[DayOfTheTentacleRooms]] = {
                character: internal_room_id_to_room.get(self.scumm_process.read_actor_room(actor_id))
                for actor_id, character in internal_actor_id_to_character.items()
            }

            spoken_internal_voice_ids: List[int] = self.scumm_process.read_new_voice_ids()
            checked_object_ids: List[int] = self.scumm_process.read_checked_pickups()
        except Exception:
            return GameState(is_valid=False)

        events: List[DayOfTheTentacleEvents] = list()
        condition_values: List[int] = list()

        event: DayOfTheTentacleEvents
        event_conditions: Tuple[DayOfTheTentacleConditionData, ...]
        for event, event_conditions in event_to_conditions.items():
            condition: DayOfTheTentacleConditionData
            for condition in event_conditions:
                condition_value: int = 0

                if condition.kind == DayOfTheTentacleConditionKinds.FLAG:
                    condition_value = flags[condition.internal_id >> 3] >> (condition.internal_id & 7) & 1
                elif condition.kind == DayOfTheTentacleConditionKinds.VARIABLE:
                    condition_value = variables[condition.internal_id]
                elif condition.kind == DayOfTheTentacleConditionKinds.OBJECT_OWNER:
                    condition_value = object_owners[condition.internal_id]
                elif condition.kind == DayOfTheTentacleConditionKinds.OBJECT_STATE:
                    condition_value = object_states[condition.internal_id]
                elif condition.kind == DayOfTheTentacleConditionKinds.OBJECT_CLASS:
                    is_class_set: bool = bool(object_classes[condition.internal_id] >> (abs(condition.value) - 1) & 1)
                    condition_value = abs(condition.value) if is_class_set else -abs(condition.value)
                elif condition.kind == DayOfTheTentacleConditionKinds.VOICE_LINE:
                    condition_value = int(condition.internal_id in spoken_internal_voice_ids)

                is_condition_met: bool = condition_value == condition.value

                if condition.is_minimum:
                    is_condition_met = condition_value >= condition.value

                if condition.previous_value is not None:
                    if self.previous_condition_values is None:
                        is_condition_met = False
                    elif self.previous_condition_values[len(condition_values)] != condition.previous_value:
                        is_condition_met = False

                if is_condition_met and event not in events:
                    events.append(event)

                condition_values.append(condition_value)

        self.previous_condition_values = tuple(condition_values)

        is_save_set_up: bool = bool(flags[save_is_set_up_internal_flag_id >> 3] >> (save_is_set_up_internal_flag_id & 7) & 1)

        granted_items: List[DayOfTheTentacleItems] = list()

        item: DayOfTheTentacleItems
        internal_flag_id: int
        for item, internal_flag_id in item_to_internal_granted_flag_id.items():
            if flags[internal_flag_id >> 3] >> (internal_flag_id & 7) & 1:
                granted_items.append(item)

        picked_up_items: List[DayOfTheTentacleItems] = list()

        object_id: int
        for item, (object_id, _) in item_to_internal_object_and_room_id.items():
            if object_id in checked_object_ids:
                picked_up_items.append(item)

        held_items: List[DayOfTheTentacleItems] = list()

        for item, (object_id, _) in item_to_internal_object_and_room_id.items():
            if object_owners[object_id] == internal_actor_id:
                held_items.append(item)

        spoken_voice_lines: List[DayOfTheTentacleVoiceLines] = list()

        voice_line: DayOfTheTentacleVoiceLines
        internal_voice_id: int
        for voice_line, internal_voice_id in voice_line_to_internal_voice_id.items():
            if internal_voice_id in spoken_internal_voice_ids:
                spoken_voice_lines.append(voice_line)

        return GameState(
            is_valid=True,
            is_in_intro=is_in_intro,
            is_save_set_up=is_save_set_up,
            room=internal_room_id_to_room.get(internal_room_id) if is_active_character_in_room else None,
            character=internal_actor_id_to_character.get(internal_actor_id),
            character_rooms=character_rooms,
            events=tuple(events),
            granted_items=tuple(granted_items),
            picked_up_items=tuple(picked_up_items),
            held_items=tuple(held_items),
            spoken_voice_lines=tuple(spoken_voice_lines),
        )
