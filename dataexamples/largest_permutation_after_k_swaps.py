"""
Largest permutation after at most k swaps
Given a permutation of first n natural numbers as array and an integer k. Print the lexicographically largest permutation after at most k swaps

Input: arr[] = {4, 5, 2, 1, 3}
       k = 3
Output: 5 4 3 2 1
Explanation:
Swap 1st and 2nd elements: 5 4 2 1 3 
Swap 3rd and 5th elements: 5 4 3 1 2 
Swap 4th and 5th elements: 5 4 3 2 1 

Input: arr[] = {2, 1, 3}
       k = 1
Output: 3 1 2
"""

def largest_permutation(a, k):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if k == 0:
                return a
            if a[i] > a[j]:
                continue
            else:
                a[i], a[j] = a[j], a[i] 
                k -= 1
    return a
            
print largest_permutation([4, 5, 2, 1, 3], 3)
print largest_permutation([2, 1, 3], 1)