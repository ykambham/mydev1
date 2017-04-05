# binary search
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    is_found = False
    while first <= last and not is_found:
        mid_point = (first + last) // 2
        if item == mid_point:
            is_found = True
            return is_found
        else:
            if item < mid_point:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return is_found
                
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print binary_search(a_list, 10)
        