import random
from typing import Tuple

from area import Point


class Lattice:
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        self.center = center
        self.max_size = max_size

    def is_boundary(self, point: Point) -> bool:
        raise NotImplemented

    def increase_size(self, step: int = 10) -> None:
        raise NotImplemented

    def random_boundary_point(self) -> Point:
        raise NotImplemented

    def random_adjacent_point(self, point: Point) -> Point:
        raise NotImplemented


class SquareLattice(Lattice):
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        super().__init__(center, max_size)

        self.min_x = center.x
        self.min_y = center.y
        self.max_x = center.x
        self.max_y = center.y

    def is_boundary(self, point: Point) -> bool:
        return point.x == self.min_x + 1 \
               or point.x == self.max_x - 1 \
               or point.y == self.min_y + 1 \
               or point.y == self.max_y - 1

    def increase_size(self, step: int = 10) -> None:
        if self.min_x != 0:
            self.min_x = max(self.min_x - step, 0)

        if self.min_y != 0:
            self.min_y = max(self.min_y - step, 0)

        if self.max_x != self.max_size[0] - 1:
            self.max_x = min(self.max_x + step, self.max_size[0] - 1)

        if self.max_y != self.max_size[1] - 1:
            self.max_y = min(self.max_y + step, self.max_size[1] - 1)

    def random_boundary_point(self) -> Point:
        boundary = random.randint(1, 4)

        if boundary == 1:
            return Point(self.min_x + 1,
                         random.randint(self.min_y + 1, self.max_y - 1)
                         )

        if boundary == 2:
            return Point(random.randint(self.min_x + 1, self.max_x - 1),
                         self.min_y + 1
                         )

        if boundary == 3:
            return Point(self.max_x - 1,
                         random.randint(self.min_y + 1, self.max_y - 1)
                         )

        if boundary == 4:
            return Point(random.randint(self.min_x + 1, self.max_x - 1),
                         self.max_y - 1
                         )

    def random_adjacent_point(self, point: Point) -> Point:
        direction = random.randint(1, 8)

        if direction == 1 and point.x > self.min_x + 1:
            return Point(point.x - 1, point.y)

        elif direction == 2 and \
                point.x > self.min_x + 1 and point.y < self.max_y - 1:
            return Point(point.x - 1, point.y + 1)

        elif direction == 3 and point.y < self.max_y - 1:
            return Point(point.x, point.y + 1)

        elif direction == 4 and \
                point.x < self.max_x - 1 and \
                point.y < self.max_y - 1:
            return Point(point.x + 1, point.y + 1)

        elif direction == 5 and point.x < self.max_x - 1:
            return Point(point.x + 1, point.y)

        elif direction == 6 and \
                point.x < self.max_x - 1 and point.y > self.min_y + 1:
            return Point(point.x + 1, point.y - 1)

        elif direction == 7 and point.y > self.min_y + 1:
            return Point(point.x, point.y - 1)

        elif direction == 8 and \
                point.x > self.min_x + 1 and point.y > self.min_y + 1:
            return Point(point.x - 1, point.y - 1)

        else:
            return point
