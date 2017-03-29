# Fins subsequence of a^nb^iC^j n, i, k >=1
# e.g. in abbc sub sequences are abc, abc, abbc

def find_sub_sequence(str1):
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    for i in range(len(str1)):
        if str1[i] == 'a':
            a_cnt = 1 + 2 * a_cnt
        elif str1[i] == 'b':
            b_cnt = a_cnt + 2 * b_cnt
        elif str1[i] == 'c':
            c_cnt = b_cnt + 2 * c_cnt
    return c_cnt

str1 = 'abcabc'
print find_sub_sequence(str1)

# Sum of all sub strings 
# Complexity o(n2)
def sub_strings(str1):
    sub_strings_list = []
    for i in range(len(str1)):
        for j in range(i, len(str1) + 1):
            sub_strings_list.append(str1[i:j])
    return sub_strings_list

def sum_of_sub_strings(str1):
    return sum(int(a) for a in sub_strings(str1) if a)

# Same problem with complexity O(n))
'''
For above example,
sumofdigit[3] = 4 + 34 + 234 + 1234
           = 4 + 30 + 4 + 230 + 4 + 1230 + 4
           = 4*4 + 10*(3 + 23 +123)
           = 4*4 + 10*(sumofdigit[2])
In general, 
sumofdigit[i]  =  (i+1)*num[i] + 10*sumofdigit[i-1]
'''

def sum_of_sub_strings1(str1):
    sum_of_digit = {}
    sum_of_digit[0] = int(str1[0])
    sum = sum_of_digit[0]
    for i in range(1, len(str1)):
        sum_of_digit[i] = (i+1) * int(str1[i]) + 10 * sum_of_digit[i-1]
        sum += sum_of_digit[i] 
    return sum
import time
t1 = time.time()
print sum_of_sub_strings("12345")
print time.time() - t1
t2 = time.time()
print sum_of_sub_strings1("12345")
print time.time() - t2
    