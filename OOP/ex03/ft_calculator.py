class calculator:
    """Calculator class"""

    def __init__(self, vector):
        """Calculator constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition"""
        res = [x + object for x in self.vector]
        self.vector = res
        print(res)

    def __mul__(self, object) -> None:
        """Multiplication"""
        res = [x * object for x in self.vector]
        self.vector = res
        print(res)

    def __sub__(self, object) -> None:
        """Subtraction"""
        res = [x - object for x in self.vector]
        self.vector = res
        print(res)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            print("Error: Division by zero")
            return
        res = [x / object for x in self.vector]
        self.vector = res
        print(res)
