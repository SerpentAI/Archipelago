from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Union

import enum

from ..enums import (
    TES3APItems,
    TES3APRegions,
    TES3APTags,
    TES3APTasks,
    TES3FreeableSlaves,
    TES3Harvestables,
)


class TES3LocationData(NamedTuple):
    name: str
    archipelago_id: Optional[int]
    region: TES3APRegions
    requirements: Optional[Any] = None
    tags: Optional[Tuple[TES3APTags, ...]] = None


location_data: Dict[
    TES3APTasks,
    Dict[enum.Enum, Dict[enum.Enum, List[TES3LocationData]]],
] = dict()


# Each task type / location group gets a distinct, large enough offset to work with
# The last digit of the resulting ID should ALWAYS be zero, leaving room for additional copies of the same locations


# Task: Free Slaves
offset = 10000

location_data = location_data | {
    TES3APTasks.FREE_SLAVE: {
        TES3FreeableSlaves.ADHARANJI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ADHARANJI.value}",
            archipelago_id=offset + 0,
            region=TES3APRegions.KUDANAT,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHAHT: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHAHT.value}",
            archipelago_id=offset + 10,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHDNI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHDNI.value}",
            archipelago_id=offset + 20,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHDRI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHDRI.value}",
            archipelago_id=offset + 30,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHJARA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHJARA.value}",
            archipelago_id=offset + 40,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHNARRA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHNARRA.value}",
            archipelago_id=offset + 50,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHNDAHRA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHNDAHRA.value}",
            archipelago_id=offset + 60,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHNISA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHNISA.value}",
            archipelago_id=offset + 70,
            region=TES3APRegions.ZAINSIPILU,
            requirements=(
                "COMBAT:9",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AHZINI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AHZINI.value}",
            archipelago_id=offset + 80,
            region=TES3APRegions.DREN_PLANTATION_SHIPPING_HOUSE,
            requirements=(
                "COMBAT:22",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AH_MEESEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AH_MEESEI.value}",
            archipelago_id=offset + 90,
            region=TES3APRegions.KUDANAT,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AINA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AINA.value}",
            archipelago_id=offset + 100,
            region=TES3APRegions.HABINBAES,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AKISH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AKISH.value}",
            archipelago_id=offset + 110,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.AM_RA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.AM_RA.value}",
            archipelago_id=offset + 120,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ANJARI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ANJARI.value}",
            archipelago_id=offset + 130,
            region=TES3APRegions.ZAINSIPILU,
            requirements=(
                "COMBAT:9",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ARABHI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ARABHI.value}",
            archipelago_id=offset + 140,
            region=TES3APRegions.DREN_PLANTATION_SHIPPING_HOUSE,
            requirements=(
                "COMBAT:22",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ARAVI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ARAVI.value}",
            archipelago_id=offset + 150,
            region=TES3APRegions.AHARUNARTUS,
            requirements=(
                "COMBAT:5",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ASHIDASHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ASHIDASHA.value}",
            archipelago_id=offset + 160,
            region=TES3APRegions.SHUSHAN,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ASUM: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ASUM.value}",
            archipelago_id=offset + 170,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BAADARGO: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BAADARGO.value}",
            archipelago_id=offset + 180,
            region=TES3APRegions.ADDAMASARTUS,
            requirements=(
                "COMBAT:2",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BAHDAHNA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BAHDAHNA.value}",
            archipelago_id=offset + 190,
            region=TES3APRegions.AHARUNARTUS,
            requirements=(
                "COMBAT:5",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BAHDRASHI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BAHDRASHI.value}",
            archipelago_id=offset + 200,
            region=TES3APRegions.ZAINSIPILU,
            requirements=(
                "COMBAT:9",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BANALZ: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BANALZ.value}",
            archipelago_id=offset + 210,
            region=TES3APRegions.ADDAMASARTUS,
            requirements=(
                "COMBAT:2",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BEEKATAN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BEEKATAN.value}",
            archipelago_id=offset + 220,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BHUSARI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BHUSARI.value}",
            archipelago_id=offset + 230,
            region=TES3APRegions.SHUSHAN,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BUNISH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BUNISH.value}",
            archipelago_id=offset + 240,
            region=TES3APRegions.SHUSHAN,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.BUN_TEEMEETA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.BUN_TEEMEETA.value}",
            archipelago_id=offset + 250,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.CHALUREEL: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.CHALUREEL.value}",
            archipelago_id=offset + 260,
            region=TES3APRegions.ZEBABI,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.CHEESH_MEEUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.CHEESH_MEEUS.value}",
            archipelago_id=offset + 270,
            region=TES3APRegions.HINNABI,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.CHIWISH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.CHIWISH.value}",
            archipelago_id=offset + 280,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DAHLEENA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DAHLEENA.value}",
            archipelago_id=offset + 290,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DAHNARA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DAHNARA.value}",
            archipelago_id=offset + 300,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DAN_RU: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DAN_RU.value}",
            archipelago_id=offset + 310,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DEESH_MEEUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DEESH_MEEUS.value}",
            archipelago_id=offset + 320,
            region=TES3APRegions.SHUSHISHI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DREADED_WATER: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DREADED_WATER.value}",
            archipelago_id=offset + 330,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DRO_QANAR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DRO_QANAR.value}",
            archipelago_id=offset + 340,
            region=TES3APRegions.VIVEC_TELVANNI_CANALWORKS,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.DRO_ZAH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.DRO_ZAH.value}",
            archipelago_id=offset + 350,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.EKAPI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.EKAPI.value}",
            archipelago_id=offset + 360,
            region=TES3APRegions.PANAT,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ELEEDAL_LEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ELEEDAL_LEI.value}",
            archipelago_id=offset + 370,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.EL_LURASHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.EL_LURASHA.value}",
            archipelago_id=offset + 380,
            region=TES3APRegions.VIVEC_TELVANNI_CANALWORKS,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.EUTEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.EUTEI.value}",
            archipelago_id=offset + 390,
            region=TES3APRegions.SATURAN,
            requirements=(
                "COMBAT:16",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.GAH_JULAN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.GAH_JULAN.value}",
            archipelago_id=offset + 400,
            region=TES3APRegions.DREN_PLANTATION_SHIPPING_HOUSE,
            requirements=(
                "COMBAT:22",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.GIH_JA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.GIH_JA.value}",
            archipelago_id=offset + 410,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.GISH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.GISH.value}",
            archipelago_id=offset + 420,
            region=TES3APRegions.ZEBABI,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.GILM: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.GILM.value}",
            archipelago_id=offset + 430,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HAN_TULM: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HAN_TULM.value}",
            archipelago_id=offset + 440,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HARAN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HARAN.value}",
            archipelago_id=offset + 450,
            region=TES3APRegions.ZAINSIPILU,
            requirements=(
                "COMBAT:9",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HARASSA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HARASSA.value}",
            archipelago_id=offset + 460,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HEEDUL: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HEEDUL.value}",
            archipelago_id=offset + 470,
            region=TES3APRegions.KUDANAT,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HEIR_ZISH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HEIR_ZISH.value}",
            archipelago_id=offset + 480,
            region=TES3APRegions.HINNABI,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HIDES_HIS_FOOT: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HIDES_HIS_FOOT.value}",
            archipelago_id=offset + 490,
            region=TES3APRegions.DREN_PLANTATION_SHIPPING_HOUSE,
            requirements=(
                "COMBAT:22",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.HUZEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.HUZEI.value}",
            archipelago_id=offset + 500,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.IDHASSI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.IDHASSI.value}",
            archipelago_id=offset + 510,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.INERRI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.INERRI.value}",
            archipelago_id=offset + 520,
            region=TES3APRegions.VIVEC_TELVANNI_CANALWORKS,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.INORRA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.INORRA.value}",
            archipelago_id=offset + 530,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.JEED_EI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.JEED_EI.value}",
            archipelago_id=offset + 540,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.JEER_MAHT: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.JEER_MAHT.value}",
            archipelago_id=offset + 550,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.J_DATO: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.J_DATO.value}",
            archipelago_id=offset + 560,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.J_JARSHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.J_JARSHA.value}",
            archipelago_id=offset + 570,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.J_RAKSA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.J_RAKSA.value}",
            archipelago_id=offset + 580,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.J_RAM_DAR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.J_RAM_DAR.value}",
            archipelago_id=offset + 590,
            region=TES3APRegions.HINNABI,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.J_ZAMHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.J_ZAMHA.value}",
            archipelago_id=offset + 600,
            region=TES3APRegions.SATURAN,
            requirements=(
                "COMBAT:16",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KAASHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KAASHA.value}",
            archipelago_id=offset + 610,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KHAZURA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KHAZURA.value}",
            archipelago_id=offset + 620,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KISEENA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KISEENA.value}",
            archipelago_id=offset + 630,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KISHNI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KISHNI.value}",
            archipelago_id=offset + 640,
            region=TES3APRegions.AHARUNARTUS,
            requirements=(
                "COMBAT:5",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KISIMBA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KISIMBA.value}",
            archipelago_id=offset + 650,
            region=TES3APRegions.HABINBAES,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.KISISA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.KISISA.value}",
            archipelago_id=offset + 660,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MA_JIDARR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MA_JIDARR.value}",
            archipelago_id=offset + 670,
            region=TES3APRegions.SHUSHISHI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MA_KHAR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MA_KHAR.value}",
            archipelago_id=offset + 680,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MA_ZAHN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MA_ZAHN.value}",
            archipelago_id=offset + 690,
            region=TES3APRegions.ZEBABI,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MEEH_MEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MEEH_MEI.value}",
            archipelago_id=offset + 700,
            region=TES3APRegions.SHUSHISHI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MEEN_SA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MEEN_SA.value}",
            archipelago_id=offset + 710,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MEER: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MEER.value}",
            archipelago_id=offset + 720,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MILAH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MILAH.value}",
            archipelago_id=offset + 730,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MIM_JEEN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MIM_JEEN.value}",
            archipelago_id=offset + 740,
            region=TES3APRegions.VIVEC_TELVANNI_CANALWORKS,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.MUZ_RA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.MUZ_RA.value}",
            archipelago_id=offset + 750,
            region=TES3APRegions.ZAINSIPILU,
            requirements=(
                "COMBAT:9",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.M_SHAN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.M_SHAN.value}",
            archipelago_id=offset + 760,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NAKUMA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NAKUMA.value}",
            archipelago_id=offset + 770,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NAM_LA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NAM_LA.value}",
            archipelago_id=offset + 780,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NEESHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NEESHA.value}",
            archipelago_id=offset + 790,
            region=TES3APRegions.CALDERA_MINING_BUNKHOUSE,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NEETINEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NEETINEI.value}",
            archipelago_id=offset + 800,
            region=TES3APRegions.DREN_PLANTATION_SHIPPING_HOUSE,
            requirements=(
                "COMBAT:22",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NISABA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NISABA.value}",
            archipelago_id=offset + 810,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.NURALG: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.NURALG.value}",
            archipelago_id=offset + 820,
            region=TES3APRegions.ZEBABI,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.OKAW: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.OKAW.value}",
            archipelago_id=offset + 830,
            region=TES3APRegions.ADDAMASARTUS,
            requirements=(
                "COMBAT:2",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.OLANK_NEEUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.OLANK_NEEUS.value}",
            archipelago_id=offset + 840,
            region=TES3APRegions.HABINBAES,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.OLEEN_GEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.OLEEN_GEI.value}",
            archipelago_id=offset + 850,
            region=TES3APRegions.KUDANAT,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.OLINK_NUR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.OLINK_NUR.value}",
            archipelago_id=offset + 860,
            region=TES3APRegions.SHUSHAN,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ON_WAZEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ON_WAZEI.value}",
            archipelago_id=offset + 870,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.PEERADEEH: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.PEERADEEH.value}",
            archipelago_id=offset + 880,
            region=TES3APRegions.SATURAN,
            requirements=(
                "COMBAT:16",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RA_KARIM: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RA_KARIM.value}",
            archipelago_id=offset + 890,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RA_MHIRR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RA_MHIRR.value}",
            archipelago_id=offset + 900,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RA_SAVA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RA_SAVA.value}",
            archipelago_id=offset + 910,
            region=TES3APRegions.KUDANAT,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.REEMUKEEUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.REEMUKEEUS.value}",
            archipelago_id=offset + 920,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RI_DARSHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RI_DARSHA.value}",
            archipelago_id=offset + 930,
            region=TES3APRegions.ASSARNUD,
            requirements=(
                "COMBAT:15",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RI_DUMIWA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RI_DUMIWA.value}",
            archipelago_id=offset + 940,
            region=TES3APRegions.HABINBAES,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.RI_VASSA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.RI_VASSA.value}",
            archipelago_id=offset + 950,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.SEEN_REI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.SEEN_REI.value}",
            archipelago_id=offset + 960,
            region=TES3APRegions.ABEBAAL_EGG_MINE,
            requirements=None,
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.SHABA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.SHABA.value}",
            archipelago_id=offset + 970,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.SHIVANI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.SHIVANI.value}",
            archipelago_id=offset + 980,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.SHOLANI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.SHOLANI.value}",
            archipelago_id=offset + 990,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.SMART_SNAKE: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.SMART_SNAKE.value}",
            archipelago_id=offset + 1000,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.S_RAVERR: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.S_RAVERR.value}",
            archipelago_id=offset + 1010,
            region=TES3APRegions.MINABI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.S_RENJI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.S_RENJI.value}",
            archipelago_id=offset + 1020,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.S_VANDRA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.S_VANDRA.value}",
            archipelago_id=offset + 1030,
            region=TES3APRegions.HLORMAREN_UNDERGROUND,
            requirements=(
                "COMBAT:18",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.TANAN: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.TANAN.value}",
            archipelago_id=offset + 1040,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.TASHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.TASHA.value}",
            archipelago_id=offset + 1050,
            region=TES3APRegions.HINNABI,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.TSABHI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.TSABHI.value}",
            archipelago_id=offset + 1060,
            region=TES3APRegions.PANAT,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.TSAJADHI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.TSAJADHI.value}",
            archipelago_id=offset + 1070,
            region=TES3APRegions.SHUSHISHI,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.TSANI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.TSANI.value}",
            archipelago_id=offset + 1080,
            region=TES3APRegions.SHA_ADNIUS,
            requirements=(
                "COMBAT:13",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.UBAASI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.UBAASI.value}",
            archipelago_id=offset + 1090,
            region=TES3APRegions.SATURAN,
            requirements=(
                "COMBAT:16",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.UDARRA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.UDARRA.value}",
            archipelago_id=offset + 1100,
            region=TES3APRegions.SATURAN,
            requirements=(
                "COMBAT:16",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ULA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ULA.value}",
            archipelago_id=offset + 1110,
            region=TES3APRegions.PANAT,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.WEER: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.WEER.value}",
            archipelago_id=offset + 1120,
            region=TES3APRegions.YAKANALIT,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.WIH_EIUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.WIH_EIUS.value}",
            archipelago_id=offset + 1130,
            region=TES3APRegions.ROTHERAN_ARENA,
            requirements=(
                "COMBAT:17",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.WUD_NEEUS: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.WUD_NEEUS.value}",
            archipelago_id=offset + 1140,
            region=TES3APRegions.VIVEC_TELVANNI_CANALWORKS,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.WULEEN_SHEI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.WULEEN_SHEI.value}",
            archipelago_id=offset + 1150,
            region=TES3APRegions.AHARUNARTUS,
            requirements=(
                "COMBAT:5",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.WUSHA: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.WUSHA.value}",
            archipelago_id=offset + 1160,
            region=TES3APRegions.SINSIBADON,
            requirements=(
                "COMBAT:11",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
        TES3FreeableSlaves.ZAHRAJI: TES3LocationData(
            name=f"{TES3APTasks.FREE_SLAVE.value}: {TES3FreeableSlaves.ZAHRAJI.value}",
            archipelago_id=offset + 1170,
            region=TES3APRegions.ZEBABI,
            requirements=(
                "COMBAT:12",
            ),
            tags=(TES3APTags.TASK_FREE_SLAVE,),
        ),
    },
}

