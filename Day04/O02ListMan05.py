
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the values of l1 to l2
l2 = l1         # shallow copy - copies the address with data

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-"  * 60)
print("-"  * 60)

l3 = [5, 6, 7, 8, 9]
print(f"l3 before :{l3}")

# copy l3 into l4
l4 = l3.copy()     # deep copy - copies only the data

print(f"l4 before :{l4}")

l4.extend([10, 11, 12, 13])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("-"  * 60)
print("-"  * 60)

l5 = [10, 20, 30, [1, 2, 3, 4, 5], 30, 40, 50]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()

print(f"l6 before :{l6}")

l6[3].append(6)
l6[3].append(7)
l6[3].append(8)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("-"  * 60)
print("-"  * 60)

l7 = [2, 4, [5, 10, 15, 20, 25], 6, 8, 10]
print(F"l7 before:{l2}")

# copy the values l7 to l8
from copy import deepcopy

l8 = deepcopy(l7)

l8[2].append(30)
l8[2].append(35)
l8[2].append(40)
l8[2].append(35)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

