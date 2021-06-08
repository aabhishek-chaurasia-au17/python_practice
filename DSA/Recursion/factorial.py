# finding the factorial of a number using with recusion.

def factorial(n):
    """
    factorial n will find the factorial of a no n.
    """
    if n ==1:
        return 1
    
    fact = n* factorial(n-1)
    return fact   

if __name__=="__main__":
    
    print(factorial(5))





 