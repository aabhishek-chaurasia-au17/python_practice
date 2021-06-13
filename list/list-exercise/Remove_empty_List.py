# Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]
b = []
for i in test_list:
    if i != []:
        # print(i, end=" ")
        b.append(i)

print(b)