class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dotproduct of the 2 vectors"""
        res = sum([x * y for x, y in zip(V1, V2)])
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Add two vectors"""
        res = [float(x + y) for x, y in zip(v1, v2)]
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Subtraction of two Vector"""
        res = [float(x - y) for x, y in zip(v1, v2)]
        print(f"Sous Vector is: {res}")
