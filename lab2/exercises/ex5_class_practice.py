class Rectangle:
    def __init__(self, width, height):
        # TODO: store `width` and `height` as attributes
        pass

    def area(self):
        # TODO: return width * height
        pass

    def perimeter(self):
        # TODO: return 2 * (width + height)
        pass

    def is_square(self):
        # TODO: return True if width == height, else False
        pass


if __name__ == "__main__":
    r = Rectangle(4, 5)
    assert r.area() == 20
    assert r.perimeter() == 18
    assert r.is_square() is False

    s = Rectangle(3, 3)
    assert s.area() == 9
    assert s.is_square() is True
    print("ex5_class_practice: all checks passed!")
