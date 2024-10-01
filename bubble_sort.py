def bubble_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        skip_last = 0
        counter = 1
        while counter < len(lst):
            for i in range(len(lst)):
                if i < (len(lst)-1-skip_last) and lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            counter += 1
            skip_last += 1
        return lst
    
print(bubble_sort([93, 42, 101, 39, 12]))

def modified_bubble_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        skip_last = 0
        counter = 1
        duplicate_list = []
        while counter < len(lst):
            for i in range(len(lst)):
                if i < (len(lst)-1-skip_last) and lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            if duplicate_list == lst:
                break
            duplicate_list = lst
            counter += 1
            skip_last += 1
        return lst

print(modified_bubble_sort([1, 2, 3, 4, 5]))