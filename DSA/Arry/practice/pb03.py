"""
sample input
3 1
1 2 3
sample output

# Print count of sub array which have exactly k even no. in a list
n = 3
k = 1 # even no in a list
array = [1,2,3]
Sub array are :
[1] 
[1,2]
[1,2,3]
[2]
[2,3]
[3]

sub array that haveonly 1 even number are :-> sum are :[1,2], [1,2,3], [2], [2,3] 
so the answer is - >  4

"""

n = 3
k = 1
a = [1,2,3]
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        count_even = 0
        for q in res:
            if q%2==0:
                count_even += 1
        if count_even == k:
            count_main += 1
print(count_main)


