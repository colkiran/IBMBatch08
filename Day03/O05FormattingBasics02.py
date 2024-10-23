
# conversions
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))
print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 3656124697))
print("{num:10} {num:f} {num:b}".format(num = 36))

print("-" * 60)
print("{num:15} Tendulkar".format(num=3))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("One Googol is {}".format(10 ** 100))
print("One Googol is {:,}".format(10 ** 100))

print("-" * 60)
print("{}".format(pi))
print("{:010.2f}".format(pi))
print("{:010.3f}".format(pi))
print("{:010.4f}".format(pi))

print("-" * 60)
print("{:>15} Tendulkar".format("Sachin"))           # right alignment
print("{:^15} Tendulkar".format("Sachin"))           # center alignment
print("{:<15} Tendulkar".format("Sachin"))           # left alignment

print("-" * 60)
print("{:-^60}".format("Sachin Tendulkar"))
print("Sachin Tendulkar".center(60, "-"))

print("-" * 60)
print("{0:^10} \t {1:>15}".format("Sachin", "Tendulkar"))

