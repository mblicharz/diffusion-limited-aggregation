class Size:
    def __init__(self, max_x: int, max_y: int):
        self._validate(max_x, max_y)
        self.max_x = max_x
        self.max_y = max_y

    def _validate(self, max_x, max_y) -> bool:
        if max_x < 0 or max_y < 0:
            raise ValueError(
                "Both dimensions should be equal or greater than 0."
            )

        return True
