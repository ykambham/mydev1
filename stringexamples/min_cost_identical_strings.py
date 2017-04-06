'''
Input :  i = "abcd", j = "acdb", costi = 10, costj = 20.
Output:  30
For Making both strings identical we have to delete 
character 'b' from both the string, hence cost will
be = 10 + 20 = 30.
'''


def find_min_cost(str1, str2, costi=10, costj=20):
    cost = 0
    if len(str1) and len(str2) == 0:
        return 0
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    x = len(str1)
    y = len(str2)
    while x and y > 0:
        if str1[x-1] == str2[y-1]:
            x -= 1
            y -= 1
        else:
            if y > 1:
                y -= 1
                cost += costj
            else:
                x -= 1
                cost += costi
        print x, y
    return cost + x * costi + y* costj

print find_min_cost("abcd", "acdb")
print find_min_cost("ef", "gh")
print find_min_cost("xyz", "xzy")