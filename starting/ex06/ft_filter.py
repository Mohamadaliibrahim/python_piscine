def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for x in iterable:
        if function(x):
            yield x


"""#yield allows a function to return a value and then pause its execution,
# saving its state. When the function is called again, it picks
# up from where it left off, rather than starting from the beginning."""
