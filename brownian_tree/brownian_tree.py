from typing import Tuple

import tqdm

from brownian_tree.lattice import CircularLattice
from brownian_tree.lattice import SquareLattice
from brownian_tree.tools.area import Area
from brownian_tree.tools.point import Point


class BrownianTree:
    def __init__(self, size: Tuple[int, int],
                 seed: Tuple[int, int] = None, particles_num: int = 0,
                 lattice_size: int = None, lattice_step: int = 10,
                 lattice_shape: str = 'square'):
        self.area = Area(size)
        self.particles_num = particles_num
        if seed:
            self.seed = Point(seed[0], seed[1])
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
            if lattice_shape == 'circle':
                self.lattice = CircularLattice(self.seed, size)
            self.lattice.increase_size(self.lattice_step)

        self.progress_bar = tqdm.tqdm(
            range(self.particles_num),
            unit=' particles',
            ncols=74,
        )

    def show(self) -> None:
        self.area.plot()

    def draw(self) -> None:
        self.area.set_point(self.seed)

        for _ in range(self.particles_num):
            particle = self._random_edge_point()

            while True:
                new_point = self._random_adjacent_point(particle)

                if self.area.point_exists(new_point):
                    self.area.set_point(particle)
                    self.progress_bar.update(1)

                    if self.lattice and self.lattice.is_edge(particle):
                        self.lattice.increase_size(self.lattice_step)

                    break

                particle = new_point

        self.progress_bar.close()

    def _random_adjacent_point(self, point: Point) -> Point:
        if self.lattice:
            return self.lattice.random_adjacent_point(point)

        return self.area.random_adjacent_point(point)

    def _random_edge_point(self) -> Point:
        if self.lattice:
            return self.lattice.random_edge_point()

        return self.area.random_edge_point()
