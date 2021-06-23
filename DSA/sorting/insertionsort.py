# Python Program for Insertion Sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return key

if __name__ == "__main__":

    arr = [20, 5, 4, 12, 84, 3, 89, 78, 50]
    for i in range(len(arr)):
        print("%d" %arr[i])
    insertion_sort(arr)
