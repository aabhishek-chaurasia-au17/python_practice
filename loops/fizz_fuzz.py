

# n = int(input("enter the number"))

# for i in range(1,n) :
#     if (i % 3 == 0) and (i % 5 == 1):
#         print("fizz_fuzz")
#     elif i % 3 == 1:
#         print("fizz") 
#     elif i % 5 == 1:
#         print("fuzz")      
#     else:
#         print(i)  


# n = int(input("enter the number"))
# d = 2 
# flag = False
# while d < n:
#     if n % 2 == 0:
#         flag = True
#     elif n % 2 == 1:
#         print("Prime Number")  
        

#     if flag:
#         print("prime number")
#     else:
#         print("prime")    


n = int(input())
m = int(input())

if n == 1:
    sum = n+m
    print(sum)
elif n == 2:
    diff = n-m
    print(diff)
elif n == 3:
    prod = n*m
    print(prod)
elif n == 4:
    divid = n/m
    print(divid) 
elif n == 5:
    mod = n%m
    print(mod)  
elif n == 6:
     pass
else:
    print("Invalid Operation")
    


