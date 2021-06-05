


# fruit = [ "apple", "Banana", "kivi", "mango", "watermelon"] 

# trget = "mango"

# def linear_search(fruit, target):

#     for i in fruit:
#         if i == target:
#             return True

#     return False        



# fruit = [ "apple", "Banana", "kivi", "mango", "watermelon"] 

# target = "mango"

# print(linear_search(fruit, target))




def linear(a, target):

    for i in range(len(a)):
        if a[i] == target:
            return i

    return -1

a = [2,5,8,9,7,10,1]
target = 11
print(linear(a, target))