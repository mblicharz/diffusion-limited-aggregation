import random
from typing import Tuple

from brownian_tree.lattice.lattice import Lattice
from brownian_tree.tools.enums import Edge, Direction
from brownian_tree.tools import Point


class SquareLattice(Lattice):
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        super().__init__(center, max_size)

        self.min_x = center.x
        self.min_y = center.y
        self.max_x = center.x
        self.max_y = center.y

    def is_edge(self, point: Point) -> bool:
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

    def random_edge_point(self) -> Point:
        edge = random.choice(list(Edge))
        point = None

        if edge == Edge.NORTH:
            point = Point(self.min_x + 1,
                         random.randint(self.min_y + 1, self.max_y - 1)
                         )

        if edge == Edge.EAST:
            point = Point(random.randint(self.min_x + 1, self.max_x - 1),
                         self.min_y + 1
                         )

        if edge == Edge.SOUTH:
            point = Point(self.max_x - 1,
                         random.randint(self.min_y + 1, self.max_y - 1)
                         )

        if edge == Edge.WEST:
            point = Point(random.randint(self.min_x + 1, self.max_x - 1),
                         self.max_y - 1
                         )

        return point

    def random_adjacent_point(self, point: Point) -> Point:
        direction = random.choice(list(Direction))
        new_point = Point(point.x, point.y)

        if direction == Direction.NORTH and point.x > self.min_x + 1:
            new_point.x -= 1

        if direction == Direction.NORTH_EAST and \
                point.x > self.min_x + 1 and point.y < self.max_y - 1:
            new_point.x -= 1
            new_point.y += 1

        if direction == Direction.EAST and point.y < self.max_y - 1:
            new_point.y += 1

        if direction == Direction.SOUTH_EAST and \
                point.x < self.max_x - 1 and \
                point.y < self.max_y - 1:
            new_point.x += 1
            new_point.y += 1

        if direction == Direction.SOUTH and point.x < self.max_x - 1:
            new_point.x += 1

        if direction == Direction.SOUTH_WEST and \
                point.x < self.max_x - 1 and point.y > self.min_y + 1:
            new_point.x += 1
            new_point.y -= 1

        if direction == Direction.WEST and point.y > self.min_y + 1:
            new_point.y -= 1

        if direction == Direction.NORTH_WEST and \
                point.x > self.min_x + 1 and point.y > self.min_y + 1:
            new_point.x -= 1
            new_point.y -= 1

        return new_point
