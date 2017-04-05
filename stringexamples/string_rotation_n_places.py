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