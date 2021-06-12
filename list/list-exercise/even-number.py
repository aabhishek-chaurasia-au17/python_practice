# Python program to print even numbers in a list

def find_even(list1):

    for i in list1:
        if i % 2 == 0:
            print(i , end=" ")

list1 = [2, 7, 5, 64, 14]
find_even(list1)