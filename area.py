import random
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        if x < 0 or y < 0:
            raise ValueError("Both x and y should be greater or equal 0.")
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x} {self.y}'


class SquareLattice:
    def __init__(self, center: Point, max_size: Tuple[int, int]):
        self.center = center
        self.max_size = max_size

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


class Area:
    def __init__(self, size: Tuple[int, int] = (0, 0)):
        self.size = size
        self.matrix = np.zeros((self.size[0], self.size[1]))

    def set_point(self, point: Point):
        self.matrix[point.x][point.y] = 1

    def point_exists(self, point: Point) -> bool:
        return bool(self.matrix[point.x][point.y])

    def get_random_edge_point(self) -> Point:
        edge = random.randint(1, 4)

        if edge == 1:
            return Point(0, random.randint(0, self.size[1] - 1))

        elif edge == 2:
            return Point(random.randint(0, self.size[0] - 1), self.size[1] - 1)

        elif edge == 3:
            return Point(self.size[0] - 1, random.randint(0, self.size[1] - 1))

        elif edge == 4:
            return Point(random.randint(0, self.size[0] - 1), 0)

    def random_adjacent_point(self, point: Point = None) -> Point:
        direction = random.randint(1, 8)

        if direction == 1 and point.x > 0:
            return Point(point.x - 1, point.y)

        elif direction == 2 and \
                point.x > 0 and point.y < self.size[1] - 1:
            return Point(point.x - 1, point.y + 1)

        elif direction == 3 and point.y < self.size[1] - 1:
            return Point(point.x, point.y + 1)

        elif direction == 4 and \
                point.x < self.size[0] - 1 and \
                point.y < self.size[1] - 1:
            return Point(point.x + 1, point.y + 1)

        elif direction == 5 and point.x < self.size[0] - 1:
            return Point(point.x + 1, point.y)

        elif direction == 6 and \
                point.x < self.size[0] - 1 and point.y > 0:
            return Point(point.x + 1, point.y - 1)

        elif direction == 7 and point.y > 0:
            return Point(point.x, point.y - 1)

        elif direction == 8 and point.x > 0 and point.y > 0:
            return Point(point.x - 1, point.y - 1)

        else:
            return point

    def plot(self) -> None:
        plt.ylim(0, self.size[0] - 1)
        plt.xlim(0, self.size[1] - 1)
        plt.imshow(self.matrix)
        plt.show()
