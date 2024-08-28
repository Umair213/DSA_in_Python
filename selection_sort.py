def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newarr = []
    copied_arr = list(arr)
    for i in range(1, len(copied_arr)+1):
        smallest = find_smallest(copied_arr)
        newarr.append(copied_arr.pop(smallest))
    return newarr
        
print(selection_sort([10, 2, 3, 1, 44]))