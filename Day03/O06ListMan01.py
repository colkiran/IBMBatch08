
l1 = list()
print(f"l1 :{l1}")
print(type(l1))
print("-" * 60)

l2 = [1, 2, 3, 4, 5.2, 6.4, 7.093, 8.0, 9+3j, 10-4j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

# create
l1 = list(range(2, 15, 2))
print(f"l1 :{l1}")

# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

print("-" * 60)
for i in l1:
    print(i, end=" ")
print()


print("-" * 60)
for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("-" * 60)
# update - change, add new element
print(f"l1 :{l1}")

l1[3] = 800         # change
l1[5] = 1000        # insert

print(f"l1 :{l1}")

print("-" * 60)
# delete

del l1[2]
del l1[-1]

print(f"l1 :{l1}")

print("-" * 60)

values = list(range(10, 31, 10))

print(values)

# unpack list
a, b, c = values

print("-" * 60)
values = list(range(10, 101, 10))
print(values)

a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

print("-" * 60)
lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 60)
lst4 = [*lst1, *lst2]
print(lst4)
print(len(lst4))
