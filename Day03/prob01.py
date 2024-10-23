
# accept a number and display the no of times each digit is occurring
# 32409823482

from collections import Counter

num = "32409823482156156222233334444"
lst = []
for i in num:
    if i not in lst:
        lst.append(i)

print(f"lst :{lst}")
res = {}
for i in lst:
    res[i] = num.count(i)

print("-" * 60)

print(res)
res1 = Counter(num)
print(res1)

