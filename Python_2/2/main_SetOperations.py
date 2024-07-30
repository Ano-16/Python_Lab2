import module_SetOperations as mso

def main():
    # Example sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # add_element
    print("Original set1:", set1)
    mso.add_element(set1, 6)
    print("After adding 6 to set1:", set1)

    # remove_element
    mso.remove_element(set1, 3)
    print("After removing 3 from set1:", set1)

    # union_intersection
    union_set, intersection_set = mso.union_intersection(set1, set2)
    print("Union of set1 and set2:", union_set)
    print("Intersection of set1 and set2:", intersection_set)

    # difference
    difference_set = mso.difference(set1, set2)
    print("Difference set1 - set2:", difference_set)

    # is_subset
    print("Is set1 a subset of set2?:", mso.is_subset(set1, set2))

    # set_length
    print("Length of set1:", mso.set_length(set1))

    # symmetric_difference
    symmetric_diff = mso.symmetric_difference(set1, set2)
    print("Symmetric difference of set1 and set2:", symmetric_diff)

    # power_set
    power_set = mso.power_set(set1)
    print("Power set of set1:", power_set)

    # unique_subsets
    unique_subs = mso.unique_subsets(set1)
    print("Unique subsets of set1:", unique_subs)

if __name__ == "__main__":
    main()
