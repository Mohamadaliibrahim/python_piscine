from typing import Any


def callLimit(limit: int):
    """A decorator factory that limits the
    number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """A decorator that wraps the given
        function and restricts its execution
        after the specified limit is reached."""
        def limit_function(*args: Any, **kwds: Any):
            """The inner function that enforces
            the call limit. It checks whether the
            function has been called fewer times
            than the allowed limit before
            executing it."""
            nonlocal count  # Allows modification
            # of the count variable in the outer scope
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function

    return callLimiter
