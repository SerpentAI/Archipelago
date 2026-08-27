from typing import Dict, List, Optional, Tuple

from ..enums import PoolsItems, PoolsLevels, PoolsLocations


chair_coordinates_by_level: Dict[PoolsLevels, Dict[PoolsLocations, Tuple[float, float, float]]] = {
    PoolsLevels.LEVEL_1: {
        PoolsLocations.LEVEL_1_CHAIR_1: (5.000, 0.640, -6.840),
        PoolsLocations.LEVEL_1_CHAIR_2: (-25.700, 1.640, 64.100),
        PoolsLocations.LEVEL_1_CHAIR_3: (21.592, -1.360, 88.930),
        PoolsLocations.LEVEL_1_CHAIR_4: (14.825, -1.360, 159.850),
        PoolsLocations.LEVEL_1_CHAIR_5: (49.540, -0.212, 28.398),
        PoolsLocations.LEVEL_1_CHAIR_6: (50.350, -0.211, 28.078),
    },
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_CHAIR_1: (58.900, 0.175, 188.850),
        PoolsLocations.LEVEL_2_CHAIR_2: (58.480, 0.175, 196.500),
        PoolsLocations.LEVEL_2_CHAIR_3: (-18.000, 2.640, 180.790),
        PoolsLocations.LEVEL_2_CHAIR_4: (-36.510, -2.370, 252.480),
        PoolsLocations.LEVEL_2_CHAIR_5: (-36.380, -2.370, 253.990),
        PoolsLocations.LEVEL_2_CHAIR_6: (-34.360, -2.370, 254.630),
        PoolsLocations.LEVEL_2_CHAIR_7: (-34.370, -2.370, 253.020),
        PoolsLocations.LEVEL_2_CHAIR_8: (-36.320, -2.370, 260.670),
        PoolsLocations.LEVEL_2_CHAIR_9: (-36.520, -2.370, 262.210),
        PoolsLocations.LEVEL_2_CHAIR_10: (-34.220, -2.370, 262.780),
        PoolsLocations.LEVEL_2_CHAIR_11: (-34.260, -2.370, 260.890),
        PoolsLocations.LEVEL_2_CHAIR_12: (-36.620, -2.370, 267.950),
        PoolsLocations.LEVEL_2_CHAIR_13: (-37.190, -2.370, 270.330),
        PoolsLocations.LEVEL_2_CHAIR_14: (-32.590, -2.370, 271.510),
        PoolsLocations.LEVEL_2_CHAIR_15: (-33.790, -2.370, 268.310),
        PoolsLocations.LEVEL_2_CHAIR_16: (-37.700, -2.370, 277.160),
        PoolsLocations.LEVEL_2_CHAIR_17: (-37.960, -2.370, 277.910),
        PoolsLocations.LEVEL_2_CHAIR_18: (-32.840, -2.370, 278.330),
        PoolsLocations.LEVEL_2_CHAIR_19: (-32.660, -2.370, 277.260),
        PoolsLocations.LEVEL_2_CHAIR_20: (-1.150, -0.870, 326.260),
        PoolsLocations.LEVEL_2_CHAIR_21: (-1.650, -0.870, 326.810),
        PoolsLocations.LEVEL_2_CHAIR_22: (-1.206, -0.870, 328.230),
        PoolsLocations.LEVEL_2_CHAIR_23: (-0.410, -0.870, 328.260),
        PoolsLocations.LEVEL_2_CHAIR_24: (0.140, -0.870, 326.490),
    },
    PoolsLevels.LEVEL_3: {
        # Sauna Benches are handled differently
        PoolsLocations.LEVEL_3_CHAIR_6: (168.250, 2.890, 67.110),
        PoolsLocations.LEVEL_3_CHAIR_10: (117.590, 10.420, -76.010),
    },
    PoolsLevels.LEVEL_4: dict(),  # No Chairs
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_CHAIR_1: (29.200, -2.370, 84.890),
        PoolsLocations.LEVEL_5_CHAIR_2: (29.110, 9.640, 191.190),
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_CHAIR_1: (-4.940, 3.640, -4.540),
        PoolsLocations.LEVEL_6_CHAIR_2: (-8.190, 3.640, -4.640),
        PoolsLocations.LEVEL_6_CHAIR_3: (-22.500, -15.380, 72.680),
        PoolsLocations.LEVEL_6_CHAIR_4: (-14.290, -20.380, 21.530),
        PoolsLocations.LEVEL_6_CHAIR_5: (-14.250, -20.380, 27.090),
        PoolsLocations.LEVEL_6_CHAIR_6: (-20.580, -13.380, 114.640),
        PoolsLocations.LEVEL_6_CHAIR_7: (-39.190, -13.380, 107.710),
        PoolsLocations.LEVEL_6_CHAIR_8: (-39.010, -13.380, 108.210),
        PoolsLocations.LEVEL_6_CHAIR_9: (-42.420, -13.380, 110.690),
        PoolsLocations.LEVEL_6_CHAIR_10: (62.920, -17.380, 69.530),
        PoolsLocations.LEVEL_6_CHAIR_11: (82.900, -18.380, 24.960),
        PoolsLocations.LEVEL_6_CHAIR_12: (90.380, -18.380, 24.560),
        PoolsLocations.LEVEL_6_CHAIR_13: (94.010, -18.380, 25.000),
        PoolsLocations.LEVEL_6_CHAIR_14: (99.990, -18.380, 25.010),
        PoolsLocations.LEVEL_6_CHAIR_15: (102.940, -18.380, 25.010),
        PoolsLocations.LEVEL_6_CHAIR_16: (154.160, -0.380, 20.240),
        PoolsLocations.LEVEL_6_CHAIR_17: (156.820, -0.380, 20.390),
        PoolsLocations.LEVEL_6_CHAIR_18: (181.79, 16.610, -53.520),
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_CHAIR_1: (11.190, 1.590, 1.230),
        PoolsLocations.LEVEL_0_CHAIR_2: (12.310, 1.590, 1.610),
        PoolsLocations.LEVEL_0_CHAIR_3: (3.820, 16.600, 88.110),
        PoolsLocations.LEVEL_0_CHAIR_4: (3.900, 16.600, 99.320),
        PoolsLocations.LEVEL_0_CHAIR_5: (3.990, 16.600, 111.420),
        PoolsLocations.LEVEL_0_CHAIR_6: (-0.470, 17.600, 120.820),
        PoolsLocations.LEVEL_0_CHAIR_7: (3.120, 28.600, 163.550),
        PoolsLocations.LEVEL_0_CHAIR_8: (-16.220, 26.600, 180.360),
        PoolsLocations.LEVEL_0_CHAIR_9: (-26.550, 22.600, 205.730),
        PoolsLocations.LEVEL_0_CHAIR_10: (-28.540, 22.600, 212.790),
        PoolsLocations.LEVEL_0_CHAIR_11: (-21.290, 22.600, 231.280),
        PoolsLocations.LEVEL_0_CHAIR_12: (19.460, 13.590, 232.520),
        PoolsLocations.LEVEL_0_CHAIR_13: (22.280, 13.590, 240.280),
        PoolsLocations.LEVEL_0_CHAIR_14: (21.790, 13.590, 238.820),
        PoolsLocations.LEVEL_0_CHAIR_15: (22.970, 13.590, 237.030),
        PoolsLocations.LEVEL_0_CHAIR_16: (23.560, 13.590, 240.460),
        PoolsLocations.LEVEL_0_CHAIR_17: (23.700, 13.590, 239.420),
        PoolsLocations.LEVEL_0_CHAIR_18: (23.560, 13.590, 238.370),
        PoolsLocations.LEVEL_0_CHAIR_19: (24.330, 13.590, 237.560),
        PoolsLocations.LEVEL_0_CHAIR_20: (24.450, 13.590, 235.960),
        PoolsLocations.LEVEL_0_CHAIR_21: (25.610, 13.590, 240.510),
        PoolsLocations.LEVEL_0_CHAIR_22: (25.010, 13.590, 238.580),
        PoolsLocations.LEVEL_0_CHAIR_23: (25.590, 13.590, 236.870),
        PoolsLocations.LEVEL_0_CHAIR_24: (26.420, 13.590, 235.620),
        PoolsLocations.LEVEL_0_CHAIR_25: (34.790, 13.590, 229.610),
        PoolsLocations.LEVEL_0_CHAIR_26: (35.510, 13.590, 231.610),
        PoolsLocations.LEVEL_0_CHAIR_27: (32.820, 13.590, 239.790),
        PoolsLocations.LEVEL_0_CHAIR_28: (42.610, 11.590, 250.610),
        PoolsLocations.LEVEL_0_CHAIR_29: (33.500, 13.590, 266.930),
        PoolsLocations.LEVEL_0_CHAIR_30: (24.220, 13.590, 266.780),
        PoolsLocations.LEVEL_0_CHAIR_31: (17.170, 11.590, 262.850),
        PoolsLocations.LEVEL_0_CHAIR_32: (2.960, 13.590, 256.250),
        PoolsLocations.LEVEL_0_CHAIR_33: (3.000, 13.590, 245.010),
        PoolsLocations.LEVEL_0_CHAIR_34: (8.900, 13.590, 232.520),
        PoolsLocations.LEVEL_0_CHAIR_35: (15.070, 13.590, 240.340),
        PoolsLocations.LEVEL_0_CHAIR_36: (46.100, 25.950, 272.420),
        PoolsLocations.LEVEL_0_CHAIR_37: (39.470, 10.750, 288.060),
        PoolsLocations.LEVEL_0_CHAIR_38: (22.620, 9.590, 278.860),
        PoolsLocations.LEVEL_0_CHAIR_39: (21.680, 9.590, 277.880),
        PoolsLocations.LEVEL_0_CHAIR_40: (-88.850, 16.600, 232.480),
        PoolsLocations.LEVEL_0_CHAIR_41: (-187.570, 1.960, 265.240),
        PoolsLocations.LEVEL_0_CHAIR_42: (-187.820, 1.960, 269.510),
        PoolsLocations.LEVEL_0_CHAIR_43: (-182.170, -7.740, 313.460),
    }
}

