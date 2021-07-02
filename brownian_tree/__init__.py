from typing import Tuple

from brownian_tree.brownian_tree import \
    BrownianTree


def get_brownian_tree(size: Tuple[int, int],
                      seed: Tuple[int, int] = None, particles_num: int = 0,
                      lattice_size: int = None, lattice_step: int = 10,
                      lattice_shape: str = 'square') \
        -> BrownianTree:
    bt = BrownianTree(
        size=size,
        seed=seed,
        particles_num=particles_num,
        lattice_size=lattice_size,
        lattice_step=lattice_step,
        lattice_shape=lattice_shape,
    )

    return bt


__all__ = ['get_brownian_tree']
