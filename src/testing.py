

def quickSort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = [x for x in arr[:-1] if x < pivot]
    greater_or_equal = [x for x in arr[:-1] if x >= pivot]

    return quickSort(smaller) + [pivot] + quickSort(greater_or_equal)


unsorted_list: list = [3, 6, 8, 10, 1, 2, 2]
sorted_list = quickSort(unsorted_list)
print(sorted_list)

