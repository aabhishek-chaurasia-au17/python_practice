
# Remove multiple elements from a list in Python

def Remove_ele(a):

    for i in a:
        if i % 2 == 0:
            a.remove(i)
    
    return a


if __name__ == "__main__":
    list1 = [11, 5, 17, 18, 23, 50]
    print(Remove_ele(list1))
