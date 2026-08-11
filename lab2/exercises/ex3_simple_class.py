class Dog:
    def __init__(self, name, breed):
        # TODO: store `name` and `breed` as attributes
        pass

    def bark(self):
        # TODO: return "<name> says Woof!"
        pass


if __name__ == "__main__":
    rex = Dog("Rex", "Labrador")
    assert rex.name == "Rex"
    assert rex.breed == "Labrador"
    assert rex.bark() == "Rex says Woof!"
    print("ex3_simple_class: all checks passed!")
