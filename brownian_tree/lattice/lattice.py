from typing import Tuple
from brownian_tree.tools.point import Point


class Lattice:
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        self.center = center
        self.max_size = max_size

    def is_edge(self, point: Point) -> bool:
        raise NotImplementedError

    def increase_size(self, step: int = 10) -> None:
        raise NotImplementedError

    def random_edge_point(self) -> Point:
        raise NotImplementedError

    def random_adjacent_point(self, point: Point) -> Point:
        raise NotImplementedError
