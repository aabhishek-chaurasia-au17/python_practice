# Python program to print all positive numbers in a range

def positive_num(start,end):

    for i in range(start, end+1):
        if i >= 0:
            print(i, end=" ")


if __name__=="__main__":
    start = -4
    end = 5
    positive_num(start,end)    