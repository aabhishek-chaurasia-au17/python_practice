# Reverse a given list in Python


print("Method 1")

def Reverse_list(a):

    a = a[::-1]
    return a

aLsit = [100, 200, 300, 400, 500]

print(Reverse_list(aLsit))


print("Method 2")

def Reverse_list(a):

    a.reverse()
    return a

aLsit = [100, 200, 300, 400, 500]

print(Reverse_list(aLsit))
