def max_subarry_value(a, length):
    max_value = a[0]
    cur_max = a[0]
    for i in range(1, length):
        cur_max = max(a[i], cur_max + a[i])
        max_value = max(cur_max, max_value)
    
    return max_value

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print max_subarry_value(a, len(a))
        