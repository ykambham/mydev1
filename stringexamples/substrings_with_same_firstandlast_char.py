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
