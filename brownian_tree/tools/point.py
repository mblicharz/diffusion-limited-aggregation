class Point:
    def __init__(self, x: int = 0, y: int = 0):
        if x < 0 or y < 0:
            raise ValueError("Both x and y should be greater or equal 0.")
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x} {self.y}'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
