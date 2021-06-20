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
            return Point(0, random.randint(0, self.size[1]) - 1)

        elif edge == 2:
            return Point(random.randint(0, self.size[0] - 1), self.size[1] - 1)

        elif edge == 3:
            return Point(self.size[0] - 1, random.randint(0, self.size[1] - 1))

        elif edge == 4:
            return Point(random.randint(0, self.size[0] - 1), 0)

    def plot(self) -> None:
        plt.ylim(0, self.size[0] - 1)
        plt.xlim(0, self.size[1] - 1)
        plt.imshow(self.matrix)
        plt.show()
