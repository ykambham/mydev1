# largest repeating palindrome
testString = "forgeeksskeegfor"
stringLenth = len(testString)
def palindrome(subString):
    if subString == subString[::-1]:
        if len(subString) > 1:
            return subString
substrings = []   
i = 0
while i < stringLenth:
    j = 0
    while j < stringLenth:
        substrings.append(testString[i: j])
        j += 1
    i += 1

palindromes = []
for a in substrings:
    if palindrome(a):
        palindromes.append(a)

maxLength = max(len(a) for a in palindromes)
answer = [a for a in palindromes if len(a) == maxLength]
print answer