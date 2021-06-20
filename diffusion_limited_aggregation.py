import random
from typing import Tuple

from area import Area, Point


class DiffusionLimitedAggregation:
    def __init__(self, area_size: Tuple[int, int] = (0, 0),
                 seed: Point = None, particles_num: int = 0):
        self.area_size = area_size
        self.area = Area(self.area_size)
        self.particles_num = particles_num
        if seed:
            self.seed = seed
        else:
            self.seed = Point(
                round(self.area_size[0] / 2),
                round(self.area_size[1] / 2))

    def show(self) -> None:
        self.area.plot()

    def draw(self) -> None:
        self.area.set_point(self.seed)

        for _ in range(self.particles_num):
            particle = self.area.get_random_edge_point()

            while True:
                new_point = self._random_adjacent_point(particle)

                if self.area.point_exists(new_point):
                    self.area.set_point(particle)
                    break

                else:
                    particle = new_point

    def _random_adjacent_point(self, point: Point) -> Point:
        return self._brownian_step_move(point)

    def _brownian_step_move(self, point: Point = None) -> Point:
        direction = random.randint(1, 8)

        if direction == 1 and point.x > 0:
            return Point(point.x - 1, point.y)

        elif direction == 2 and \
                point.x > 0 and point.y < self.area_size[1] - 1:
            return Point(point.x - 1, point.y + 1)

        elif direction == 3 and point.y < self.area_size[1] - 1:
            return Point(point.x, point.y + 1)

        elif direction == 4 and \
                point.x < self.area_size[0] - 1 and \
                point.y < self.area_size[1] - 1:
            return Point(point.x + 1, point.y + 1)

        elif direction == 5 and point.x < self.area_size[0] - 1:
            return Point(point.x + 1, point.y)

        elif direction == 6 and \
                point.x < self.area_size[0] - 1 and point.y > 0:
            return Point(point.x + 1, point.y - 1)

        elif direction == 7 and point.y > 0:
            return Point(point.x, point.y - 1)

        elif direction == 8 and point.x > 0 and point.y > 0:
            return Point(point.x - 1, point.y - 1)

        else:
            return point
