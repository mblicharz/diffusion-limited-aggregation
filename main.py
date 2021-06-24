import time

from diffusion_limited_aggregation import DiffusionLimitedAggregation

if __name__ == "__main__":
    dla = DiffusionLimitedAggregation(
        size=(250, 250),
        particles_num=12000,
        lattice_shape='circle',
    )

    start_time = time.perf_counter()

    dla.draw()

    end_time = time.perf_counter()

    run_time = end_time - start_time

    print(f"Executed in {run_time:.4f} secs.")

    dla.show()
