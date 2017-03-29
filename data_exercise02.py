# Find if sum of elements match to target

def is_sum_found_in_elements(elements, target):
    is_found = False
    compliments = []
    for element in elements:
        if (target - element) in compliments:
            return True
        else:
            compliments.append(element)
    return is_found

elements = [1, 2, 4, 4, 7]
print is_sum_found_in_elements(elements, 3)
print is_sum_found_in_elements(elements, 8)
print is_sum_found_in_elements(elements, 10)