# given a list search for an item in it Banana?

list = ["apple", "mango", "kivi", "Banana", "Greaps"]

target = "Banana"

def searching():
    
    for fruit in list:
        if fruit == target:
            return True
        
    return False

print(searching())