discriminators_by_level: Dict[PoolsLevels, Dict[str, List[Tuple[PoolsLocations, str, float, Optional[PoolsItems]]]]] = {
    PoolsLevels.LEVEL_1: {
        "springboard-vr-mesh": [
            (PoolsLocations.LEVEL_1_BOARD_1, "Y", -2.72, PoolsItems.DIVING_BOARDS),
            (PoolsLocations.LEVEL_1_BOARD_2, "Y", -13.57, PoolsItems.DIVING_BOARDS),
        ],
    },
    PoolsLevels.LEVEL_2: dict(),
    PoolsLevels.LEVEL_3: {
        "toilet_LOD0": [
            (PoolsLocations.LEVEL_3_PROP_1, "Y", 1.89, None),
            (PoolsLocations.LEVEL_3_PROP_2, "Y", 3.89, None),
            (PoolsLocations.LEVEL_3_PROP_4, "Y", -4.61, None),
        ],
    },
    PoolsLevels.LEVEL_4: {
        "giant-statue-head_LOD0": [
            (PoolsLocations.LEVEL_4_PROP_1, "Y", -22.61, None),
            (PoolsLocations.LEVEL_4_PROP_5, "Y", -24.66, None),
        ],
        "toilet_LOD0": [
            (PoolsLocations.LEVEL_4_PROP_2, "Y", -24.61, None),
            (PoolsLocations.LEVEL_4_PROP_4, "Y", -2.61, None),
        ],
        "water-floor.001": [
            (PoolsLocations.LEVEL_4_POOL_13, "X", -24.00, PoolsItems.POOLS_6T),
            (PoolsLocations.LEVEL_4_POOL_14, "X", -27.00, PoolsItems.POOLS_6T),
        ],
    },
    PoolsLevels.LEVEL_5: {
        "three-slides": [
            (PoolsLocations.LEVEL_5_SLIDE_1, "X", 21.00, PoolsItems.SLIDES_RED),
            (PoolsLocations.LEVEL_5_SLIDE_2, "X", 17.75, PoolsItems.SLIDES_YELLOW),
            (PoolsLocations.LEVEL_5_SLIDE_3, "X", 14.50, PoolsItems.SLIDES_BLUE),
        ],
        "springboard-vr-mesh": [
            (PoolsLocations.LEVEL_5_BOARD_1, "Z", 80.21, PoolsItems.DIVING_BOARDS),
            (PoolsLocations.LEVEL_5_BOARD_2, "Z", 93.81, PoolsItems.DIVING_BOARDS),
        ],
        "BezierCurve": [
            (PoolsLocations.LEVEL_5_SLIDE_5, "Z", 195.00, PoolsItems.SLIDES_RED),
            (PoolsLocations.LEVEL_5_SLIDE_6, "Z", 193.00, PoolsItems.SLIDES_BLUE),
            (PoolsLocations.LEVEL_5_SLIDE_7, "Z", 191.00, PoolsItems.SLIDES_YELLOW),
            (PoolsLocations.LEVEL_5_SLIDE_8, "Z", 189.00, PoolsItems.SLIDES_GREEN),
        ],
    },
    PoolsLevels.LEVEL_6: {
        "pillow_LOD0": [
            (PoolsLocations.LEVEL_6_PROP_3, "Y", -24.38, None),
            (PoolsLocations.LEVEL_6_PROP_6, "Y", -20.38, None),
        ],
        "tile-plane.064": [
            (PoolsLocations.LEVEL_6_POOL_20, "Y", -19.00, PoolsItems.POOLS_6T),
            (PoolsLocations.LEVEL_6_POOL_21, "Y", -16.00, PoolsItems.POOLS_4T),
        ],
    },
    PoolsLevels.LEVEL_0: {
        "giant head_LOD0": [
            (PoolsLocations.LEVEL_0_PROP_4, "Y", -39.97, None),
            (PoolsLocations.LEVEL_0_PROP_12, "Y", -7.83, None),
        ],
        "Plane.002": [
            (PoolsLocations.LEVEL_0_POOL_8, "Y", -74.65, PoolsItems.POOLS_3T),
            (PoolsLocations.LEVEL_0_POOL_10, "Y", -66.55, PoolsItems.POOLS_2T),
        ],
    },
}

