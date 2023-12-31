from mesa import Agent, Model  # type: ignore
from mesa.time import SimultaneousActivation  # type: ignore
from mesa.space import MultiGrid  # type: ignore


posicionesEdificios = [(2, 18), (2, 19), (2, 21),
                       (3, 18), (3, 19), (3, 20), (3, 21),
                       (4, 18), (4, 19), (4, 20), (4, 21),
                       (5, 18), (5, 19), (5, 20), (5, 21),
                       (6, 19), (6, 20), (6, 21),
                       (7, 18), (7, 19), (7, 20), (7, 21),
                       (8, 18), (8, 19), (8, 20), (8, 21),
                       (9, 18), (9, 19), (9, 20),
                       (10, 18), (10, 19), (10, 20), (10, 21),
                       (11, 18), (11, 20), (11, 21),  # edificio 1

                       (16, 18), (16, 19), (16, 20), (16, 21),
                       (17, 18), (17, 19), (17, 21),  # edificio 2

                       (20, 18), (20, 20), (20, 21),
                       (21, 18), (21, 19), (21, 20), (21, 21),  # edificio 3

                       (2, 12), (2, 13), (2, 14), (2, 15),
                       (3, 12), (3, 13), (3, 14), (3, 15),
                       (4, 12), (4, 14), (4, 15),  # edificio 4

                       (7, 12), (7, 13), (7, 14), (7, 15),
                       (8, 12), (8, 13), (8, 14),
                       (9, 12), (9, 13), (9, 14), (9, 15),
                       (10, 12), (10, 13), (10, 14), (10, 15),
                       (11, 12), (11, 14), (11, 15),  # edificio 5

                       (16, 12), (16, 14), (16, 15),
                       (17, 12), (17, 13), (17, 14), (17, 15),  # edificio 6

                       (20, 12), (20, 13), (20, 14), (20, 15),
                       (21, 12), (21, 13), (21, 15),  # edificio 7

                       (2, 2), (2, 3), (2, 4), (2, 5), (2, 7),
                       (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                       (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
                       (5, 2), (5, 4), (5, 5), (5, 6), (5, 7),  # edificio 8

                       (8, 2), (8, 4), (8, 5), (8, 6), (8, 7),
                       (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7),
                       (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7),
                       (11, 2), (11, 3), (11, 4), (11,
                                                   5), (11, 6), (11, 7),  # edificio 9

                       (16, 6), (16, 7),
                       (17, 7),
                       (18, 6), (18, 7),
                       (19, 7),
                       (20, 6), (20, 7),
                       (21, 6), (21, 7),  # edificio 10

                       (16, 2), (16, 3),
                       (17, 2), (17, 3),
                       (18, 2), (18, 3),
                       (19, 2),
                       (20, 2), (20, 3),
                       (21, 2), (21, 3)  # edificio 11
                       ]

posicionesEstacionamientos = [(9, 21),  # 1
                              (2, 20),  # 2
                              (17, 20),  # 3
                              (11, 19),  # 4
                              (20, 19),  # 5
                              (6, 18),  # 6
                              (8, 15),  # 7
                              (21, 14),  # 8
                              (4, 13),  # 9
                              (11, 13),  # 10
                              (16, 13),  # 11
                              (2, 6),  # 12
                              (17, 6),  # 13
                              (19, 6),  # 14
                              (5, 3),  # 15
                              (8, 3),  # 16
                              (19, 3)  # 17
                              ]


posicionesSemaforos = [((0, 12), (1, 12)),
                       ((2, 10), (2, 11)),
                       ((5, 15), (6, 15)),
                       ((7, 16), (7, 17)),
                       ((11, 0), (11, 1)),
                       ((12, 2), (13, 2)),
                       ((14, 3), (15, 3)),
                       ((14, 21), (15, 21)),
                       ((16, 4), (16, 5)),
                       ((16, 22), (16, 23)),
                       ((21, 8), (21, 9)),
                       ((22, 7), (23, 7))
                       ]


posicionesGlorieta = [(13, 9), (13, 10), (14, 9), (14, 10)]

sigPosEstacionamiento = {1: (9, 22),
                         2: (1, 20),
                         3: (18, 20),
                         4: (12, 19),
                         5: (19, 19),
                         6: (6, 17),
                         7: (8, 16),
                         8: (22, 14),
                         9: (5, 13),
                         10: (12, 13),
                         11: (15, 13),
                         12: (1, 6),
                         13: (17, 5),
                         14: (19, 5),
                         15: (6, 3),
                         16: (7, 3),
                         17: (19, 4)}

direcciones_calle = {
    (0, 0): [(1, 0), (1, 1)], (0, 1): [(0, 0), (1, 1), (1, 0)], (0, 2): [(1, 1), (0, 1)], (0, 3): [(1, 2), (0, 2)], (0, 4): [(1, 3), (0, 3)], (0, 5): [(1, 4), (0, 4)],
    (0, 6): [(1, 5), (0, 5)], (0, 7): [(1, 6), (0, 6)], (0, 8): [(1, 7), (0, 7)], (0, 9): [(1, 8), (0, 8)], (0, 10): [(1, 9), (0, 9)], (0, 11): [(1, 10), (0, 10)],
    (0, 12): [(1, 11), (0, 11)], (0, 13): [(1, 12), (0, 12)], (0, 14): [(1, 13), (0, 13)], (0, 15): [(1, 14), (0, 14)], (0, 16): [(1, 15), (0, 15)], (0, 17): [(1, 16), (0, 16)],
    (0, 18): [(1, 17), (0, 17)], (0, 19): [(1, 18), (0, 18)], (0, 20): [(1, 19), (0, 19)], (0, 21): [(1, 20), (0, 20)], (0, 22): [(1, 21), (0, 21)], (0, 23): [(1, 22), (0, 22)],

    (1, 0): [(2, 0), (2, 1)], (1, 1): [(2, 1), (2, 0)], (1, 2): [(0, 1), (1, 1), (2, 1)], (1, 3): [(0, 2), (1, 2)], (1, 4): [(0, 3), (1, 3)], (1, 5): [(0, 4), (1, 4)],
    (1, 6): [(0, 5), (1, 5)], (1, 7): [(0, 6), (1, 6)], (1, 8): [(0, 7), (1, 7)], (1, 9): [(0, 8), (1, 8), (2, 8)], (1, 10): [(0, 9), (1, 9), (2, 9)], (1, 11): [(0, 10), (1, 10)],
    (1, 12): [(0, 11), (1, 11)], (1, 13): [(0, 12), (1, 12)], (1, 14): [(0, 13), (1, 13)], (1, 15): [(0, 14), (1, 14)], (1, 16): [(0, 15), (1, 15)], (1, 17): [(0, 16), (1, 16)],
    (1, 18): [(0, 17), (1, 17)], (1, 19): [(0, 18), (1, 18)], (1, 20): [(0, 19), (1, 19)], (1, 21): [(0, 20), (1, 20)], (1, 22): [(0, 21), (0, 22), (0, 23)], (1, 23): [(0, 22), (0, 23)],

    (2, 0): [(3, 0), (3, 1)], (2, 1): [(3, 0), (3, 1)], (2, 8): [(3, 8), (3, 9)], (2, 9): [(3, 8), (3, 9)], (2, 10): [(1, 10)], (2, 11): [(1, 11)],
    (2, 16): [(1, 16)], (2, 17): [(1, 17)], (2, 22): [(1, 22)], (2, 23): [(1, 23), (1, 22)],

    (3, 0): [(4, 0), (4, 1)], (3, 1): [(4, 0), (4, 1)], (3, 8): [(4, 8), (4, 9)], (3, 9): [(4, 8), (4, 9)], (3, 10): [(2, 10), (2, 11)], (3, 11): [(2, 10), (2, 11)],
    (3, 16): [(2, 16), (2, 17)], (3, 17): [(2, 16), (2, 17)], (3, 22): [(2, 22), (2, 23)], (3, 23): [(2, 22), (2, 23)],

    (4, 0): [(5, 0), (5, 1)], (4, 1): [(5, 0), (5, 1)], (4, 8): [(5, 8), (5, 9)], (4, 9): [(5, 8), (5, 9)], (4, 10): [(3, 10), (3, 11)], (4, 11): [(3, 10), (3, 11)],
    (4, 16): [(3, 16), (3, 17)], (4, 17): [(3, 16), (3, 17)], (4, 22): [(3, 22), (3, 23)], (4, 23): [(3, 22), (3, 23)],

    (5, 0): [(6, 0), (6, 1)], (5, 1): [(6, 0), (6, 1)], (5, 8): [(6, 8), (6, 9)], (5, 9): [(6, 8), (6, 9)], (5, 10): [(4, 10), (4, 11)], (5, 11): [(4, 10), (4, 11), (5, 12)],
    (5, 12): [(6, 13), (5, 13)], (5, 13): [(6, 14), (5, 14)], (5, 14): [(6, 15), (5, 15)], (5, 15): [(5, 16)], (5, 16): [(4, 16), (4, 17)], (5, 17): [(4, 16), (4, 17)],
    (5, 22): [(4, 22), (4, 23)], (5, 23): [(4, 22), (4, 23)],

    (6, 0): [(7, 0), (7, 1)], (6, 1): [(7, 0), (7, 1)], (6, 2): [(6, 1), (7, 1)], (6, 3): [(6, 2), (7, 2)], (6, 4): [(6, 3), (7, 3)], (6, 5): [(6, 4), (7, 4)],
    (6, 6): [(6, 5), (7, 5)], (6, 7): [(6, 6), (7, 6)], (6, 8): [(7, 7), (7, 8), (7, 9)], (6, 9): [(7, 8), (7, 9)], (6, 10): [(5, 10), (5, 11)], (6, 11): [(5, 10), (5, 11), (5, 12)],
    (6, 12): [(5, 13), (6, 13)], (6, 13): [(5, 14), (6, 14)], (6, 14): [(5, 15), (6, 15)], (6, 15): [(5, 16), (6, 16)], (6, 16): [(5, 16), (5, 17)], (6, 17): [(5, 16), (5, 17)],
    (6, 22): [(5, 22), (5, 23)], (6, 23): [(5, 22), (5, 23)],

    (7, 0): [(8, 0), (8, 1)], (7, 1): [(8, 0), (8, 1)], (7, 2): [(7, 1)], (7, 3): [(7, 2), (6, 2)], (7, 4): [(7, 3), (6, 3)], (7, 5): [(7, 4), (6, 4)],
    (7, 6): [(7, 5), (6, 5)], (7, 7): [(7, 6), (6, 6)], (7, 8): [(8, 8), (8, 9), (7, 7)], (7, 9): [(8, 9), (8, 8)], (7, 10): [(6, 10), (6, 11)], (7, 11): [(6, 10), (6, 11)],
    (7, 16): [(6, 16), (6, 17)], (7, 17): [(6, 16), (6, 17)], (7, 22): [(6, 22), (6, 23)], (7, 23): [(6, 22), (6, 23)],

    (8, 0): [(9, 0), (9, 1)], (8, 1): [(9, 0), (9, 1)], (8, 8): [(9, 8), (9, 9)], (8, 9): [(9, 8), (9, 9)], (8, 10): [(7, 10), (7, 11)], (8, 11): [(7, 10), (7, 11)],
    (8, 16): [(7, 16), (7, 17)], (8, 17): [(7, 16), (7, 17)], (8, 22): [(7, 22), (7, 23)], (8, 23): [(7, 22), (7, 23)],

    (9, 0): [(10, 0), (10, 1)], (9, 1): [(10, 0), (10, 1)], (9, 8): [(10, 8), (10, 9)], (9, 9): [(10, 8), (10, 9)], (9, 10): [(8, 10), (8, 11)], (9, 11): [(8, 10), (8, 11)],
    (9, 16): [(8, 16), (8, 17)], (9, 17): [(8, 16), (8, 17)], (9, 22): [(8, 22), (8, 23)], (9, 23): [(8, 22), (8, 23)],

    (10, 0): [(11, 0), (11, 1)], (10, 1): [(11, 0), (11, 1)], (10, 8): [(11, 8), (11, 9)], (10, 9): [(11, 8), (11, 9)], (10, 10): [(9, 10), (9, 11)], (10, 11): [(9, 10), (9, 11)],
    (10, 16): [(9, 16), (9, 17)], (10, 17): [(9, 16), (9, 17)], (10, 22): [(9, 22), (9, 23)], (10, 23): [(9, 22), (9, 23)],
    (10, 16): [(9, 16), (9, 17)], (10, 17): [(9, 16), (9, 17)], (10, 22): [(9, 22), (9, 23)], (10, 23): [(9, 22), (9, 23)],

    (11, 0): [(12, 0), (12, 1)], (11, 1): [(12, 0), (12, 1)], (11, 8): [(12, 8)], (11, 9): [(12, 8), (12, 9)], (11, 10): [(10, 10), (10, 11)], (11, 11): [(10, 10), (10, 11)],
    (11, 16): [(10, 16), (10, 17)], (11, 17): [(10, 16), (10, 17)], (11, 22): [(10, 22), (10, 23)], (11, 23): [(10, 22), (10, 23)],

    (12, 0): [(13, 0), (13, 1)], (12, 1): [(13, 0), (13, 1)], (12, 2): [(12, 1), (13, 1)], (12, 3): [(12, 2), (13, 2)], (12, 4): [(12, 3), (13, 3)], (12, 5): [(12, 4), (13, 4)],
    (12, 6): [(12, 5), (13, 5)], (12, 7): [(12, 6), (13, 6)], (12, 8): [(13, 7), (13, 8)], (12, 9): [(13, 8)], (12, 10): [(11, 10), (11, 11)], (12, 11): [(11, 10), (11, 11)],
    (12, 12): [(11, 11), (12, 11), (13, 11)], (12, 13): [(12, 12), (13, 12)], (12, 14): [(12, 13), (13, 13)], (12, 15): [(12, 13), (13, 13)], (12, 16): [(12, 15), (13, 15)], (12, 17): [(11, 16), (12, 16), (12, 17)],
    (12, 18): [(11, 17), (12, 17), (13, 17)], (12, 19): [(12, 18), (13, 18)], (12, 20): [(12, 19), (13, 19)], (12, 21): [(12, 20), (13, 20)], (12, 22): [(11, 22), (11, 23)], (12, 23): [(11, 22), (11, 23)],

    (13, 0): [(14, 0), (14, 1)], (13, 1): [(14, 0), (14, 1)], (13, 2): [(13, 1)], (13, 3): [(13, 2), (12, 2)], (13, 4): [(13, 3), (12, 3)], (13, 5): [(13, 4), (12, 4)],
    (13, 6): [(13, 5), (12, 5)], (13, 7): [(13, 6), (12, 6)], (13, 8): [(13, 7), (14, 8)], (13, 11): [(12, 11)],
    (13, 12): [(13, 11)], (13, 13): [(13, 12), (12, 12)], (13, 14): [(13, 13), (12, 13)], (13, 15): [(13, 14), (12, 14)], (13, 16): [(13, 15), (12, 15)], (13, 17): [(13, 16), (12, 16)],
    (13, 18): [(13, 17), (12, 17)], (13, 19): [(13, 18), (12, 18)], (13, 20): [(13, 19), (12, 19)], (13, 21): [(13, 20), (12, 20)], (13, 22): [(12, 21), (12, 22), (12, 23), (13, 21)], (13, 23): [(12, 22), (12, 23)],

    (14, 0): [(15, 0), (15, 1)], (14, 1): [(15, 0), (15, 1), (15, 2)], (14, 2): [(14, 3), (15, 3)], (14, 3): [(14, 4), (15, 4)], (14, 4): [(14, 5), (15, 5)], (14, 5): [(14, 6), (15, 6)],
    (14, 6): [(14, 7), (15, 7)], (14, 7): [(14, 8), (15, 8)], (14, 8): [(15, 8), (15, 9)], (14, 11): [(13, 11)],
    (14, 12): [(14, 13), (15, 13)], (14, 13): [(14, 14), (15, 14)], (14, 14): [(14, 15), (15, 15)], (14, 15): [(14, 16), (15, 16)], (14, 16): [(14, 17), (15, 17)], (14, 17): [(14, 18), (15, 18)],
    (14, 18): [(14, 19), (15, 19)], (14, 19): [(14, 20), (15, 20)], (14, 20): [(14, 21), (15, 21)], (14, 21): [(13, 22), (14, 22), (15, 22)], (14, 22): [(13, 21), (13, 22), (13, 23)], (14, 23): [(13, 22), (13, 23)],

    (15, 0): [(16, 0), (16, 1)], (15, 1): [(15, 2), (16, 0), (16, 1)], (15, 2): [(14, 3), (15, 3)], (15, 3): [(14, 4), (15, 4)], (15, 4): [(14, 5), (15, 5)], (15, 5): [(14, 6), (15, 6)],
    (15, 6): [(14, 7), (15, 7)], (15, 7): [(15, 8)], (15, 8): [(16, 8)], (15, 9): [(16, 9), (15, 10)], (15, 10): [(15, 11)], (15, 11): [(14, 11), (15, 12)],
    (15, 12): [(14, 13), (15, 13)], (15, 13): [(14, 14), (15, 15)], (15, 14): [(14, 15), (15, 15)], (15, 15): [(14, 16), (15, 16)], (15, 16): [(16, 16), (14, 17), (15, 17)], (15, 17): [(16, 17), (14, 18), (15, 18)],
    (15, 18): [(14, 19), (15, 19)], (15, 19): [(14, 20), (15, 20)], (15, 20): [(14, 21), (15, 21)], (15, 21): [(15, 22)], (15, 22): [(14, 22), (14, 23)], (15, 23): [(14, 22), (14, 23)],

    (16, 0): [(17, 0), (17, 1)], (16, 1): [(17, 0), (17, 1)], (16, 4): [(15, 4), (15, 5)], (16, 5): [(15, 4), (15, 5)],
    (16, 8): [(17, 8), (17, 9)], (16, 9): [(17, 8), (17, 9)], (16, 10): [(15, 10), (15, 11)], (16, 11): [(15, 10), (15, 11)],
    (16, 16): [(17, 16), (17, 17)], (16, 17): [(17, 16), (17, 17)],
    (16, 22): [(15, 22), (15, 23)], (16, 23): [(15, 22), (15, 23)],

    (17, 0): [(18, 0), (18, 1)], (17, 1): [(18, 0), (18, 1)], (17, 4): [(16, 4), (16, 5)], (17, 5): [(16, 4), (16, 5)],
    (17, 8): [(18, 8), (18, 9)], (17, 9): [(18, 8), (18, 9)], (17, 10): [(16, 10), (16, 11)], (17, 11): [(16, 10), (16, 11)],
    (17, 16): [(18, 16), (18, 17)], (17, 17): [(18, 16), (18, 17)],
    (17, 22): [(16, 22), (16, 23)], (17, 23): [(16, 22), (16, 23)],

    (18, 0): [(19, 0), (19, 1)], (18, 1): [(19, 0), (19, 1)], (18, 4): [(17, 4), (17, 5)], (18, 5): [(17, 4), (17, 5)],
    (18, 8): [(19, 8), (19, 9)], (18, 9): [(19, 8), (19, 9)], (18, 10): [(17, 10), (17, 11)], (18, 11): [(18, 12), (17, 10), (17, 11)],
    (18, 12): [(18, 13), (19, 13)], (18, 13): [(18, 14), (19, 14)], (18, 14): [(18, 15), (19, 15)], (18, 15): [(18, 16)], (18, 16): [(19, 16), (19, 17)], (18, 17): [(19, 16), (19, 17)],
    (18, 18): [(18, 17)], (18, 19): [(19, 18), (18, 18)], (18, 20): [(19, 19), (18, 19)], (18, 21): [(19, 20), (18, 20)], (18, 22): [(18, 21), (17, 22), (17, 23)], (18, 23): [(17, 22), (17, 23)],

    (19, 0): [(20, 0), (20, 1)], (19, 1): [(20, 0), (20, 1)], (19, 4): [(18, 4), (18, 5)], (19, 5): [(18, 4), (18, 5)],
    (19, 8): [(20, 8), (20, 9)], (19, 9): [(20, 8), (20, 9)], (19, 10): [(18, 10), (18, 11)], (19, 11): [(18, 10), (18, 11)],
    (19, 12): [(18, 13), (19, 13)], (19, 13): [(18, 14), (19, 14)], (19, 14): [(18, 15), (19, 15)], (19, 15): [(19, 16)], (19, 16): [(20, 16), (20, 17)], (19, 17): [(20, 16), (20, 17)],
    (19, 18): [(19, 17)], (19, 19): [(18, 18), (19, 18)], (19, 20): [(18, 19), (19, 19)], (19, 21): [(18, 20), (19, 20)], (19, 22): [(18, 23), (18, 22), (18, 21), (19, 21)], (19, 23): [(18, 23), (18, 22)],

    (20, 0): [(21, 0), (21, 1)], (20, 1): [(21, 0), (21, 1)], (20, 4): [(19, 4), (19, 5)], (20, 5): [(19, 4), (19, 5)],
    (20, 8): [(21, 8), (21, 9)], (20, 9): [(21, 8), (21, 9)], (20, 10): [(19, 10), (19, 11)], (20, 11): [(19, 10), (19, 11)],
    (20, 16): [(21, 16), (21, 17)], (20, 17): [(21, 16), (21, 17)],
    (20, 22): [(19, 21), (19, 22), (19, 23)], (20, 23): [(19, 22), (19, 23)],

    (21, 0): [(22, 0), (22, 1)], (21, 1): [(22, 0), (22, 1)], (21, 4): [(20, 4), (20, 5)], (21, 5): [(20, 4), (20, 5)],
    (21, 8): [(22, 8), (22, 9)], (21, 9): [(22, 8), (22, 9), (22, 10)], (21, 10): [(20, 10), (20, 11)], (21, 11): [(20, 10), (20, 11)],
    (21, 16): [(22, 15), (22, 16), (22, 17)], (21, 17): [(22, 16), (22, 17), (22, 18)],
    (21, 22): [(20, 22), (20, 23)], (21, 23): [(20, 22), (20, 23)],

    (22, 0): [(23, 0), (23, 1)], (22, 1): [(22, 2)], (22, 2): [(22, 3), (23, 3)], (22, 3): [(22, 4), (23, 4)], (22, 4): [(21, 4), (22, 5), (23, 5)], (22, 5): [(21, 5), (22, 6), (23, 6)],
    (22, 6): [(22, 7), (23, 7)], (22, 7): [(22, 8), (23, 8)], (22, 8): [(22, 9), (23, 9)], (22, 9): [(22, 10), (23, 10)], (22, 10): [(21, 10), (22, 12), (23, 12)], (22, 11): [(21, 11), (22, 12), (23, 12)],
    (22, 12): [(22, 13), (23, 13)], (22, 13): [(22, 14), (23, 14)], (22, 14): [(22, 15), (23, 15)], (22, 15): [(22, 16), (23, 16)], (22, 16): [(22, 17), (23, 17)], (22, 17): [(22, 18), (23, 18)],
    (22, 18): [(22, 19), (23, 19)], (22, 19): [(22, 20), (23, 20)], (22, 20): [(22, 21), (23, 21)], (22, 21): [(22, 22)], (22, 22): [(21, 22), (21, 23)], (22, 23): [(21, 22), (21, 23)],

    (23, 0): [(23, 1)], (23, 1): [(22, 2), (23, 2)], (23, 2): [(22, 3), (23, 3)], (23, 3): [(22, 4), (23, 4)], (23, 4): [(22, 5), (23, 5)], (23, 5): [(22, 6), (23, 6)],
    (23, 6): [(22, 7), (23, 7)], (23, 7): [(22, 8), (23, 8)], (23, 8): [(22, 9), (23, 9)], (23, 9): [(22, 10), (23, 10)], (23, 10): [(22, 11), (23, 11)], (23, 11): [(22, 12), (23, 12)],
    (23, 12): [(22, 13), (23, 13)], (23, 13): [(22, 14), (23, 14)], (23, 14): [(22, 15), (23, 15)], (23, 15): [(22, 16), (23, 16)], (23, 16): [(22, 17), (23, 17)], (23, 17): [(22, 18), (23, 18)],
    (23, 18): [(22, 19), (23, 19)], (23, 19): [(22, 20), (23, 20)], (23, 20): [(22, 21), (23, 21)], (23, 21): [(22, 22), (22, 23)], (23, 22): [(22, 22), (22, 23)], (23, 23): [(22, 22), (22, 23)]

}


class Edificio(Agent):
    """
    Un edificio en la ciudad
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class Estacionamiento(Agent):
    """
    Un estacionamiento en la ciudad
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class Glorieta(Agent):
    """
    Una glorieta en la ciudad
    """
    def __init__(self, model):
        super().__init__("glorieta", model)


class Semaforo(Agent):
    """
    Un semaforo en la ciudad
    """
    def __init__(self, unique_id, model, color, position):
        super().__init__(unique_id, model)
        self.color = color
        self.count = 0
        self.pos = position

    def step(self):
        self.count += 1
        # Cambiar el color del semaforo cada 5 pasos
        if self.count == 5:
            if self.color == "green":
                self.color = "red"
                self.count = 0
            elif self.color == "red":
                self.color = "green"
                self.count = 0


class Coche(Agent):
    """
    Un coche en la ciudad
    """
    def __init__(self, unique_id, model, estOrigen, estDestino):
        super().__init__(unique_id, model)
        self.estOrigen = estOrigen
        self.estDestino = estDestino
        self.pos = posicionesEstacionamientos[estOrigen - 1]
        self.countPos = 1

    def step(self):
        # Si el coche está en el estacionamiento de origen, moverlo a la calle
        if self.countPos == 1:
            posicion = sigPosEstacionamiento[self.estOrigen]
            self.model.grid.move_agent(self, posicion)
            self.countPos = 0
            self.pos = posicion

        else:
            # Si el coche está frente al estacionamiento destino, meterlo y dejarlo ahí
            if self.pos == sigPosEstacionamiento[self.estDestino] or self.pos == posicionesEstacionamientos[self.estDestino - 1]:
                posicion = posicionesEstacionamientos[self.estDestino - 1]
                self.model.grid.move_agent(self, posicion)
                self.pos = posicion
            else:
                possibleSteps = direcciones_calle[self.pos]
                vecinos = self.model.grid.get_neighbors(self.pos, False)
                for vecino in vecinos:
                    # Si el vecino es un semaforo, y está en la lista de posibles pasos, y está en rojo, no moverse
                    if isinstance(vecino, Semaforo):
                        if vecino.pos in possibleSteps:
                            if vecino.color == "red":
                                return
                # Si no hay semaforos en rojo, moverse a una posicion aleatoria de las posibles
                posicion = self.random.choice(possibleSteps)
                self.model.grid.move_agent(self, posicion)
                self.pos = posicion


class SimulacionCiudad(Model):
    """
    Una simulacion de una ciudad
    """
    def __init__(self, estOrigen, estDestino):
        self.schedule = SimultaneousActivation(self)
        self.running = True
        self.grid = MultiGrid(24, 24, False)
        self.estOrigen = estOrigen
        self.estDestino = estDestino

        # Crear agentes de edificio
        for i in range(len(posicionesEdificios)):
            edificio = Edificio(i, self)
            self.grid.place_agent(edificio, posicionesEdificios[i])

        # Crear agentes de estacionamiento
        for j in range(len(posicionesEstacionamientos)):
            estacionamiento = Estacionamiento(j, self)
            self.grid.place_agent(
                estacionamiento, posicionesEstacionamientos[j])

        # Crear agentes de glorieta
        for k in posicionesGlorieta:
            glorieta = Glorieta(self)
            self.grid.place_agent(glorieta, k)

        # Crear agentes de semáforo
        for l in range(len(posicionesSemaforos)):
            for m in range(2):
                semaforoPos = posicionesSemaforos[l][m]
                # Si la posicion del semaforo es par, ponerlo en verde, si es impar, ponerlo en rojo
                if l % 2 == 0:
                    semaforo = Semaforo(
                        str(posicionesSemaforos[l][m]), self, "green", semaforoPos)
                else:
                    semaforo = Semaforo(
                        str(posicionesSemaforos[l][m]), self, "red", semaforoPos)
                self.grid.place_agent(semaforo, semaforoPos)
                self.schedule.add(semaforo)

        # Crear agente de coche
        coche = Coche(1, self, self.estOrigen, self.estDestino)
        self.grid.place_agent(
            coche, posicionesEstacionamientos[self.estOrigen - 1])
        self.schedule.add(coche)

    def step(self):
        self.schedule.step()