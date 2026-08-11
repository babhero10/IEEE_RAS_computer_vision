class Counter:
    def __init__(self):
        # TODO: start the count at 0
        pass

    def increment(self):
        # TODO: add 1 to the count
        pass

    def decrement(self):
        # TODO: subtract 1 from the count
        pass

    def reset(self):
        # TODO: set the count back to 0
        pass


if __name__ == "__main__":
    c = Counter()
    assert c.count == 0
    c.increment()
    c.increment()
    c.increment()
    assert c.count == 3
    c.decrement()
    assert c.count == 2
    c.reset()
    assert c.count == 0
    print("ex4_class_methods: all checks passed!")
