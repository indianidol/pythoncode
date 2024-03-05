# Nested dictionary
nested_dict = {
    'a': {'x': 1, 'y': 2, 'z': 3},
    'b': {'x': 4, 'y': 5, 'z': 6},
    'c': {'x': 7, 'y': 8, 'z': 9}
}

# Dictionary comprehension with conditional filtering
filtered_dict = {outer_key: 
                 {inner_key: value for inner_key, value in inner_dict.items() if value % 2 == 0} 
                 for outer_key, inner_dict in nested_dict.items()
                 }

print(filtered_dict)
