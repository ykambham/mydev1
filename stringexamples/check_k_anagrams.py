
#Check if two strings are k-anagrams or not
'''
Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.

Two strings are called k-anagrams if following two conditions are true.

Both have same number of characters.
Two strings can become anagram by changing at most k characters in a string.
Examples:

Input:  str1 = "anagram" , str2 = "grammar" , k = 3
Output:  Yes
Explanation: We can update maximum 3 values and 
it can be done in changing only 'r' to 'n' 
and 'm' to 'a' in str2.
'''

def check_k_anagrams(str1, str2, k):
    for i in range(len(str1)):
        if str1[i] not in list(str2):
            k -= 1
    if k >= 0:
        return True
    else:
        return False

print check_k_anagrams("anagram", "grammar", 3)