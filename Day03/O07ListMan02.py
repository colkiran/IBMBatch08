
print("enumerate".center(60, "-"))

letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()
print("-" * 60)

for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)

for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"{ind}\t{lst}")

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for i, l in enumerate(lst):
        print(f"\t{i}\t{l}")

print("-" * 60)
l1 = []
print(dir(l1))

