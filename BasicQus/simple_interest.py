"""
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
"""
# EXAMPLE1:
# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500
# We need to find simple interest on 
# Rs. 10,000 at the rate of 5% for 5 
# units of time.

# EXAMPLE2:
# Input : P = 3000
#         R = 7
#         T = 1
# Output :210
# -------------------------------------------------------------

def simpleinterest(a,b,c):
    print("the principle is",a)
    print("the time period is",b)
    print("the intrest rate is",c)

    i = (a*b*c)/100
    print("The Simple Interest is",i)
    
simpleinterest(20,6,5)    
