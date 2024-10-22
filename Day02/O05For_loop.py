
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(1, 15, 2):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 60)
# continue - to skip the current iteration
# break  - to stop the iteration
# else

for i in range(1, 31):
    # if i > 25:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\nCompleted iterating.....")

