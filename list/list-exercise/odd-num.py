
# Python program to print odd numbers in a List

def find_odd(a):

    i = 0
    while i < len(a):
        if a[i] % 2 != 0:
            print(a[i], end=" ")

        i+=1


list1 = [10, 21, 4, 45, 66, 93]

find_odd(list1)
