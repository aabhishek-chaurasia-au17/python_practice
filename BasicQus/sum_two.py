
"""
Given two integer numbers return their product. 
If the product is greater than 1000, then return their sum.
"""

def product(a,b):

    prod = a*b
    
    if prod < 1000:
        return prod
    else:
        return a+b   
    
a = 20
b = 30

print(product(a,b))