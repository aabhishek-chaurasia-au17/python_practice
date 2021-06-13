# Python program to find sum of elements in list

print("------------------ methoth 1 ------------------")

def find_sum(a):

    sum = 0
    for i in a:
        sum += i
    return sum

a = [17, 5, 3, 5]
print(find_sum(a))   


print("------------------- methoth 2 ------------------")

b = [12, 15, 3, 10]

total = sum(b)

print(total)