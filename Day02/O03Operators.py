
print("Arithmetic Operators".center(60, "-"))
print(f"Add 20 + 8 = {20 + 8}")
print(f"Sub 20 - 8 = {20 - 8}")
print(f"Mul 20 * 8 = {20 * 8}")
print(f"Div 20 / 8 = {20 / 8}")
print(f"Flr_div 20 // 8 = {20 // 8}")    # floor division
print(f"Mod 20 % 8 = {20 % 8}")
print(f"Exp 20 ** 2 = {20 ** 2}")

print("Augmentor Operator".center(60,"-"))
# =, +=, -=, *=, /=

x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
a = 10
b = 15

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(8, "-"))

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 2 and 2 == 2 :{1 == 2 and 2 == 2}")
print(f"1 == 2 and 2 == 1 :{1 == 2 and 2 == 1}")

print("-" * 60)
# OR operator
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 2 == 2 :{1 == 2 or 2 == 2}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")
print("-" * 60)
#not Operator
# ------------
print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 2 or 2 == 2) :{not(1 == 2 or 2 == 2)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('A') :{ord('A')}")      # ascii value of characters
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z' :{ord('z')}")

print("-" * 60)
# vice versa
print(f"chr(65)  :{chr(65)}")
print(f"chr(90)  :{chr(90)}")
print(f"chr(97)  :{chr(97)}")
print(f"chr(122) :{chr(122)}")

print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 = {5 | 3}")
print(f"5 & 3 = {5 & 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"8 << 1 = {8 << 1}")
print(f"5 << 2 = {5 << 2}")
print(f"16 >> 1 = {16 >> 1}")

print("Ternary Operator".center(60, "-"))
frt1 = "Apple"

wgt = 4
cst = 345


print(f"We got a discount of 20% on {frt1} as there was a discount on purchases more than 3 kgs, for 5 kgs we paid : "
      f"{wgt * cst * 0.8 if wgt > 3 else wgt * cst}")

print("-" * 60)

age = 18
print("Eligible" if age > 17 else "Not Eligible")
