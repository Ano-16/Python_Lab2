# main_ListOperations.py

import module_ListFunction as mlf

def main():
    list1 = [x for x in range(1, 11)]
    list2 = [x for x in range(10, 0, -1)]  
    list3 = [x**2 for x in range(1, 6)]  
    list4 = [2, 3, 5, 7, 11, 13]  
    list5 = [1.5, 2.5, 3.5, 4.5, 5.5]  

    # Testing the functions from module_ListFunction
    print("List 1:", list1)
    print("Max:", mlf.find_max(list1))
    print("Min:", mlf.find_min(list1))
    print("Sum:", mlf.calculate_sum(list1))
    print("Average:", mlf.compute_average(list1))
    print("Median:", mlf.determine_median(list1))

    print("\nList 2:", list2)
    print("Max:", mlf.find_max(list2))
    print("Min:", mlf.find_min(list2))
    print("Sum:", mlf.calculate_sum(list2))
    print("Average:", mlf.compute_average(list2))
    print("Median:", mlf.determine_median(list2))

    print("\nList 3:", list3)
    print("Max:", mlf.find_max(list3))
    print("Min:", mlf.find_min(list3))
    print("Sum:", mlf.calculate_sum(list3))
    print("Average:", mlf.compute_average(list3))
    print("Median:", mlf.determine_median(list3))

    print("\nList 4:", list4)
    print("Max:", mlf.find_max(list4))
    print("Min:", mlf.find_min(list4))
    print("Sum:", mlf.calculate_sum(list4))
    print("Average:", mlf.compute_average(list4))
    print("Median:", mlf.determine_median(list4))

    print("\nList 5:", list5)
    print("Max:", mlf.find_max(list5))
    print("Min:", mlf.find_min(list5))
    print("Sum:", mlf.calculate_sum(list5))
    print("Average:", mlf.compute_average(list5))
    print("Median:", mlf.determine_median(list5))

if __name__ == "__main__":
    main()