eligible_starting_levels: List[PoolsLevels] = [
    PoolsLevels.LEVEL_2,
    PoolsLevels.LEVEL_4,
    PoolsLevels.LEVEL_5,
    PoolsLevels.LEVEL_6,
]

pool_collisions_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: {
        PoolsLocations.LEVEL_1_POOL_1: "waterfloor.008",
        PoolsLocations.LEVEL_1_POOL_2: "waterfloor.002",
        PoolsLocations.LEVEL_1_POOL_3: "waterfloor.006",
        PoolsLocations.LEVEL_1_POOL_4: "waterfloor.007",
        PoolsLocations.LEVEL_1_POOL_5: "waterfloor.005",
        PoolsLocations.LEVEL_1_POOL_6: "waterfloor.010",
        PoolsLocations.LEVEL_1_POOL_7: "waterfloor.004",
        PoolsLocations.LEVEL_1_POOL_8: "floorplane 2x4.224",
        PoolsLocations.LEVEL_1_POOL_9: "waterfloor.012",
        PoolsLocations.LEVEL_1_POOL_10: "waterfloor.009",
        PoolsLocations.LEVEL_1_POOL_11: "waterfloor.003",
        PoolsLocations.LEVEL_1_POOL_12: "waterfloor.011",
        PoolsLocations.LEVEL_1_POOL_13: "waterfloor.001",
    },
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_POOL_1: "waterfloor.004 box",
        PoolsLocations.LEVEL_2_POOL_2: "water-floor.001",
        PoolsLocations.LEVEL_2_POOL_3: "water-floor",
        PoolsLocations.LEVEL_2_POOL_4: "waterfloor.005",
        PoolsLocations.LEVEL_2_POOL_5: "tile-floor.003",
        PoolsLocations.LEVEL_2_POOL_6: "--waterfloor--",
        PoolsLocations.LEVEL_2_POOL_7: "waterfloor.018",
        PoolsLocations.LEVEL_2_POOL_8: "waterfloor.002",
        PoolsLocations.LEVEL_2_POOL_9: "waterfloor.009",
        PoolsLocations.LEVEL_2_POOL_10: "waterfloor.016 box",
        PoolsLocations.LEVEL_2_POOL_11: "tile-wall.051",
        PoolsLocations.LEVEL_2_POOL_12: "waterfloor.010",
        PoolsLocations.LEVEL_2_POOL_13: "waterfloor.006",
        PoolsLocations.LEVEL_2_POOL_14: "waterfloor.001",
        PoolsLocations.LEVEL_2_POOL_15: "waterfloor.004",
        PoolsLocations.LEVEL_2_POOL_16: "waterfloor.017",
        PoolsLocations.LEVEL_2_POOL_17: "waterfloor.019",
        PoolsLocations.LEVEL_2_POOL_18: "waterfloor.006 box",
        PoolsLocations.LEVEL_2_POOL_19: "tile-floor.098",
        PoolsLocations.LEVEL_2_POOL_20: "waterfloor.008",
        PoolsLocations.LEVEL_2_POOL_21: "--waterfloor--.001 box",
        PoolsLocations.LEVEL_2_POOL_22: "waterfloor.011",
        PoolsLocations.LEVEL_2_POOL_23: "stairs convex.046",
        PoolsLocations.LEVEL_2_POOL_24: "waterfloor.015",
        PoolsLocations.LEVEL_2_POOL_25: "waterfloor.003",
        PoolsLocations.LEVEL_2_POOL_26: "waterfloor.016",
        PoolsLocations.LEVEL_2_POOL_27: "waterfloor.011 box",
    },
    PoolsLevels.LEVEL_3: {
        PoolsLocations.LEVEL_3_POOL_1: "waterfloor.019",
        PoolsLocations.LEVEL_3_POOL_2: "waterfloor.007",
        PoolsLocations.LEVEL_3_POOL_3: "waterfloor.022",
        PoolsLocations.LEVEL_3_POOL_4: "waterfloor.001",
        PoolsLocations.LEVEL_3_POOL_5: "waterfloor.002 box",
        PoolsLocations.LEVEL_3_POOL_6: "waterfloor",
        PoolsLocations.LEVEL_3_POOL_7: "waterfloor.002",
        PoolsLocations.LEVEL_3_POOL_8: "waterfloor.011",
        PoolsLocations.LEVEL_3_POOL_9: "waterfloor.004",
        PoolsLocations.LEVEL_3_POOL_10: "waterfloor.005",
        PoolsLocations.LEVEL_3_POOL_11: "waterfloor.024",
        PoolsLocations.LEVEL_3_POOL_12: "waterfloor.028 box",
        PoolsLocations.LEVEL_3_POOL_13: "waterfloor.029",
        PoolsLocations.LEVEL_3_POOL_14: "waterfloor.009",
        PoolsLocations.LEVEL_3_POOL_15: "waterfloor.010",
        PoolsLocations.LEVEL_3_POOL_16: "waterfloor.011 box",
    },
    PoolsLevels.LEVEL_4: {
        PoolsLocations.LEVEL_4_POOL_1: "wood-waterfloor box",
        PoolsLocations.LEVEL_4_POOL_2: "waterfloor.001",
        PoolsLocations.LEVEL_4_POOL_3: "waterfloor.010",
        PoolsLocations.LEVEL_4_POOL_4: "waterfloor-box",
        PoolsLocations.LEVEL_4_POOL_5: "waterfloor.009",
        PoolsLocations.LEVEL_4_POOL_6: "water-floor",
        PoolsLocations.LEVEL_4_POOL_7: "tile-plane.300",
        PoolsLocations.LEVEL_4_POOL_8: "tile-plane.121",
        PoolsLocations.LEVEL_4_POOL_9: "waterfloor.003",
        PoolsLocations.LEVEL_4_POOL_10: "waterfloor.006",
        PoolsLocations.LEVEL_4_POOL_11: "waterfloor.005",
        PoolsLocations.LEVEL_4_POOL_12: "water-floor.003",
        PoolsLocations.LEVEL_4_POOL_15: "waterfloor.008",
        PoolsLocations.LEVEL_4_POOL_16: "waterfloor.011",
        PoolsLocations.LEVEL_4_POOL_17: "tile-waterfloor.002",
        PoolsLocations.LEVEL_4_POOL_18: "tile-waterfloor.004",
    },
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_POOL_1: "waterfloor.001",
        PoolsLocations.LEVEL_5_POOL_2: "waterfloor",
        PoolsLocations.LEVEL_5_POOL_3: "brick-object.169",
        PoolsLocations.LEVEL_5_POOL_4: "brick-object.173",
        PoolsLocations.LEVEL_5_POOL_5: "brick-object",
        PoolsLocations.LEVEL_5_POOL_6: "waterfloor.005",
        PoolsLocations.LEVEL_5_POOL_7: "waterfloor.016",
        PoolsLocations.LEVEL_5_POOL_8: "waterfloor.014",
        PoolsLocations.LEVEL_5_POOL_9: "arc-portal.047",
        PoolsLocations.LEVEL_5_POOL_10: "waterfloor box",
        PoolsLocations.LEVEL_5_POOL_11: "waterfloor.006",
        PoolsLocations.LEVEL_5_POOL_12: "waterfloor.007",
        PoolsLocations.LEVEL_5_POOL_13: "waterfloor.008",
        PoolsLocations.LEVEL_5_POOL_14: "waterfloor.009",
        PoolsLocations.LEVEL_5_POOL_15: "arc-portal.030",
        PoolsLocations.LEVEL_5_POOL_16: "Plane.059",
        PoolsLocations.LEVEL_5_POOL_17: "waterfloor.013",
        PoolsLocations.LEVEL_5_POOL_18: "BezierCurve.011",
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_POOL_1: "tile-plane.046",
        PoolsLocations.LEVEL_6_POOL_2: "tile-plane.104",
        PoolsLocations.LEVEL_6_POOL_3: "waterfloor.016 box",
        PoolsLocations.LEVEL_6_POOL_4: "tile-floor.003",
        PoolsLocations.LEVEL_6_POOL_5: "tile-plane.066",
        PoolsLocations.LEVEL_6_POOL_6: "tile-plane.076",
        PoolsLocations.LEVEL_6_POOL_7: "tile-plane.084",
        PoolsLocations.LEVEL_6_POOL_8: "plaster-plane.036",
        PoolsLocations.LEVEL_6_POOL_9: "tile-plane.450",
        PoolsLocations.LEVEL_6_POOL_10: "tile-plane.469",
        PoolsLocations.LEVEL_6_POOL_11: "tile-plane.321",
        PoolsLocations.LEVEL_6_POOL_12: "tile-wall.026",
        PoolsLocations.LEVEL_6_POOL_13: "waterfloor.006",
        PoolsLocations.LEVEL_6_POOL_14: "tile-plane.408",
        PoolsLocations.LEVEL_6_POOL_15: "tile-plane.295",
        PoolsLocations.LEVEL_6_POOL_16: "tile-plane.394",
        PoolsLocations.LEVEL_6_POOL_17: "waterfloor.001",
        PoolsLocations.LEVEL_6_POOL_18: "waterfloor.002",
        PoolsLocations.LEVEL_6_POOL_19: "tile-plane.261",
        PoolsLocations.LEVEL_6_POOL_22: "tile-plane.019",
        PoolsLocations.LEVEL_6_POOL_23: "waterfloor.003",
        PoolsLocations.LEVEL_6_POOL_24: "waterfloor.004",
        PoolsLocations.LEVEL_6_POOL_25: "Circle.008",
        PoolsLocations.LEVEL_6_POOL_26: "floorplane 2x4.248",
        PoolsLocations.LEVEL_6_POOL_27: "wallpaper.119",
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_POOL_1: "Circle.097_1 (chimney)",
        PoolsLocations.LEVEL_0_POOL_2: "Plane.121",
        PoolsLocations.LEVEL_0_POOL_3: "sewer-floor-collider",
        PoolsLocations.LEVEL_0_POOL_4: "Plane.383",
        PoolsLocations.LEVEL_0_POOL_5: "Plane.1303",
        PoolsLocations.LEVEL_0_POOL_6: "Plane.070",
        PoolsLocations.LEVEL_0_POOL_7: "Plane.447",
        PoolsLocations.LEVEL_0_POOL_9: "Plane.003",
        PoolsLocations.LEVEL_0_POOL_11: "Plane.038",
        PoolsLocations.LEVEL_0_POOL_12: "Plane.654",
    },
}

