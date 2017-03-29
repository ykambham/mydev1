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
            for end in permute( LIST[:n] + LIST[n+1:] ):
                yield [ LIST[n] ] + end