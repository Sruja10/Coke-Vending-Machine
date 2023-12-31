class NoCoke(Exception):
    # Exception raised when coke is not present in the menu
    def __init__(self, msg):
        super().__init__(msg)


class InsufficientAmount(Exception):
    # Exception raised when amount entered to buy coke is inefficient
    def __init__(self, msg):
        super().__init__(msg)


class InvalidAmount(Exception):
    # Exception raised when the amount entered is -ve
    def __init__(self, msg):
        super().__init__(msg)
