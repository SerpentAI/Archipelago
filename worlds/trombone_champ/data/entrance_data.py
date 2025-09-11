from typing import Dict, List, Tuple, Union

from ..enums import TromboneChampRegions, TromboneChampTromboners


Entrance = Tuple[TromboneChampRegions, TromboneChampRegions]

EntranceRule = Union[
    Tuple[str, ...],
    None,
]

EntranceRuleData = Dict[Entrance, EntranceRule]

entrance_rule_data: EntranceRuleData = {
    (TromboneChampRegions.CARD_COLLECTION, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.MENU, TromboneChampRegions.CARD_COLLECTION): None,
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_APPALOOSA): (
        f"TROMBONER - {TromboneChampTromboners.APPALOOSA.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_BEEZERLY): (
        f"TROMBONER - {TromboneChampTromboners.BEEZERLY.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_HORN_LORD): (
        f"TROMBONER - {TromboneChampTromboners.HORN_LORD.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_JERMAJESTY): (
        f"TROMBONER - {TromboneChampTromboners.JERMAJESTY.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_KAIZYLE_II): (
        f"TROMBONER - {TromboneChampTromboners.KAIZYLE_II.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_MELDOR): (
        f"TROMBONER - {TromboneChampTromboners.MELDOR.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_POLYGON): (
        f"TROMBONER - {TromboneChampTromboners.POLYGON.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_SERVANT_OF_BABI): (
        f"TROMBONER - {TromboneChampTromboners.SERVANT_OF_BABI.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_SODA): (
        f"TROMBONER - {TromboneChampTromboners.SODA.value}",
    ),
    (TromboneChampRegions.MENU, TromboneChampRegions.TROMBONER_TRIXIEBELL): (
        f"TROMBONER - {TromboneChampTromboners.TRIXIEBELL.value}",
    ),
    (TromboneChampRegions.TROMBONER_APPALOOSA, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_BEEZERLY, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_HORN_LORD, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_JERMAJESTY, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_KAIZYLE_II, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_MELDOR, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_POLYGON, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_SERVANT_OF_BABI, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_SODA, TromboneChampRegions.MENU): None,
    (TromboneChampRegions.TROMBONER_TRIXIEBELL, TromboneChampRegions.MENU): None,
}
