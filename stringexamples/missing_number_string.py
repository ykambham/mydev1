#Find the missing number in a string of numbers with no separator
# e.g. 89101113 Missing = 12 (8, 9, 10, 11, 13)
# WEb method not working for all 
def find_missing_number(num1):
    i = 1
    j = 0
    missing_Number = 0
    while i < 6 :
        Find = True
        while j+i < len(num1):
            a = int(num1[j:j+i])
            b = int(num1[j+i:j+i+i])
            if b - a > 2 or b - a <0:
                i += 1
                j = i
                Find = False
                break
            else:
                if b - a == 2:
                    missing_Number = a + 1
                j += i
        if Find:
            print "Missing Number is:",missing_Number
            break
        
find_missing_number("8910111214")