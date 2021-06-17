from typing import Tuple, List


class DiffusionLimitedAggregation:
    def __init__(self, area_size: List[int, int] = None,
                 seed: Tuple[int, int] = None):
        self.area_size = area_size
        if seed:
            self.seed = seed
        else:
            self.seed = [self.area_size[0] / 2, self.area_size[1] / 2]
