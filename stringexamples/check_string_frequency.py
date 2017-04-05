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