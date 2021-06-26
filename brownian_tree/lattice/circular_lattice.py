import math
import random
from typing import Tuple

from brownian_tree.lattice.lattice import Lattice
from brownian_tree.tools.enums import Direction
from brownian_tree.tools import Point


class CircularLattice(Lattice):
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        super().__init__(center, max_size)

        self.radius = 0

    def is_edge(self, point: Point) -> bool:
        point_radius = self._point_radius(point)

        return point_radius >= self.radius - 1

    def increase_size(self, step: int = 10) -> None:
        self.radius += step

        if self.center.x - self.radius < 0:
            self.radius += self.center.x - self.radius

        if self.center.x + self.radius > self.max_size.max_x:
            self.radius -= self.max_size.max_x - self.radius

        if self.center.y - self.radius < 0:
            self.radius += self.center.y - self.radius

        if self.center.y + self.radius > self.max_size.max_y:
            self.radius -= self.max_size.max_y - self.radius

    def random_edge_point(self) -> Point:
        theta = random.random() * 2.0 * math.pi
        return Point(
            round(self.center.x + math.cos(theta) * (self.radius - 1)),
            round(self.center.y + math.sin(theta) * (self.radius - 1))
        )

    def random_adjacent_point(self, point: Point) -> Point:
        new_point = Point(point.x, point.y)
        direction = random.choice(list(Direction))

        if direction == Direction.NORTH:
            new_point.x -= 1

        elif direction == Direction.NORTH_EAST:
            new_point.x -= 1
            new_point.y += 1

        elif direction == Direction.EAST:
            new_point.y += 1

        elif direction == Direction.SOUTH_EAST:
            new_point.x += 1
            new_point.y += 1

        elif direction == Direction.SOUTH:
            new_point.x += 1

        elif direction == Direction.SOUTH_WEST:
            new_point.x += 1
            new_point.y -= 1

        elif direction == Direction.WEST:
            new_point.y -= 1

        elif direction == Direction.NORTH_WEST:
            new_point.x -= 1
            new_point.y -= 1

        new_point_radius = self._point_radius(new_point)
        if new_point_radius < self.radius:
            return new_point

        return point

    def _point_radius(self, point: Point) -> int:
        return round(math.hypot(
            self.center.x - point.x, self.center.y - point.y
        ))
