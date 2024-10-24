
# remove, pop, clear
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1]

print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1= list(range(1, 31))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("count".center(60, "-"))
l1 = [1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2,2, 2, 2, 2, 2, 2,2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1,1, 2, 2, 2,2 ,2 , 2, 2, 2,2,2,2,2,2,2]

print(f"count of 1's :{l1.count(1)}")
print(f"count of 2's :{l1.count(2)}")
print(f"count of 3's :{l1.count(3)}")
print(f"count of 7's :{l1.count(7)}")

print("index".center(60, "-"))
l1 = [1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2,2, 2, 2, 2, 2, 2,2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1,1, 2, 2, 2,2 ,2 , 2, 2, 2,2,2,2,2,2,2]

print(f"l1 :{l1}")
print("-" * 60)

print("first 3  :", l1.index(3))
print("second 3 :", l1.index(3, l1.index(3) + 1))
print("Third 3  :", l1.index(3, l1.index(3, l1.index(3) + 1) + 1))


