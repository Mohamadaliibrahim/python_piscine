def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array based on
    the given start and end indices.
    Args:
        family (list): A 2D array (list of lists).
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.
    Returns:
        list: A sliced 2D array (list of lists).
    Raises:
        TypeError: If the input is not a
        valid list or if a row in the 2D array is not a list.
        ValueError: If the rows are not of
        the same length or if the start and end indices are out of range.
    """
    if not isinstance(family, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each row in the 2D array must be a list")
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise TypeError("All rows must have the same length")
    print(f"My shape is: ({len(family),  row_length})")
    if start < 0:
        start = len(family) + start
    if end < 0:
        end = len(family) + end
    if start < 0 or end > len(family) or start > end:
        raise ValueError("Invalid slicing indices")
    sliced_family = family[start:end]
    print(f"My new shape is : {len(sliced_family)}, {row_length}")
    return sliced_family