progress_collisions_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: dict(),
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_PROGRESS_3: "tile-wall.059",
        PoolsLocations.LEVEL_2_PROGRESS_8: "tile-wall.050",
    },
    PoolsLevels.LEVEL_3: dict(),
    PoolsLevels.LEVEL_4: dict(),
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_PROGRESS_2: "escalator-steps-collider",
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_PROGRESS_2: "escalators-mid",
        PoolsLocations.LEVEL_6_PROGRESS_4: "tile-plane.170",
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_PROGRESS_2: "BézierCurve.007",
        PoolsLocations.LEVEL_0_PROGRESS_4: "Cube.012",
        PoolsLocations.LEVEL_0_PROGRESS_6: "Plane.017",
    },
}

progress_flags_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: {
        PoolsLocations.LEVEL_1_PROGRESS_1: "TriggerAudio-Creature-Soundscape-1",
        PoolsLocations.LEVEL_1_PROGRESS_2: "ladders",
    },
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_PROGRESS_2: "GraffitiPiece_Progress_2",
        PoolsLocations.LEVEL_2_PROGRESS_4: "GraffitiPiece_Progress_1",
        PoolsLocations.LEVEL_2_PROGRESS_5: "GraffitiPiece_Progress_0",
        PoolsLocations.LEVEL_2_PROGRESS_6: "GraffitiPiece_Progress_4",
        PoolsLocations.LEVEL_2_PROGRESS_7: "GraffitiPiece_Progress_3",
        PoolsLocations.LEVEL_2_PROGRESS_9: "GraffitiEventCompleted-Progress",
    },
    PoolsLevels.LEVEL_3: dict(),
    PoolsLevels.LEVEL_4: {
        PoolsLocations.LEVEL_4_PROGRESS_1: "LevelProgress-TutorialWall",
        PoolsLocations.LEVEL_4_PROGRESS_4: "LevelProgress-EndingWall",
    },
    PoolsLevels.LEVEL_5: dict(),
    PoolsLevels.LEVEL_6: dict(),
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_PROGRESS_1: "ConcreteRoomWaterSlideEasterEgg",
    },
}

