# This solution is without itertools
# with itertools do below steps
# import itertools
#[a for a in itertools.permutations(numbers)]
def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
            for end in permute(LIST[:n] + LIST[n+1:]):
                yield [LIST[n]] + end

# Python library way to get all_combinations with repeats
def all_combinations(*args, **kwds):
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
for item in  all_combinations([1, 2, 3], repeat=3):
    print item

'''
Output of result in each iteration:
[[1], [2], [3]]

[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

[[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1], [1, 3, 2], 
[1, 3, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 3, 1], 
[2, 3, 2], [2, 3, 3], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 2, 1], [3, 2, 2], [3, 2, 3], 
[3, 3, 1], [3, 3, 2], [3, 3, 3]]
'''