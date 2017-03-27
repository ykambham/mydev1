# Inserts data in buckets by the index 
# starts with last element and goes through each element
# Good only for certain data types
#  Time Complexity of Solution:
#  Best Case O(kn); Average Case O(kn); Worst Case O(kn),
#  where k is the length of the longest number and n is the
#  size of the input array.
#
#  Note: if k is greater than log(n) then an nlog(n) algorithm would
#  be a better fit. In reality we can always change the radix
#  to make k less than log(n).
aList = [123, 456, 321, 012, 490]
def radixsort(aList):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX

radixsort(aList)
print aList