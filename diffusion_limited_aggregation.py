from typing import Tuple

from area import Area, Point, SquareLattice


class DiffusionLimitedAggregation:
    def __init__(self, size: Tuple[int, int] = (0, 0),
                 seed: Point = None, particles_num: int = 0,
                 lattice_size: int = None, lattice_step: int = 10,
                 lattice_shape: str = 'square', show_progress: bool = False):
        self.area = Area(size)
        self.particles_num = particles_num
        if seed:
            self.seed = seed
        else:
            self.seed = Point(
                round(size[0] / 2),
                round(size[1] / 2))

        self.lattice = None
        self.lattice_step = None
        if lattice_size:
            self.lattice_step = lattice_step
            if lattice_shape == 'square':
                self.lattice = SquareLattice(self.seed, size)
            self.lattice.increase_size(self.lattice_step)

        self.show_progress = show_progress

    def show(self) -> None:
        self.area.plot()

    def draw(self) -> None:
        self.area.set_point(self.seed)

        for i in range(self.particles_num):
            if self.show_progress:
                print(f'{self.particles_num} / {i} ||'
                      f' {round(i / self.particles_num * 100)}%')

            particle = self._random_edge_point()

            while True:
                new_point = self._random_adjacent_point(particle)

                if self.area.point_exists(new_point):
                    self.area.set_point(particle)

                    if self.lattice and self.lattice.is_boundary(particle):
                        self.lattice.increase_size(self.lattice_step)

                    break

                else:
                    particle = new_point

    def _random_adjacent_point(self, point: Point) -> Point:
        if self.lattice:
            return self.lattice.random_adjacent_point(point)

        return self.area.random_adjacent_point(point)

    def _random_edge_point(self) -> Point:
        if self.lattice:
            return self.lattice.random_boundary_point()

        return self.area.get_random_edge_point()
