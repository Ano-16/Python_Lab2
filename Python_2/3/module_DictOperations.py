def merging_Dict(*args):
    """Merge multiple dictionaries."""
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

def common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set &= set(dictionary.keys())
    return common_keys_set

def invert_dict(d):
    """Invert a dictionary, swapping keys and values. 
    If multiple keys have the same value, group these keys in a list."""
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted

def common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    common_pairs = args[0].items()
    for dictionary in args[1:]:
        common_pairs &= dictionary.items()
    return dict(common_pairs)

# Demonstration of the functions with examples
if __name__ == "__main__":
    # Example dictionaries
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    dict3 = {'a': 1, 'c': 3, 'e': 6}

    # Merging dictionaries
    merged_dict = merging_Dict(dict1, dict2, dict3)
    print("Merged dictionary:", merged_dict)

    # Finding common keys
    common_keys_set = common_keys(dict1, dict2, dict3)
    print("Common keys:", common_keys_set)

    # Inverting a dictionary
    inverted_dict = invert_dict(dict1)
    print("Inverted dictionary:", inverted_dict)

    # Finding common key-value pairs
    common_pairs = common_key_value_pairs(dict1, dict2, dict3)
    print("Common key-value pairs:", common_pairs)
