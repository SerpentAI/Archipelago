from typing import Dict, Optional

from rule_builder.rules import Rule, And, Has, Or

from ..enums import MirrorsEdgeAbilities, MirrorsEdgeLevelCheckpoints


level_checkpoint_rules: Dict[MirrorsEdgeLevelCheckpoints, Optional[Rule]] = {
    MirrorsEdgeLevelCheckpoints.ACTINO_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_2: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_3: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_4: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_5: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_6: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_7: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_8: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_9: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_1: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_2: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_3: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_4: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_5: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_6: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_7: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_8: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                And(
                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                ),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_9: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_10: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_11: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_12: None,
    MirrorsEdgeLevelCheckpoints.ACTINO_RISE_13: None,
    MirrorsEdgeLevelCheckpoints.ARLAND_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ARLAND_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has("Advanced Logic"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.ARLAND_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.ARLAND_4: None,
    MirrorsEdgeLevelCheckpoints.ARLAND_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ARLAND_6: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_1: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Or(
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_3: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_4: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_5: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_6: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_7: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_8: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_9: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_10: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_11: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_12: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_13: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_14: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_15: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_16: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_ONE_17: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_1: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_3: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_4: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_5: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_6: Has(
        f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"
    ),
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_7: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_10: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_11: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_12: None,
    MirrorsEdgeLevelCheckpoints.ATRIUM_TWO_13: None,
    MirrorsEdgeLevelCheckpoints.BURFIELD_1: None,
    MirrorsEdgeLevelCheckpoints.BURFIELD_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.BURFIELD_3: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.BURFIELD_4: None,
    MirrorsEdgeLevelCheckpoints.BURFIELD_5: None,
    MirrorsEdgeLevelCheckpoints.CHASE_1: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
    ),
    MirrorsEdgeLevelCheckpoints.CHASE_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has(f"Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.CHASE_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        And(
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
                Has(f"Advanced Logic"),
            ),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                And(
                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
                    Has(f"Advanced Logic"),
                )
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.CHASE_4: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.CHASE_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CHASE_6: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"
    ),
    MirrorsEdgeLevelCheckpoints.CHROMA_1: None,
    MirrorsEdgeLevelCheckpoints.CHROMA_2: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            ),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
            Has("Advanced Logic"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.CHROMA_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CHROMA_4: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                Has("Advanced Logic"),
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.CHROMA_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CHROMA_6: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_4: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has("Advanced Logic"),
        ),
        Or(
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            ),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
                Or(
                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                )
            )
        ),
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_5: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_6: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_ONE_7: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_1: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        ),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_4: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_5: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_6: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_7: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has("Advanced Logic"),
        ),
        Or(
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            ),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.CONVOY_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_4: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_6: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
            Has("Advanced Logic"),
        ),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_7: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_8: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_9: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_10: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_11: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_12: None,
    MirrorsEdgeLevelCheckpoints.CRANES_ONE_13: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_3: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_4: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_5: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_6: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_7: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.CRANES_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.EDGE_1: None,
    MirrorsEdgeLevelCheckpoints.EDGE_2: None,
    MirrorsEdgeLevelCheckpoints.EDGE_3: None,
    MirrorsEdgeLevelCheckpoints.EDGE_4: None,
    MirrorsEdgeLevelCheckpoints.EDGE_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.EDGE_6: None,
    MirrorsEdgeLevelCheckpoints.EDGE_7: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FACTORY_1: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_2: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_3: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_4: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_5: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FACTORY_6: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_7: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FACTORY_8: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_9: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_10: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_11: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_12: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_13: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_14: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_15: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_16: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FACTORY_17: None,
    MirrorsEdgeLevelCheckpoints.FACTORY_18: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_1: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_2: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_3: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.FLIGHT_5: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_6: None,
    MirrorsEdgeLevelCheckpoints.FLIGHT_7: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FLIGHT_8: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FLOW_1: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FLOW_2: None,
    MirrorsEdgeLevelCheckpoints.FLOW_3: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.FLOW_4: None,
    MirrorsEdgeLevelCheckpoints.FLOW_5: None,
    MirrorsEdgeLevelCheckpoints.FLOW_6: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.HEAT_1: Or(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.HEAT_2: None,
    MirrorsEdgeLevelCheckpoints.HEAT_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.HEAT_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.HEAT_5: None,
    MirrorsEdgeLevelCheckpoints.HEAT_6: None,
    MirrorsEdgeLevelCheckpoints.HEAT_7: None,
    MirrorsEdgeLevelCheckpoints.HEAT_8: None,
    MirrorsEdgeLevelCheckpoints.HEAT_9: None,
    MirrorsEdgeLevelCheckpoints.KINETIC_1: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.KINETIC_2: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.KINETIC_3: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.KINETIC_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Or(
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                And(
                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
                    Or(
                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                    )
                )
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.KINETIC_5: None,
    MirrorsEdgeLevelCheckpoints.KINETIC_6: None,
    MirrorsEdgeLevelCheckpoints.KINETIC_7: None,
    MirrorsEdgeLevelCheckpoints.KINETIC_8: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"
    ),
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        Or(
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            )
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_3: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_5: None,
    MirrorsEdgeLevelCheckpoints.NEW_EDEN_6: And(
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.OFFICE_1: None,
    MirrorsEdgeLevelCheckpoints.OFFICE_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_ONE_1: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_ONE_2: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
            Has("Advanced Logic"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_ONE_3: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
            Has("Advanced Logic"),
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),

    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_ONE_4: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_ONE_5: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_2: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_5: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_6: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_7: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_8: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_9: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_10: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_11: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_THREE_12: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_1: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            )
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
            )
        )
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_3: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_4: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_5: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_6: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_7: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.PLAYGROUND_TWO_10: None,
    MirrorsEdgeLevelCheckpoints.RAZZMATAZZ_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.RAZZMATAZZ_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.RAZZMATAZZ_3: None,
    MirrorsEdgeLevelCheckpoints.RAZZMATAZZ_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.RAZZMATAZZ_5: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_2: And(
        Or(
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            ),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_3: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_4: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_5: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            ),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_6: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_7: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_8: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_9: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_3: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_4: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_5: None,
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_6: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.REFLEX_REDUX_7: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_2: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_3: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_4: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_5: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
            Has("Advanced Logic"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_6: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_7: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_8: None,
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_9: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.SHARD_ONE_10: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_1: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_2: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_3: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_4: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_5: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_6: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_7: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.SHARD_TWO_10: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_1: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_2: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_3: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_4: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_5: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_6: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_7: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_8: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_9: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_10: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_11: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_12: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_13: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_14: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_ONE_15: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_1: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_2: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
        Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_3: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_4: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_5: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_6: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_7: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_THREE_8: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_1: Or(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
            Or(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
            )
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_2: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_3: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
        Has("Advanced Logic"),
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_4: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_5: Has(
        f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"
    ),
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_6: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_7: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_8: None,
    MirrorsEdgeLevelCheckpoints.STORMDRAINS_TWO_9: None,
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_1: And(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
        ),
    ),
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_2: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
        ),
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
        ),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
    ),
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_3: None,
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_4: None,
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_5: None,
    MirrorsEdgeLevelCheckpoints.SYNESTHESIA_6: None,
    MirrorsEdgeLevelCheckpoints.VELOCITY_1: And(
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
            ),
            And(
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
                Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
            )
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.VELOCITY_2: And(
        And(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
            Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
        ),
        Or(
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
            Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
        )
    ),
    MirrorsEdgeLevelCheckpoints.VELOCITY_3: None,
    MirrorsEdgeLevelCheckpoints.VELOCITY_4: None,
    MirrorsEdgeLevelCheckpoints.VELOCITY_5: None,
    MirrorsEdgeLevelCheckpoints.VELOCITY_6: Or(
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
        Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
    ),
}
