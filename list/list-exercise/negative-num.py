
# Python program to print negative numbers in a list

# def find_nagetive(a):

#     for i in a:
#         if i < 0:
#             print(i, end=" ")



# if __name__ == "__main__":
    
#     list1 = [12, -7, 5, 64, -14]
#     find_nagetive(list1)


print()


def find_negetive_num(list2):
    
    i = 0
    
    while (i < len(list2)):

        if list2[i] < 0:
            print(list2[i], end=" ")

        i+=1

list2 = [12, 14, -95, 3, -21] 
find_negetive_num(list2)   



