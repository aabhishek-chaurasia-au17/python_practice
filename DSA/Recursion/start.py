
# Recursion
"""
function calling themself
"""
# def hello():

#     print("Hi")
#     hello()

# hello()

# if i want hi to be printed 3 times

count=0
def hello1():
    global count
    if count == 3:
        return
    print("Hi")
    count += 1
    hello1()

hello1()