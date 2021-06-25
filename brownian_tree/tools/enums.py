from enum import Enum


class Edge(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Direction(Enum):
    NORTH = 1
    NORTH_EAST = 2
    EAST = 3
    SOUTH_EAST = 4
    SOUTH = 5
    SOUTH_WEST = 6
    WEST = 7
    NORTH_WEST = 8
