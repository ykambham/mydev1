'''
Perfect reversible string
You are given a string str, the task is to check that reverses of all possible substrings of str are present in str or not.
'''

def get_all_subsrings(str1):
    return [str1[i:j+1] for i in range(len(str1)) for j in range(i, len(str1))]

def check_if_substrings_reversible(str1):
    sub_strings = get_all_subsrings(str1)
    print sub_strings
    for each_string in sub_strings:
        if each_string[::-1] not in str1:
            return False, each_string
    return True
        
print check_if_substrings_reversible("abab")