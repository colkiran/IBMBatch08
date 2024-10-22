"""
int
float
complex
"""

a = 100
b = -100

print(f"a :{a}")
print(type(a))              # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)

c = 100.0
d = -100.9
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)

g = 100+2j
h = 100-5j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(27, 18, 10, 15, 12, 20)
print("MAX :", max(27, 18, 10, 15, 12, 20))
print("Min :", min(27, 18, 10, 15, 12, 20))

print("-" * 60)
x = 2 + 3.5
print(f"x :{x} \t {type(x)}")

x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("Conversion".center(60, "-"))
a = -100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)           # decimal
print(0b11)         # binary  1 * 2 ** 1 + 1 * 2 ** 0
print(0b101)        # binary
print(0o11)         # octal
print(0o111)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
