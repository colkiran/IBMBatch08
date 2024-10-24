"""
sort   - sort will sort the original list
sorted - sorted will take a copy of the list and sorts it
"""
print("sort".center(60, "-"))
l1 = [8, 10, 5, 7, 1, 9, 2, 4, 6, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print("Ascending order :", res_asc)

res_desc = sorted(l1, reverse=True)
print("Descending order :", res_desc)

print("-" * 60)
l1 = [8, 'zebra', 10,'apple',  5, 'xray', 'blue', 7, 'white', 'dog', 1, 'violet', 'green', 9, 'pink', 'maroon', 2, 'egg', 'night', 4, 'orange', 'queen', 6, 'hen', 'cat', 3, 134, 1782, 28, 213, 2097]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(F"res :{res}")

for i in range(1, len(res)):
    if type(res[i]) == int:
        # print(i)
        break

print("-" * 60)
print(res[:16] + sorted(res[16:]))
print("-" * 60)

cities = ['thiruvananthapuram', 'chennai', 'bangalore', 'delhi', 'hyderabad', 'mumbai', 'ooty', 'kolkota', 'vishakapatnam', 'pune']

print(f'cities :{cities}')
# sort the cities in ascending order of their length

print("-" * 60)
res = sorted(cities, key=len)
print(f"res :{res}")

print("reverse".center(60, "-"))

l1 = [8, 10, 5, 7, 1, 9, 2, 4, 6, 3]
print(f"l1 :{l1}")

# reverse, reversed
print("-" * 60)
res = list(reversed(l1))
print(f"res :{res}")

print("-" * 60)
l1.reverse()
print(f"l1 :{l1}")

