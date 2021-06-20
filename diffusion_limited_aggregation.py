from typing import Tuple

from area import Area, Point


class DiffusionLimitedAggregation:
    def __init__(self, area_size: Tuple[int, int] = (0, 0),
                 seed: Point = None, particles_num: int = 0):
        self.area_size = area_size
        self.particles_num = particles_num
        if seed:
            self.seed = seed
        else:
            self.seed = Point(
                round(self.area_size[0] / 2),
                round(self.area_size[1] / 2))

    def draw(self):
        pass
