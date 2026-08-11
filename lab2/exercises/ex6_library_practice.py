import math


class Circle:
    def __init__(self, radius):
        # TODO: store `radius` as an attribute
        pass

    def area(self):
        # TODO: return the circle's area using math.pi
        pass

    def circumference(self):
        # TODO: return the circle's circumference using math.pi
        pass


if __name__ == "__main__":
    c = Circle(3)
    assert round(c.area(), 2) == 28.27
    assert round(c.circumference(), 2) == 18.85
    print("ex6_library_practice: all checks passed!")
