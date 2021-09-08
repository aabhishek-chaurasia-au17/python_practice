
def binery(A, target):

    left = 0
    right = len(A)-1

    while left < right:
        mid = (left + right)//2

        if A[mid] == target:
            return mid

        elif A[mid] > target:
            right = mid-1

        else:
            left = mid + 1

    return -1 

A = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 11
print(binery(A, target))

