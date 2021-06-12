
# Python program to find second largest number in a list

# def find_seconde(list1):

#     list1.sort()
#     return list1

# list1 = [70, 11, 20, 4, 100]

# print(find_seconde(list1[:-2]))

print()

list2 = [10, 20, 4, 45, 99]
newlist = set(list2)
newlist.remove(max(newlist))
print(max(newlist))


