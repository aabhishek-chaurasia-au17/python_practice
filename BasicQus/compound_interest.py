"""
Python Program for compound interest
"""
# Formula to calculate compound interest annually is given by: 
# A = P(1 + R/100) t 
# Compound Interest = A – P 
# Where, 
# A is amount 
# P is principle amount 
# R is the rate and 
# T is the time span
# Ex:
# Input : Principle (amount): 1200
#         Time: 2
#         Rate: 5.4
# Output : Compound Interest = 133.099243

def compound_interest(p,r,t):
    
    print("principle amount is",p)
    print("rate of intrest is",r)
    print("the time span is",t)

    a = p*(pow((1+r/100),t))
    ci = a - p
    print("Compound Interest",ci)

compound_interest(10000,10.5,5)
