#Array inversion indicates how far the array is from being sorted.
#Inversions are pairs of elements in array that are out of order.

def count_inversions(array):
    inversions = 0
    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                inversions += 1
    return inversions


print("res is %s" % count_inversions([6,5,4,3,3,3,3,2,1]))