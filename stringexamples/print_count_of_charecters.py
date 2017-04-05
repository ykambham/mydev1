long_string = 'AAAZZZCCDDDDD'
import collections
output = ''
for word, count in collections.Counter(long_string).items():
    output += word + str(count)
print output
