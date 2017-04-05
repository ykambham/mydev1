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