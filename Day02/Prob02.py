n = 0
for i in range(150, 49, -1):
    cntr = 0
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        n += 1

print(f"\nThere are {n} prime numbers between 150 and 50")




"""
prime_number = []
for num in range(50, 151):
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_number.append(num)

count = len(prime_number)
print("Prime numbers between 50 and 150:", prime_number)
print("Count of prime numbers:", count)

"""