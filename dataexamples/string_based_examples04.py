#Check if a string has all characters with same frequency with one variation allowed
'''
Input : string str = "abbca"
Output : Yes
We can make it valid by removing "c"

Input : string str = "aabbcd"
Output : No
We need to remove at least two characters
to make it valid.

Input : string str = "abbccd"
Output : No
'''

def is_valid_string(str1, changes_allowed):
    count = {}
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for key, value in count.items():
        if value % 2 != 0:
            changes_allowed -= 1
            
    if changes_allowed == 0:
        return True
    else:
        return False
            
print is_valid_string("abbac", 1)
print is_valid_string("aabbcd", 1)
print is_valid_string("abbccd", 2)

'''
Perfect reversible string
You are given a string str, the task is to check that reverses of all possible substrings of str are present in str or not.
'''
print "\n"
def get_all_subsrings(str1):
    return [str1[i:j+1] for i in range(len(str1)) for j in range(i, len(str1))]

def check_if_substrings_palindrome(str1):
    sub_strings = get_all_subsrings(str1)
    print sub_strings
    for each_string in sub_strings:
        if each_string[::-1] not in str1:
            return False, each_string
    return True
        
print check_if_substrings_palindrome("abab")


'''
String with additive sequence
Input : s = 235813
Output : true
2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13

Input : s = 199100199
Output : true
1 + 99 = 100, 99 + 100 = 199

Input : s = 12345678
Output : false
'''


