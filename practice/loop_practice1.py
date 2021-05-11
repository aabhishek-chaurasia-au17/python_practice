
user_input = int(input("Enter a Number :"))

for i in range(1,user_input + 1):
    if i % 5 == 0 and i % 3 == 0:
        print(i,"FIZZ,FUZZ")
    elif i % 5 == 0:
        print(i,"FUZZ") 
    elif i % 3 == 0:
        print(i,"Fizz") 