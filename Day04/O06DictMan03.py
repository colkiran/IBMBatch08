
print("setdetfault".center(60, "-"))
# used to add new key value pairs into the dictionary

player = {'name': 'Rahul', 'age': 32, 'runs': 65, 'oppn': 'Eng'}
print(f"player :{player}")

player.setdefault('name', "Dravid")
player.setdefault('runs', 90)

player.setdefault('venue', 'lords')
player.setdefault('tournmnt', 'WC')

print(f"player :{player}")

print("-" * 60)
fruits = ['apple', 'orange', 'grapes', 'apple']
print(f"fruits :{fruits}")

counts = {}
for fruit in fruits:
    counts.setdefault(fruit, 0)
    counts[fruit] += 1

print(counts)

print("pop".center(60, "-"))

player = {'name': 'Rahul', 'age': 32, 'runs': 65, 'oppn': 'Eng'}
print(f"player :{player}")

res = player.pop('age')
print(f"res :{res}")

res = player.pop('oppn')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(60,  "-"))

player = {'name': 'Rahul', 'age': 32, 'runs': 65, 'oppn': 'Eng'}
print(f"player :{player}")

res = player.popitem()
print(res)

res = player.popitem()
print(res)

print(f"player :{player}")

print("update".center(60, "-"))

emp1 = {'empid': 101, 'ename': 'Peter', 'age': 35, 'desig': 'MGR', 'salary': 96000}

emp2 = {'empid': 242, 'ename': 'Tina', 'age': 30, 'desig': 'BDE', 'dept': 'MKT'}

print("-" * 60)
print(f"emp1 :{emp1}")

print("-" * 60)
print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(60 ,"-"))

emp2 = {'empid': 242, 'ename': 'Tina', 'age': 30, 'desig': 'BDE', 'dept': 'MKT'}
print(f"emp2 :{emp2}")

emp2.clear()
print(emp2)
