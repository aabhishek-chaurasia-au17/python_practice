"""
Python Program to find largest element in an array

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
"""

def largest_arry(arr,a):
    max = 0
    for i in range(1, a):
        if arr[i] > max:
            max = arr[i]
    return  max


arr = [20, 10, 20, 4, 100]
a = len(arr)
print(largest_arry(arr,a))
