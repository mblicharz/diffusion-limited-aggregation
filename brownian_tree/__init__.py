from typing import Tuple

from brownian_tree.brownian_tree import \
    BrownianTree


def get_brownian_tree(size: Tuple[int, int],
                      seed: Tuple[int, int] = None, particles_num: int = 0,
                      lattice_size: int = None, lattice_step: int = 10,
                      lattice_shape: str = 'square') \
        -> BrownianTree:
    """Returns an object of Brownian Tree.

    :param size: The maximum size of the area on which the fractal will grow.
    :type size: (int, int)
    :param seed: Point with x and y coordinates, from which the fractal growth
    will start. By default, it is centered on the area.
    :type seed: (int, int)
    :param particles_num: The number of particles that the fractal will
    consist of.
    :type particles_num: int
    :param lattice_size: The Initial size for lattice.
    This parameter is mandatory if you want to use lattice.
    :type lattice_size: int
    :param lattice_step: The value by which the lattice will grow.
    If 'lattice_size' is not set, this parameter will be ignored.
    :type lattice_step: int
    :param lattice_shape: The shape of lattice. Available shapes are 'square'
    and 'circle'. This affects the end result, e.g. for square lattice,
    the fractal will be square. If 'lattice_size' is not set, this parameter
    will be ignored.
    :type lattice_shape: str
    :return: Object of BrownianTree.
    :rtype: BrownianTree
    """
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
