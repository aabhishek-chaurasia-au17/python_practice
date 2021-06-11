# Python | Multiply all numbers in the list (4 different ways)

def multiply_list(a):
    
    total = 1
    for i in a:
        total *= i
    print(total) 

a = [1,2,3]

multiply_list(a)    