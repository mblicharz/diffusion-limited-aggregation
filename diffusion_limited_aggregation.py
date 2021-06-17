from typing import Tuple, List


class DiffusionLimitedAggregation:
    def __init__(self, area: List[int, int] = None,
                 seed: Tuple[int, int] = None):
        self.__area = area
        if seed:
            self.__seed = seed
        else:
            self.__seed = [self.__area[0] / 2, self.__area[1] / 2]

    def draw(self) -> List[List[bool]]:
        pass
