#Efficiently check if a string has duplicates without using any additional data structure
def check_duplicates(str1):
    for i in range(len(str1)):
        for j in range(i + 1, len(str1)):
            if str1[i] == str1[j]:
                return True
    return False


print check_duplicates("aaabbccc")
print check_duplicates("abcd")