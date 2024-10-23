
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13, 14])
print(f"l1 :{l1}")
print(f"l1[-1][2:5] :{l1[-1][2:5]}")

print("extend".center(60, "-"))
l2 = [2, 4, 6, 8, 10]
print(f"l2 :{l2}")

l2.extend([12, 14, 16, 18])
print(f"l2 :{l2}")

l2.extend([20])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)


print(f"l1 :{l1}")
