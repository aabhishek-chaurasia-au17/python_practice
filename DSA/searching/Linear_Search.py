# Python Program for Linear Search
"""
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
        x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
        x = 175;
Output : -1
Element x is not present in arr[].
"""

def linear_search(arr):
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1        
        


if __name__ == "__main__":

    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    x = 110

    print(linear_search(arr))