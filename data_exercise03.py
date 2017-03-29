# Check if two strings are anagrams in optimized way and not using in built libraries
# like collections 
from atk import Value
def check_anagram(str1, str2):
    is_anagram = False
    # if lengths are not same then they are not anagrams
    if len(str1) != len(str2):
        return is_anagram
    char_dict = {}
    for i in range(len(str1)):
        if str1[i] in char_dict: 
            char_dict[str1[i]] += 1
        else:
            char_dict[str1[i]] = 1
    for i in range(len(str2)):
        if str2[i] not in char_dict:
            return is_anagram
        else:
            char_dict[str2[i]] -= 1
    
    temp_sum = 0
    for key, value in char_dict.items():
        temp_sum += value
    
    if temp_sum == 0:
        is_anagram = True
        
    return is_anagram

print check_anagram("YUGESH", "HEUYSG")