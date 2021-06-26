import random
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np

from brownian_tree.tools.enums import Edge, Direction
from brownian_tree.tools.point import Point
from brownian_tree.tools.size import Size


class Area:
    def __init__(self, size: Tuple[int, int] = (0, 0)):
        self.size = Size(size[0], size[1])
        self.matrix = np.zeros((self.size.max_x, self.size.max_y))

    def set_point(self, point: Point):
        self.matrix[point.x][point.y] = 1

    def point_exists(self, point: Point) -> bool:
        return bool(self.matrix[point.x][point.y])

    def random_edge_point(self) -> Point:
        edge = random.choice(list(Edge))
        point = None

        if edge == Edge.NORTH:
            point = Point(0, random.randint(0, self.size.max_y - 1))

        if edge == Edge.EAST:
            point = Point(
                random.randint(0, self.size.max_x - 1),
                self.size.max_y - 1
            )

        if edge == Edge.SOUTH:
            point = Point(
                self.size.max_x - 1,
                random.randint(0, self.size.max_y - 1)
            )

        if edge == Edge.WEST:
            point = Point(random.randint(0, self.size.max_x - 1), 0)

        return point

    def random_adjacent_point(self, point: Point) -> Point:
        direction = random.choice(list(Direction))
        new_point = Point(point.x, point.y)

        if direction == Direction.NORTH and point.x > 0:
            new_point.x -= 1

        if direction == Direction.NORTH_EAST and \
                point.x > 0 and point.y < self.size.max_y - 1:
            new_point.x -= 1
            new_point.y += 1

        if direction == Direction.EAST and point.y < self.size.max_y - 1:
            new_point.y += 1

        if direction == Direction.SOUTH_EAST and \
                point.x < self.size.max_x - 1 and \
                point.y < self.size.max_y - 1:
            new_point.x += 1
            new_point.y += 1

        if direction == Direction.SOUTH and point.x < self.size.max_x - 1:
            new_point.x += 1

        if direction == Direction.SOUTH_WEST and \
                point.x < self.size.max_x - 1 and point.y > 0:
            new_point.x += 1
            new_point.y -= 1

        if direction == Direction.WEST and point.y > 0:
            new_point.y -= 1

        if direction == Direction.NORTH_WEST and point.x > 0 and point.y > 0:
            new_point.x -= 1
            new_point.y -= 1

        return new_point

    def plot(self) -> None:
        plt.ylim(0, self.size.max_x - 1)
        plt.xlim(0, self.size.max_y - 1)
        plt.imshow(self.matrix)
        plt.show()