progress_zoom_ins_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: dict(),
    PoolsLevels.LEVEL_2: dict(),
    PoolsLevels.LEVEL_3: dict(),
    PoolsLevels.LEVEL_4: {
        PoolsLocations.LEVEL_4_PROGRESS_2: "railing.001",
        PoolsLocations.LEVEL_4_PROGRESS_3: "circle railing",
    },
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_PROGRESS_1: "railings",
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_PROGRESS_1: "railings .002",
        PoolsLocations.LEVEL_6_PROGRESS_3: "railings",
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_PROGRESS_3: "Plane.251",
        PoolsLocations.LEVEL_0_PROGRESS_5: "Plane.111",
    },
}

prop_collisions_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: {
        PoolsLocations.LEVEL_1_PROP_1: "poolstairs-head.001 box.001",
    },
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_PROP_1: "marble-statue_LOD0",
        PoolsLocations.LEVEL_2_PROP_2: "statue-agony_LOD2",
        PoolsLocations.LEVEL_2_PROP_3: "marble statue",
    },
    PoolsLevels.LEVEL_3: {
        PoolsLocations.LEVEL_3_PROP_3: "statue3_LOD0",
        PoolsLocations.LEVEL_3_PROP_5: "statue-sitting_LOD0",
    },
    PoolsLevels.LEVEL_4: {
        PoolsLocations.LEVEL_4_PROP_3: "poolstairs box.002",
        PoolsLocations.LEVEL_4_PROP_6: "statute-house_LOD0",
    },
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_PROP_1: "tile-pile_LOD0",
        PoolsLocations.LEVEL_5_PROP_2: "brick-object.117 box",
        PoolsLocations.LEVEL_5_PROP_3: "toilet_LOD0",
        PoolsLocations.LEVEL_5_PROP_4: "old british phone booth_LOD0",
        PoolsLocations.LEVEL_5_PROP_5: "Hornspeaker_LOD0",
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_PROP_1: "giant hand mesh_LOD0.006",
        PoolsLocations.LEVEL_6_PROP_2: "wooden table_LOD0",
        PoolsLocations.LEVEL_6_PROP_4: "toilet_LOD0",
        PoolsLocations.LEVEL_6_PROP_5: "painting-stand",
        PoolsLocations.LEVEL_6_PROP_7: "sofa_LOD0",
        PoolsLocations.LEVEL_6_PROP_10: "statue3_LOD0",
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_PROP_1: "Hornspeaker_LOD0",
        PoolsLocations.LEVEL_0_PROP_2: "Plane.165 ",  # Intentional trailing space
        PoolsLocations.LEVEL_0_PROP_3: "Plane.342",
        PoolsLocations.LEVEL_0_PROP_6: "big-table_LOD0",
        PoolsLocations.LEVEL_0_PROP_7: "rocking-chair_LOD0",
        PoolsLocations.LEVEL_0_PROP_8: "statue-chained",
        PoolsLocations.LEVEL_0_PROP_10: "commode_LOD0",
        PoolsLocations.LEVEL_0_PROP_11: "swing.LOD0",
    },
}