# Task: Harvest Flora
offset = 20000

location_data = location_data | {
    TES3APTasks.HARVEST_FLORA: {
        TES3Harvestables.BITTERGREEN_PLANT: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.BITTERGREEN_PLANT.value}",
            archipelago_id=offset + 0,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.BLACK_ANTHER_PLANT: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.BLACK_ANTHER_PLANT.value}",
            archipelago_id=offset + 10,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.CORKBULB: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.CORKBULB.value}",
            archipelago_id=offset + 20,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.DESERT_SWEETBARREL: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.DESERT_SWEETBARREL.value}",
            archipelago_id=offset + 30,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.FIRE_FERN: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.FIRE_FERN.value}",
            archipelago_id=offset + 40,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.FLOWERING_SWEETBARREL: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.FLOWERING_SWEETBARREL.value}",
            archipelago_id=offset + 50,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.GOLD_KANET_FLOWER: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.GOLD_KANET_FLOWER.value}",
            archipelago_id=offset + 60,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.GOLDEN_SEDGE: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.GOLDEN_SEDGE.value}",
            archipelago_id=offset + 70,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.HACKLE_LO: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.HACKLE_LO.value}",
            archipelago_id=offset + 80,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.HOLLY_BUSH: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.HOLLY_BUSH.value}",
            archipelago_id=offset + 90,
            region=TES3APRegions.SOLSTHEIM,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.HORN_LILY: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.HORN_LILY.value}",
            archipelago_id=offset + 100,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.KRESHWEED: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.KRESHWEED.value}",
            archipelago_id=offset + 110,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.MARSHMERROW: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.MARSHMERROW.value}",
            archipelago_id=offset + 120,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.MUCKSPUNGE: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.MUCKSPUNGE.value}",
            archipelago_id=offset + 130,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.NOBLE_SEDGE: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.NOBLE_SEDGE.value}",
            archipelago_id=offset + 140,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.RIPENED_BELLADONNA: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.RIPENED_BELLADONNA.value}",
            archipelago_id=offset + 150,
            region=TES3APRegions.SOLSTHEIM,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.SLOUGH_FERN: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.SLOUGH_FERN.value}",
            archipelago_id=offset + 160,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.SPINY_LLORAMOR: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.SPINY_LLORAMOR.value}",
            archipelago_id=offset + 170,
            region=TES3APRegions.MOURNHOLD,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.STONEFLOWER: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.STONEFLOWER.value}",
            archipelago_id=offset + 180,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.TRAMA_SHRUB: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.TRAMA_SHRUB.value}",
            archipelago_id=offset + 190,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.UNRIPENED_BELLADONNA: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.UNRIPENED_BELLADONNA.value}",
            archipelago_id=offset + 200,
            region=TES3APRegions.SOLSTHEIM,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.WILLOW_FLOWER: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.WILLOW_FLOWER.value}",
            archipelago_id=offset + 210,
            region=TES3APRegions.VVARDENFELL,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
        TES3Harvestables.WOLFSBANE: TES3LocationData(
            name=f"{TES3APTasks.HARVEST_FLORA.value}: {TES3Harvestables.WOLFSBANE.value}",
            archipelago_id=offset + 220,
            region=TES3APRegions.SOLSTHEIM,
            requirements=None,
            tags=(TES3APTags.TASK_HARVEST_FLORA,),
        ),
    },
}
