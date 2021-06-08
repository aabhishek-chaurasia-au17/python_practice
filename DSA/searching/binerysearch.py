
def binerysearch(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid +1

    return None               




arr = [1,3,4,6,8,9,11,14,16]
target = 11

print(binerysearch(arr, target))