# a

def clean_dict_value_3a(d, bad_val):
    clean_dict = {k: v for k, v in d.items() if v != bad_val}
    return clean_dict


my_dict = {'a': 1, 'b': 3, 'c': 5, 'd': 14}

print(my_dict)
print(clean_dict_value_3a({'a': 5, 'b': 6, 'c': 5, 'd': 14}, 5))


# b

def clean_dict_values_3b(d, bad_val):
    return {k: v for k, v in d.items() if v not in bad_val}


print(my_dict)
print(clean_dict_values_3b(my_dict, [3, 4, 5]))
