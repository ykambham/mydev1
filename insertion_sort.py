#  Time Complexity of Solution:
#  Best O(n); Average O(n^2); Worst O(n^2).
#
#  Approach:
#  Insertion sort is good for collections that are very small
#  or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much. Each time an insertion is made,
#  all elements in a greater position are shifted.
#======================================================================= 
def insertionsort(aList):
  for i in range(1, len(aList)):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp