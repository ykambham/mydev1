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


#Find the missing number in a string of numbers with no separator
# e.g. 89101113 Missing = 12 (8, 9, 10, 11, 13)

def find_missing_numer(num1):
    i = 1
    j = 0
    while i < 6 :
        Find = True
        while j+i < len(num1):
            a = int(num1[j:j+i])
            b = int(num1[j+i:j+i+i])
            if b - a > 2 or b - a <0:
                i += 1
                j = 0
                Find = False
                break
            else:
                if b - a == 2:
                    missing_Number = a + 1
                j += i
        if Find:
            print "Missing Number is:",missing_Number
            break


find_missing_numer("59606163")


# print all occurances of a given characters a, b, c
def print_occcrences(chars, length):
    pass


print print_occcrences(['a', 'b', 'c'], 3)
