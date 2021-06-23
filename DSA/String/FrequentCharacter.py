# Python – Least Frequent Character in String

test_str = "geekforgeeks"

print("the original sating is", str(test_str))

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res = min(all_freq, key= all_freq.get)

print("Frequent Character in String is", res)
