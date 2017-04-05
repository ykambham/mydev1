# Check if the string is a palindrome by removing just one letter
def is_palindrome(str1):
    if str1 == str1[::-1]:
        return True

def check_if_palindrome_possible(str1):
    for i in range(len(str1)):
        if is_palindrome(str1[:i] + str1[i+1:]):
            return str1[i]

print check_if_palindrome_possible("abcbea")