# Find substring in a string
name = "i am an employee at HPE"
if name.find("am"):
    print name.index("am")
    

    
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
        
# Permutations of numbers
numbers = [3, 5, 8, 10]
import itertools
print [a for a in itertools.permutations(numbers)]

from permute import permute
result = []
for x in permute(numbers):
    result.append(x)
print result