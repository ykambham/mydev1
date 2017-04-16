# Check if a string can become empty by recursively deleting a given sub-string

def check_strings(str1, str2):
    if str1 == str2:
        print "Can be emptied"
    else:
        if str1.find(str2) > 0:
            if len(str1) > 0:
                check_strings(str1.replace(str2, ''), str2)
        else:
            print "Not possible!"
            return

check_strings("geegeeksks", 'geeks')