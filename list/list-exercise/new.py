
# Python | Sum of number digits in List

# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

def num_digits(a):
    sum = 0
    size = len(a)
    for i in range(0, size):
        sum += size[i]

    print(sum)

if __name__=="__main__":
    list1 = [12, 67, 98, 34]
    num_digits(list1)
