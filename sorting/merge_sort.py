# Time Complexity of Solution:
#  Best = Average = Worst = O(nlog(n)).
#
#  Approach:
#   Merge sort is a divide and conquer algorithm. In the divide and
#   conquer paradigm, a problem is broken into pieces where each piece
#   still retains all the properties of the larger problem -- except
#   its size. To solve the original problem, each piece is solved
#   individually; then the pieces are merged back together.
#
#   For illustration, imagine needing to sort an array of 200 elements
#   using selection sort. Since selection sort takes O(n^2), it would
#   take about 40,000 time units to sort the array. Now imagine
#   splitting the array into ten equal pieces and sorting each piece
#   individually still using selection sort. Now it would take 400
#   time units to sort each piece; for a grand total of 10400 = 4000.
#   Once each piece is sorted, merging them back together would take
#   about 200 time units; for a grand total of 200+4000 = 4,200.
#   Clearly 4,200 is an impressive improvement over 40,000. Now
#   imagine greater. Imagine splitting the original array into
#   groups of two and then sorting them. In the end, it would take about
#   1,000 time units to sort the array. That's how merge sort works.
#
#  NOTE to the Python experts:
#     While it might seem more "Pythonic" to take such approach as
#
#         mid = len(aList) / 2
#         left = mergesort(aList[:mid])
#         right = mergesort(aList[mid:])
#
#     That approach take too much memory for creating sublists.
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)