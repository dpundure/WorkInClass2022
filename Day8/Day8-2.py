def replace_dist_value(d, bad_val, good_val):
    new_dict = {}
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value
    return new_dict


my_dict = {'a': 5, 'b': 6, 'c': 5}

print(my_dict, "->", replace_dist_value(my_dict, 5, 10))
