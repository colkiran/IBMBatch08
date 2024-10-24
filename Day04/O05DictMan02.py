
print("get".center(60, "-"))

player = {'name': 'Tendulkar', 'age': 32, 'runs': 98, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2003}
print(f"player :{player}")

print("-" * 60)
print(f"Name :{player.get('name', 'Invalid Key')}")
print(f"Runs :{player.get('rns', 'Invalid Key')}")

print("keys".center(60, "-"))

player = {'name': 'Tendulkar', 'age': 32, 'runs': 98, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2003}
print(f"player :{player}")

print("-" * 60)
k = player.keys()
print(k)

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print('values'.center(60, "-"))
player = {'name': 'Tendulkar', 'age': 32, 'runs': 98, 'oppn': 'WI', 'venue': 'Sabina Park', 'year': 2003}
print(f"player :{player}")

v = player.values()
print(v)

print("items".center(60, "-"))
# items =  keys + values

emp = {
    'emp1' :{'empid': 101, 'ename': 'Peter', 'age': 35, 'desig': 'MGR', 'dept': 'Finance', 'salary': 96000},
    'emp2' :{'empid': 242, 'ename': 'Tina', 'age': 30, 'desig': 'BDE', 'dept': 'MKT', 'salary': 60000},
    'emp3'  :{'empid': 330, 'ename': 'Abraham', 'age': 27, 'desig': 'SE', 'dept': 'IT', 'salary': 85000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for keys, info in emp.items():
    print(keys)
    print("-" * len(keys))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("fromkeys".center(60, "-"))
# used to convert a list into a dictionary
cities = ['blr', 'che', 'hyd', 'del', 'mum', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 21)
print(f"res2 :{res2}")
