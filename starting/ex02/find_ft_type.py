def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    
    # Print the corresponding type name for each object type
    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type not found")
    
    # Return 42 at the end of the function
    return 42


# from find_ft_type import all_thing_is_obj

