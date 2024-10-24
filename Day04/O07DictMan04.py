
print("copy".center(60, "-"))

d1 = {'name': 'sachin', 'age': 34, 'runs': 35}
print(f"d1 before :{d1}")

# copy d1 to d2
d2 = d1         # shallow copy, copies the address with the data

print(f"d2 before:{d2}")

d2['oppn'] = 'PAK'
d2['venue'] = 'Chinnaswamy'

print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("-" * 60)
print("-" * 60)

d3 = {'name': 'sachin', 'age': 34, 'runs': 35}
print(f"d3 before :{d3}")

# copy d3 to d4
d4 = d3.copy()

print(f"d4  before :{d4}")

d4['oppn'] = 'PAK'
d4['venue'] = 'Chinnaswamy'

print(f"d4 after :{d4}")
print(f'd3 after :{d3}')

print("-" * 60)
print("-" * 60)

d5 = {'name': 'sachin', 'age': 34, 'runs': {'pak':135, 'aus': 85, 'zim': 92}}
print(f"d5 before :{d5}")

# copy d5 to d6

d6 = d5.copy()

print(f'd6 before :{d6}')

d6['runs']['ken'] = 0
d6['runs']['nzl'] = 65

print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

print("-" * 60)
print("-" * 60)

d7 = {'name': 'sachin', 'age': 34, 'runs': {'pak':135, 'aus': 85, 'zim': 92}}
print(f"d7 before :{d7}")

# copy d7 to d8
from copy import deepcopy

d8 = deepcopy(d7)

print(f'd8 before :{d8}')

d8['runs']['ken'] = 0
d8['runs']['nzl'] = 65

print(f'd8 after :{d8}')
print(f'd7 after :{d7}')