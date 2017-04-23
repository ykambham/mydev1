"""
Count number of substrings with exactly k distinct characters
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}
"""
import collections
def count_subtrings_k_distrinct(s, k):
    res = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            s1 = s[i:j]
            if len(s1) >= k and len(collections.Counter(s1).items()) == k:
                res += 1
    return res

print count_subtrings_k_distrinct('abc', 2)
print count_subtrings_k_distrinct('aba', 2)
print count_subtrings_k_distrinct('aa', 1)

