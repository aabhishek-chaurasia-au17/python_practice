
# list = [29]


# list.append(1)
# list.append(6)
# list.append(10)
# list.append(8)
# list.append(9)
# list.append(2)
# list.append(12)
# list.append(7)
# list.append(3)
# list.append(5)
# list.insert(8,66)
# list.insert(1,30)
# list.insert(6,75)
# list.insert 4 44
# list.insert 9 67
# list.insert 2 44
# list.insert 9 21
# list.insert 8 87
# list.insert 1 75
# list.insert 1 48
# print(list)


# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))

def print_rangoli(size):
    
    alpha = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

