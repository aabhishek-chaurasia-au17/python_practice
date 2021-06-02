"""
Problem: Given an array arr[] of n elements, 
write a function to search a given element x in arr[].
"""

# Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
# x = 175;
# Output : -1
# Element x is not present in arr[].

def find_linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i

    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 170
print(find_linear_search(arr, x))    