# You are given a list of non-negative integers, a1, a2, ..., an,
# and a target, S. Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
import itertools

def get_combinations(a_list, repeat):
    return itertools.product(a_list, repeat=repeat)

def find_possible_ways(a_list, target):
    operators = ['+', '-']
    res = 0
    combos = get_combinations(operators, len(a_list))
    for combo in combos:
        count= 0
        for i in range(len(a_list)):
            count += int(combo[i] + str(a_list[i]))
        if count == target:
            res += 1
    return res
    
print find_possible_ways([1, 1, 1, 1, 1], 3)