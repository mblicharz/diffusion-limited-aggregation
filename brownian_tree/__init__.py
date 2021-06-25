from typing import Tuple

from brownian_tree.diffusion_limited_aggregation import \
    DiffusionLimitedAggregation


def get_brownian_tree(size: Tuple[int, int] = (0, 0),
                      seed: Tuple[int, int] = None, particles_num: int = 0,
                      lattice_size: int = None, lattice_step: int = 10,
                      lattice_shape: str = 'square') \
        -> DiffusionLimitedAggregation:
    brownian_tree = DiffusionLimitedAggregation(
        size=size,
        particles_num=particles_num,
        lattice_shape=lattice_shape,
    )

    return brownian_tree


__all__ = ['get_brownian_tree']