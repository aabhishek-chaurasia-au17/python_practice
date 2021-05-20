"""
Given a sorted Integer array , Write a Program to search the target
element using Binary Search, If target element is found return the index .
Otherwise return -1 .
Input : arr = [1,2,3,15,16,19,23,55,1000] , target = 15
Output: - 3
Explanation:
Just Use Binary search method
Sample :
def Binarysearch(arr , target):
"""

arr = [1,2,3,15,16,19,23,55,1000]
target = 15
def Binarysearch(arr , target):
    low = 0
    high = len(arr)-1
    while (low<= high):
        for i in range (low,len(arr)):
            mid = (low+high)//2
            if target==arr[mid]:
                return 
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1
print(Binarysearch(arr,target))