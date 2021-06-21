from typing import Tuple

from area import Area, Point, SquareLattice


class DiffusionLimitedAggregation:
    def __init__(self, size: Tuple[int, int] = (0, 0),
                 seed: Point = None, particles_num: int = 0,
                 lattice_size: int = None, lattice_step: int = None,
                 lattice_shape: str = 'square'):
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
