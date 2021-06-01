# Binery Search
"""
binery search is works only for sorted solution Space/list.
"""

A = [1,22,44,55,66,77,88,120,151]

target = 88

def binery_search(A, target):

    left = 0
    right = len(A)-1

    while left <= right:
        mid = (left+right)//2

        if A [mid] == target:
            return mid
        elif A[mid] > target:
            right = mid -1
        else:
            left = mid -1        

    return None

A = [1,22,44,55,66,77,88,120,151]

target = 88

print(binery_search( A, target))