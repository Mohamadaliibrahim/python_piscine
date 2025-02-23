from typing import List, Union

#     Calculate the BMI for each pair of height and weight values and return a list of BMI values.
    
#     Args:
#         height (List[Union[int, float]]): A list of heights in meters (can be int or float).
#         weight (List[Union[int, float]]): A list of weights in kilograms (can be int or float).
    
#     Returns:
#         List[Union[int, float]]: A list of BMI values.
    
#     Raises:
#         ValueError: If the lengths of height and weight lists do not match.

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    bmi_values = []
    for h, w in zip(height, weight):
        bmi = w / (h * 2)
        bmi_values.append(bmi)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    print("hello")