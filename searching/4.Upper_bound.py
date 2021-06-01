# Upper bound


def upper_bound(arry, target):
    prev = len(arry)
    for i in range(len(arry)-1, 0, -1):
        if arry[i] == target:
            return i
        elif arry[i] < target:
            return prev
        prev = i    


arry = [1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6]
target = 2

print(upper_bound( arry, target))