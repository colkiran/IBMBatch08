
# c style formatting printf

st = "Welcome %s, what a %s player"
val = ("Sachin", "superb")              # tuples
print(st, val)

print("-" * 60)
print(st % val)

print("-" * 60)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))
print("Welcome %s, with a rating of %d what a %s player" % ("Sachin", 9, "class"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Sachin", 9.823742, "class"))
print("Welcome %s, with a rating of %.2f what a %s player" % ("Sachin", 9.823742, "class"))
print("Welcome %s, with a rating of %.0f what a %s player" % ("Sachin", 9.823742, "class"))

print("-" * 60)
# Unix Shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name = "Sachin", adj = "superb"))

print("-" * 60)
# python string format => st.format()

print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {2}, what a {0} player for {1}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))
print("Welcome {pname}, what a {adj} player for {ctry}".format(pname = "Sachin", adj="superb", ctry="India"))

print("-" * 60)

print("Welcome {pname}, with a rating {rating} what a {adj} player for {ctry}".format(pname = "Sachin", rating=9, adj="superb", ctry="India"))

print("Welcome {pname}, with a rating {rating:.3f} what a {adj} player for {ctry}".format(pname = "Sachin", rating=9.8965234, adj="superb", ctry="India"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI = {}  and Eulers constant = {}".format(pi, e))
print("PI = {} and Eulers constant = {e}".format(pi, e=e))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']         # list
print(f"full_name :{full_name}")
print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]}".format(name=full_name))
print("Mr.{name[1]}".format(name=full_name))

print("-" * 60)
import math
print(__name__)

print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant e = {mod.e}".format(mod=math))
