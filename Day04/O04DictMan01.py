
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 32, 'runs': 123, 'oppn': "WI"}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 29), ('runs', 87), ('oppn', 'eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name="virat", age = 23, runs=63, oppn="Aus")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'sachin', 'age': 32, 'runs': 120, 'oppn': 'WI'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modification, adding new value
player['name'] = "Tendulkar"
player['runs'] = 98

player['venue'] = 'Sabina Park'
player['year'] = 2003

print(f"player :{player}")

print("-" * 60)
# delete
print(f"player: {player}")
del player['age']
del player['oppn']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
