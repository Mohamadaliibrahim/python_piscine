import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Garlic: {object} <class 'float'>")

    # Check if the object is a boolean (False is a boolean)
    elif isinstance(object, bool):
        print(f"Fake: {object} <class 'bool'>")
    
    # Check if the object is an integer (Zero is an integer)
    elif isinstance(object, int):
        print(f"Zero: {object} <class 'int'>")
    
    # Check if the object is an empty string
    elif isinstance(object, str) and object == '':
        print(f"Empty: <class 'str'>")
    
    # For any other objects, print their type
    else:
        print("Type not Found")
        return 1
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))