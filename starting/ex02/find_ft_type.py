def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    
    # isinstance check the object that if its list or any kind of type specified
    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"str : {object} is at 42 beirut : {object_type}")
    else:
        print("Type not found")
    return 42