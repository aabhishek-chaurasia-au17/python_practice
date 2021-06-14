
# Python | Sum of number digits in List

# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

print("----------- Try 1 -------------")

def num_digits(a):

    for b in a:
        sum = 0
        for i in str(b):
            sum += int(i)
        list2.append(sum)
    
if __name__=="__main__":
    list1 = [12, 67, 98, 34]
    list2 = []
    num_digits(list1)
    print(list2)

print("----------- Try 2 -------------")

def Sum_number(test_list):
    
    for ele in test_list:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)        
    return res

if __name__=="__main__":

    test_list = [12, 67, 98, 34]
    res = []
    print(Sum_number(test_list)) 