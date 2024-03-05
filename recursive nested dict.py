# Recursive function to filter nested dictionaries
def filter_nested_dict(nested_dict):
    filtered_dict = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            filtered_dict[key] = filter_nested_dict(value)
        else:
            # Apply conditional filtering here
            if value % 2 == 0:
                filtered_dict[key] = value
    return filtered_dict

# Example nested dictionary
nested_dict = {
    'a': {'x': 1, 'y': 2, 'z': {'p': 3, 'q': 4}},
    'b': {'x': 5, 'y': 6, 'z': 7},
    'c': {'x': 8, 'y': {'r': 9, 's': 10}, 'z': 11}
}

# Call the recursive function
filtered_dict = filter_nested_dict(nested_dict)

print(filtered_dict)
