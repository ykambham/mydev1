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