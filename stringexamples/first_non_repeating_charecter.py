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