scene_internal_name_to_level: Dict[str, PoolsLevels] = {
    "1": PoolsLevels.LEVEL_1,
    "2": PoolsLevels.LEVEL_2,
    "3": PoolsLevels.LEVEL_3,
    "4": PoolsLevels.LEVEL_4,
    "5": PoolsLevels.LEVEL_5,
    "6": PoolsLevels.LEVEL_6,
    "Ending": PoolsLevels.ENDING,
    "0": PoolsLevels.LEVEL_0,
}

level_to_scene_internal_name: Dict[PoolsLevels, str] = {
    v: k for k, v in scene_internal_name_to_level.items()
}

slide_collisions_by_level: Dict[PoolsLevels, Dict[PoolsLocations, str]] = {
    PoolsLevels.LEVEL_1: {
        PoolsLocations.LEVEL_1_SLIDE_1: "spiral-slide_LOD0.002",
    },
    PoolsLevels.LEVEL_2: {
        PoolsLocations.LEVEL_2_SLIDE_1: "BezierCurve",
        PoolsLocations.LEVEL_2_SLIDE_2: "big-slide-green-rear",
        PoolsLocations.LEVEL_2_SLIDE_3: "slide",
    },
    PoolsLevels.LEVEL_3: {
        PoolsLocations.LEVEL_3_SLIDE_1: "slide-blue-short",
        PoolsLocations.LEVEL_3_SLIDE_2: "slide-curve-start",
        PoolsLocations.LEVEL_3_SLIDE_3: "level3-redslide",
        PoolsLocations.LEVEL_3_SLIDE_4: "yellow-slide",
    },
    PoolsLevels.LEVEL_4: {
        PoolsLocations.LEVEL_4_SLIDE_1: "red-slide",
        PoolsLocations.LEVEL_4_SLIDE_2: "yellow-slide",
        PoolsLocations.LEVEL_4_SLIDE_3: "blue-slide",
        PoolsLocations.LEVEL_4_SLIDE_4: "Circle.021",
    },
    PoolsLevels.LEVEL_5: {
        PoolsLocations.LEVEL_5_SLIDE_4: "BezierCurve.010",
        PoolsLocations.LEVEL_5_SLIDE_9: "BezierCurve.009",
    },
    PoolsLevels.LEVEL_6: {
        PoolsLocations.LEVEL_6_SLIDE_1: "BezierCurve.001",
        PoolsLocations.LEVEL_6_SLIDE_2: "BezierCurve.002",
    },
    PoolsLevels.LEVEL_0: {
        PoolsLocations.LEVEL_0_SLIDE_1: "ch0-purpleslide",
        PoolsLocations.LEVEL_0_SLIDE_2: "BézierCurve.001",
    },
}
