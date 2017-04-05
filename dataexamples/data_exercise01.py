def collections_test():
    aList = [1, 2, 4, 6, 8, 9, 12, 13]
    print filter(lambda x: x%2, aList)
    print map(lambda x: x*2, aList)
    print reduce(lambda x, y: x + y, aList)
    print {n: n**2 for n in aList}
    print [n*2 for n in aList]
    print aList[5:]
    print aList[::-1]
    
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]
    print A0
    print A1
    print A2
    print A3
    print A4
    print A5
    print A6
collections_test()

import os
def print_directory_contents(dir):
    if os.path.isdir(dir):
        for child in os.listdir(dir):
            childPath = os.path.join(dir, child)
            if os.path.isdir(child):              
                print_directory_contents(childPath)
            else:
                print childPath


print_directory_contents(os.path.abspath('/home/ykambham/workspace/Testing'))

def f(*args, **kwargs):
    print (args, kwargs)

print f(3)
print f(3, 4)
print f(3, {'a': 1, 'b': 2})
print f(3, {'a': 1, 'b': 2}, name="yugesh")
print f(range(10))


bList = [1, 1, 3, 4, 6, 6, 6, 7, 7, 7, 7, 7, 9]
import collections 
cnt = collections.Counter
print cnt(bList)
testString = 'aaabnbnbsdambmbasmbdmas'
print cnt(testString)
cDict = {'a':1, 'b':2, 'c':3, 'd':4}
print cnt(cDict)
print collections.OrderedDict(cDict)

if 2 in cDict.values():
    print "key found"

def read_file():
    with open('/home/ykambham/workspace/MOCK_DATA.csv', "r") as fileText:
        for eachLine in fileText:
            if eachLine:
                columns = eachLine.split(',')
                if "Female" in columns and int(columns[0]) > 999:
                    print columns[0], columns[1], columns[3], columns[5]
import cProfile

profile = cProfile.Profile()
profile.enable()
read_file()
profile.disable()
profile.print_stats(sort="time")

import unittest

class test_cases(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName=methodName)
        self.testData = '1,Gerald,Green,ggreen0@google.it,Male,220.186.134.201'.split(',')
    def test_case1(self):
        self.assertIsNotNone(self.testData[0], "Id is None")
    def test_case2(self):
        self.assertIsNot(self.testData[1], str, "Name is not string")

unittest.main()


test1 = "I am a good boy, I need a good pen and good circle"
cnt2 = Counter()
print cnt2(test1)
