"""
Calculate sum of all numbers present in a string
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.

Examples:

Input:  1abc23
Output: 24

Input:  geeks4geeks
Output: 4

Input:  1abc2x30yz67
Output: 100

Input:  123abc
Output: 123
"""

def find_sum_string(s):
    sum = 0
    num1 = ''
    for i in range(len(s)):
        if s[i].isdigit():
            num1 += s[i]
        else:
            if num1:
                sum += int(num1)
                num1 = ''
    sum += int(num1)
    return sum

print find_sum_string('12abc23')
print find_sum_string('123abc1')
