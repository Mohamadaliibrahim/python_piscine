def square(x: int | float) -> int | float:
    """Return the square of x"""
    z = x * x
    return z


def pow(x: int | float) -> int | float:
    """Return the x power x"""
    z = x ** x
    return z


def outer(x: int | float, function) -> object:
    """inner function that computes function(x)"""

    def inner() -> float:
        """Update x"""

        nonlocal x  # allows modification of x in the outer scope
        res = function(x)
        x = res
        return res
    return inner
