'''
a = [1, 2, 3, 4, 3]
sum = 6
combinations = [1, 2, 3], [2, 4], [3, 3]
'''

def find_combos(Alist, target):
    count = 0
    for i in range(len(Alist)):
        total_sum = Alist[i]
        for j in range(i+1, len(Alist)):
            total_sum += Alist[j]
            sum =  Alist[i] + Alist[j]
            if total_sum == target or sum == target:
                count += 1
    return count       

print find_combos([1, 2, 3, 4, 3], 6)