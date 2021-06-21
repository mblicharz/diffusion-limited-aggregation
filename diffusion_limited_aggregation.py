from typing import Tuple

from area import Area, Point


class DiffusionLimitedAggregation:
    def __init__(self, size: Tuple[int, int] = (0, 0),
                 seed: Point = None, particles_num: int = 0):
        self.area = Area(size)
        self.particles_num = particles_num
        if seed:
            self.seed = seed
        else:
            self.seed = Point(
                round(size[0] / 2),
                round(size[1] / 2))

    def show(self) -> None:
        self.area.plot()

    def draw(self) -> None:
        self.area.set_point(self.seed)

        for _ in range(self.particles_num):
            print(_)
            particle = self.area.get_random_edge_point()

            while True:
                new_point = self.area.random_adjacent_point(particle)

                if self.area.point_exists(new_point):
                    self.area.set_point(particle)
                    break

                else:
                    particle = new_point
