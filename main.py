from brownian_tree import get_brownian_tree

if __name__ == "__main__":
    brownian_tree = get_brownian_tree(size=(250, 250),
                                      particles_num=12000,
                                      lattice_shape='circle'
                                      )
    brownian_tree.draw()
    brownian_tree.show()
