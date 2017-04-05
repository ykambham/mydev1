'''
String with additive sequence
Input : s = 235813
Output : true
2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13

Input : s = 199100199
Output : true
1 + 99 = 100, 99 + 100 = 199

Input : s = 12345678
Output : false
'''


def additive_series(str1):
    sum = 0
    index = 1
    start = 0
    cur = ''
    for i in range(1, len(str1), index):
        for j in range(i+1, len(str1)+1, index):
            a = str1[start:i]
            b = str1[i:j]
            sum = int(a) + int(b)
            for k in range(j+1,len(str1)+1):
                if sum == int(str1[j:k]):
                    cur =  str1[0:k]
                    index = max(len(a), len(b))
                    start += index
                    i += index
                    print a, b, sum, cur, index
            if cur == str1:
                return True
    return False


print additive_series("1123581321") 
'''
1 1 2 112 1
1 2 3 1123 1
2 3 5 11235 1
3 5 8 112358 1
5 8 13 11235813 1
8 13 21 1123581321 2
'''
print additive_series("252651")
'''
25 26 51 252651 2
'''
print additive_series("123456")
'''
1 2 3 123 1
'''