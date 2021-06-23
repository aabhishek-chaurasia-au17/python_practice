# Python Program for Binary Search (Recursive and Iterative)




def Binary_search(arr,x):
    
    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) //2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            right = mid -1

        else:
            left = mid +1    

    return -1

if __name__ == "__main__":

    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    x = 80
    print(Binary_search(arr,x))

