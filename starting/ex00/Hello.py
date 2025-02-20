ft_list = ["Hello", "World!"] # list of anytype and we can modify it, its ordered
ft_tuple = ("Hello", "Lebanon!") # tuple of anytype and we can't modify it, its ordered
ft_set = {"Beirut!", "Hello"} # A set is an unordered collection of unique elements.(you can add or remove element but you cant have duplicate values)
ft_dict = {"Hello" : "42Beirut!"} # dictionary is unsoreted, key must be unique, you can add, remove or modify data..

ordered_set = list(ft_set)
if "Hello" in ordered_set:
    ordered_set.remove("Hello")
    ordered_set.insert(0, "Hello")

ft_set = ordered_set

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
