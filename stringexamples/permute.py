# This solution is without itertools
# with itertools do below steps
# import itertools
#[a for a in itertools.permutations(numbers)]
def permute(a_list):
    length=len(a_list)
    if length <= 1:
        yield a_list
    else:
        for n in range(0,length):
            for end in permute(a_list[:n] + a_list[n+1:]):
                yield [a_list[n]] + end

print [item for item in permute([1, 2, 3])]

# Python library way to get all_combinations with repeats
def all_combinations(a_list, repeat):
    pools = [a_list] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield prod
 
print [item for item in all_combinations([1, 2, 3], 3)]

'''
Output of result in each iteration:
[[1], [2], [3]]

[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

[[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1], [1, 3, 2], 
[1, 3, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 3, 1], 
[2, 3, 2], [2, 3, 3], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 2, 1], [3, 2, 2], [3, 2, 3], 
[3, 3, 1], [3, 3, 2], [3, 3, 3]]
'''