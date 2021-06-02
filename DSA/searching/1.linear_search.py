# given a list search for an item in it Banana?

# list = ["apple", "mango", "kivi", "Banana", "Greaps"]

# target = "Banana"

# def searching():
    
#     for fruit in list:
#         if fruit == target:
#             return True
        
#     return False

# print(searching())

def liner_search(fruit, target):
    for i in range(len(fruit)):
        if fruit[i] == target:
            return i
        
    return -1

fruit =[ "apple", "mango", "kivi", "banana"]
target = "kivi"    
print(liner_search(fruit, target))
