# Python | Matrix Product
"""
The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
The total element product in lists is : 1622880
"""

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : ", test_list)

# using list comprehension + loop
# Matrix Product
res = prod([ele for sub in test_list for ele in sub])

# print result
print("The total element product in lists is : ", res)
