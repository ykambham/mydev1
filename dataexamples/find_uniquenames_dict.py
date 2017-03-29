names = ["yugesh", "ram", "sam", "raghu", "yugesh","sam"]

import collections 
for name, count in collections.Counter(names).items():
    if count == 1:
        print name 

# Not using in built libraries
def find_unique_names(names):
    unique_names = []
    names_dict = {}
    for name in names:
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1
    
    for key, value in names_dict.items():
        if value == 1:
            unique_names.append(key)
    return unique_names

print find_unique_names(names)