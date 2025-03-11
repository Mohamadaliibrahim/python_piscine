def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
        Calculate the BMI for each pair of height and weight
        values and return a list of BMI values.
        Args:
            height (List[Union[int, float]]): A list of heights
            in meters (can be int or float).
            weight (List[Union[int, float]]): A list of weights
            in kilograms (can be int or float).
        Returns:
            List[Union[int, float]]: A list of BMI values.
        Raises:
            ValueError: If the lengths of height and weight
            lists do not match.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    bmi_values = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_values.append(bmi)
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Given a list of BMI values and a limit,
        return a list of booleans where each
        boolean indicates whether the corresponding
        BMI is greater than the limit.
        Args:
            bmi (List[Union[int, float]]): A list of
            BMI values (can be int or float).
            limit (int): An integer representing the
            limit to compare the BMI values against.
        Returns:
            List[bool]: A list of booleans where each
            value is True if the BMI exceeds the limit,
                        otherwise False.
        Raises:
            ValueError: If the length of the BMI list
            is not the same as the limit.
            TypeError: If BMI list contains non-numeric
            values or if limit is not an integer.
    """
    if not all(isinstance(value, (int, float)) for value in bmi):
        raise TypeError("Error: float or int")
    if not isinstance(limit, int):
        raise TypeError("The limit must be an integer.")
    result = [value > limit for value in bmi]
    return result
