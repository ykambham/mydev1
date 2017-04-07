"""
Remove extra spaces from a string
Given a string containing many consecutive spaces, trim all spaces so that all words should contain only a single space between them. The conversion should be done in-place and solution should handle trailing and leading spaces and also remove preceding spaces before common punctuation like full stop, comma and a question mark.

Examples:

Input: 
str = "   Hello Geeks . Welcome   to  GeeksforGeeks   .    ";
Output: 
"Hello Geeks. Welcome to GeeksforGeeks."

Input: 
str = "GeeksforGeeks";
Output: 
"GeeksforGeeks"
(No change is needed)
"""


def remove_extra_spaces(s):
    s1 = ''
    for s2 in s.split(' '):
        if s2:
            s1 += s2 + ' '
    s3 = list(s1)
    for i in range(len(s3) - 1):
        if s3[i] == ' ':
            if s3[i + 1] == '.':
                s3[i] = ''
                
    return ''.join(s3)


print remove_extra_spaces('   Hello Geeks . Welcome   to  GeeksforGeeks   .    ')
print remove_extra_spaces("geeksforgeeks")