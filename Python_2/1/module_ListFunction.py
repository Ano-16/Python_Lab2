
def find_max(lst):
    """Find the maximum value in a given list."""
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    """Find the minimum value in a given list."""
    if not lst:
        return None
    return min(lst)

def calculate_sum(lst):
    """Sum of all elements in a list."""
    return sum(lst)

def compute_average(lst):
    """Compute the average of the list."""
    if not lst:
        return None
    return sum(lst) / len(lst)

def determine_median(lst):
    """Determine the median of a list."""
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median

# Demonstration of the functions with various lists

if __name__ == "__main__":

    list1 = [x for x in range(1, 11)]  # List of numbers from 1 to 10
    list2 = [2, 3, 5, 7, 11, 13]  # List of prime numbers
    list3 = [1.5, 2.5, 3.5, 4.5, 5.5]  # List of floating-point numbers

    print("List 1:", list1)
    print("Max:", find_max(list1))
    print("Min:", find_min(list1))
    print("Sum:", calculate_sum(list1))
    print("Average:", compute_average(list1))
    print("Median:", determine_median(list1))

    print("\nList 2:", list2)
    print("Max:", find_max(list2))
    print("Min:", find_min(list2))
    print("Sum:", calculate_sum(list2))
    print("Average:", compute_average(list2))
    print("Median:", determine_median(list2))

    print("\nList 3:", list3)
    print("Max:", find_max(list3))
    print("Min:", find_min(list3))
    print("Sum:", calculate_sum(list3))
    print("Average:", compute_average(list3))
    print("Median:", determine_median(list3))

  