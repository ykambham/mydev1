# Return the number that's not repeated even times
a = [1, 2, 3, 1, 2, 4, 4, 6, 6, 7, 7, 7, 7]
countDict = {}
for num in a:
    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1

for a in countDict:
    if countDict[a] == 1:
        print a
    

# Find substring in a string
name = "i am an employee at HPE"
if name.find("am"):
    print name.index("am")
    
    
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

# Ordering a set of people. each one knows who they should follow but lost
order = [{"name": 'a', "value": ''}, 
         {"name": 'd', "value": 'c'},
         {"name": 'c', "value": 'b'},
         {"name": 'b', "value": 'a'},]

for a in order:
    if not a.get("value"):
        startDict = a
orderList = []
orderList.append(startDict)
j = 0
i = 0
while i < len(order):
    for dict1 in order:
        if dict1.get('value') == orderList[j].get('name'):
            orderList.append(dict1)
            j += 1
    i += 1
print orderList
    
print(order.sort(key=lambda s: s['value']))

# lambda to multiply sales
sales = [1, 2, 3, 4, 5, 6]
newSales = map(lambda x: x**2, sales)
print newSales


# Return prime numbers in 50
nums = range(2, 50) 
for i in nums: 
    nums = filter(lambda x: x == i or x % i, nums)

print nums

# find longest repeating alphabet
xyz = "aaabbbccddddddddddddddddddddddeefyujgfakhdk"
count = len(xyz)
i = 0
countDict = {}
while i < count:
    if xyz[i] in countDict:
        countDict[xyz[i]] += 1
    else:
        countDict[xyz[i]] = 1
    i += 1
maxCount = 0
for k, v in countDict.items():
    if v > maxCount:
        maxCount = v
        maxItem = k
print maxItem, maxCount


# Remove duplicate elements in all lists but keep in same list
list1 = [1, 3, 7]
list2 = [2, 2, 4, 6]
list3 = [3, 5, 6]
list5 = list1 + list2 + list3

list4 = list(set(list1)&set(list2)) + list(set(list1)&set(list3)) + list(set(list3)&set(list2))
resultList = [x for x in list5 if x not in list4]
print sorted(resultList)


a='Beautiful, is; better*than\nugly'
import re
print re.split('; |, |\*|\n',a)

words = ['look', 'into', 'my', 'eyes', 'look', 'into',
'my', 'eyes', 'the', 'eyes', 'the', 'eyes',
'the', 'eyes', 'not', 'around', 'the', 'eyes',
"don't", 'look', 'around', 'the', 'eyes',
'look', 'into', 'my', 'eyes', "you're", 'under']

from collections import defaultdict

words_index = defaultdict(list)
n = 0 
for word in words:
    words_index[word].append(n)
    n += 1
print words_index

long_string = 'AAAZZZCCDDDDD'
import collections
output = ''
for word, count in collections.Counter(long_string).items():
    output += word + str(count)
print output


# Classes 
class Rectangle():
    length = 10
    width = 10
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
a = Rectangle(10, 20)
print a.area()
print getattr(a, 'length')
print delattr(a,'length')
print a
        
# print first non-repeating character in a string
a = 'geeksforgeek'
countList = collections.Counter(a).items()
smallestIndex = ''
smallestKey = ''
for key, count in countList:
    if count == 1:
        if a.index(key) <= smallestIndex:
            smallestIndex = a.index(key)
            smallestKey = key
print smallestKey, smallestIndex

# Permutations of numbers
numbers = [3, 5, 8, 10]
import itertools
print [a for a in itertools.permutations(numbers)]

#without itertools
def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
            for end in permute( LIST[:n] + LIST[n+1:] ):
                yield [ LIST[n] ] + end
result = []
for x in permute(numbers):
    result.append(x)
print result