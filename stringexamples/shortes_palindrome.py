# Time:  O(n)
# Space: O(n)
#
# Given a string S, you are allowed to convert it to a palindrome 
# by adding characters in front of it. Find and return the shortest 
# palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".
#
def shortest_palindrome(s1):
    missing = []
    start = 0
    for i in range(len(s1)-1, 0, -1):
        if s1[i] != s1[start]:
            missing.append(s1[i])
            i -= 1
        else:
            i -= 1
            start += 1
    return ''.join(missing) + s1

print shortest_palindrome('aacecaaa')
print shortest_palindrome('abcd') 
