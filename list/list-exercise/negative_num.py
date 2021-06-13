# Python program to print all negative numbers in a range

def negative_num(start, end):

    for i in range(start, end):
        if i < 0:
            print(i, end=" ") 


if __name__=="__main__":
    start = -4
    end = 5
    negative_num(start, end)