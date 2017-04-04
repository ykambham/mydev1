# Find substrings starting with same first character and last character

def find_sub_strings(str1):
    sub_strings_list = []
    for i in range(len(str1)):
        for j in range(i, len(str1) + 1):
            sub_string = str1[i:j]
            if sub_string:
                if sub_string[0] == sub_string[-1]:
                    sub_strings_list.append(str1[i:j])
    return sub_strings_list

print find_sub_strings("abcab")


import itertools
for p in itertools.product("abc", repeat=3):
    print p
    
# Find largest word in dictionary by deleting some characters of given string
def longest_substring_possible(a_list, str1):
    str_list = list(str1)
    max_count = 0 
    matching_word = '' 
    for item in a_list:
        matching_count = 0
        for elemtent in list(item):
            if elemtent in str_list:
                matching_count += 1
        if matching_count > max_count:
            max_count = matching_count
            matching_word = item
    return matching_word

print longest_substring_possible(["ale", "apple", "monkey", "plea"], 'abpcplea')


# Check if a string can be obtained by rotating another string 2 places
'''
Input : string1 = "amazon" 
        string2 = "azonam"  // rotated anti-clockwise
Output : Yes

Input : string1 = "amazon"
        string2 = "onamaz"  // rotated clockwise
Output : Yes
'''

def is_string_rotated(str1, str2, rotation):
    clock_wise_rotation = str1[rotation:] + str1[:rotation]
    anti_clock_wise_rotation = str1[-rotation::-1] + str1[:len(str1) - rotation]
    if  str2 == clock_wise_rotation or anti_clock_wise_rotation:
        return True
        
print is_string_rotated("amazon", "azonam", 2)
print is_string_rotated("amazon", "onamaz", 2)


#Efficiently check if a string has duplicates without using any additional data structure
def check_duplicates(str1):
    for i in range(len(str1)):
        for j in range(i + 1, len(str1)):
            if str1[i] == str1[j]:
                return True
    return False


print check_duplicates("aaabbccc")
print check_duplicates("abcd")


#Hamming Distance between two strings

def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

print hamming_distance("geeksforgeeks", 'geeksandgeeks')


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


# Check if the string is a palindrome by removing just one letter
def is_palindrome(str1):
    if str1 == str1[::-1]:
        return True

def check_if_palindrome_possible(str1):
    for i in range(len(str1)):
        if is_palindrome(str1[:i] + str1[i+1:]):
            return str1[i]

print check_if_palindrome_possible("abcbea")


# Check if a string can become empty by recursively deleting a given sub-string

def check_strings(str1, str2):
    if str1 == str2:
        print "Can be emptied"
    else:
        if str1.find(str2) > 0:
            if len(str1) > 0:
                check_strings(str1.replace(str2, ''), str2)
        else:
            print "Not possible!"
            return

check_strings("geegeeksks", 'geeksa')