# Python | Cloning or Copying a list
# # Python program to copy or clone a list


def cloning(a):
    list_copy = a[:]
    return list_copy

if __name__=="__main__":
    list1 = [4, 8, 2, 10, 15, 18]
    list_copy = cloning(list1)
    print(cloning(list1))
    print(cloning(list_copy))



print("Using the extend() method")

def cloning(a):
    list_copy = []
    list_copy.extend(a)
    return list_copy

if __name__=="__main__":
    list1 = [4, 8, 2, 10, 15, 18]
    list_copy = cloning(list1)
    print(cloning(list1))
    print(cloning(list_copy))