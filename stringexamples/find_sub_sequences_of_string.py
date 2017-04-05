# Find subsequence of a^nb^iC^j n, i, k >=1
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
