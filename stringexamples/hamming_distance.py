#Hamming Distance between two strings

def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

print hamming_distance("geeksforgeeks", 'geeksandgeeks')