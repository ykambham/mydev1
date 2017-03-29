#Lexicographically find first palindrome string
from permute import permute

def is_palindrome(str1):
    if str1 == str1[::-1] and len(str1) > 1:
        return True

def first_possible_palindrome(sub_strings):
    for string in sub_strings:
        if is_palindrome(string):
            return string

def possible_strings(str1):
    #split and sort list
    chars_list = sorted(list(str1))
    sub_strings = []
    permutations = permute(chars_list)
    for each in permutations:
        sub_strings.append(''.join(each))
    return sub_strings

print first_possible_palindrome(possible_strings("malayalam"))