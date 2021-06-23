# Python Program for Reversal algorithm for array rotation

"""
Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output : arr[] = [3, 4, 5, 6, 7, 1, 2]
"""

def reversal(arr, d, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end -1 
        
def leftrotat(arr,d):
    n = len(arr)
    reversal(arr,0, d-1)
    reversal(arr,d, n-1)
    reversal(arr,0, n-1) 

def printarry(arr):
    for i in range(0, len(arr)):
        print (arr[i])       

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7]
    reversal(arr, 2)
    print(printarry(arr))