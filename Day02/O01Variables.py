"""
1. a variable should start with a letter or an underscore
2. we cannot use keywords as variable name - if, for, while
3. varaible name cannot start with a number
4. varaible names can have alphanumeric characters and underscore or hyphen
5. we cannot have spaces inbetween variable names
6. variable names are case-sensitive
"""
# cricket

player_count = 11
rating = 8.79
has_won_world_cup = True
team_name = "India"

# f string or format string - interpolation
print(f"Each team has {player_count} players")
# print("Each team has", player_count, "players")

print(f"The rating of this team is {rating}")

print(f"The team has won a world cup :{has_won_world_cup}")

print(f"This is team {team_name}")

print("-" * 60)

# current module name
print(__name__)  # double underscore name => dunder_name

# to implement formatting to the entire file - ctrl + alt + L
a, b, c = 1, 2, "hello"
print(a, b, c, sep=", ")
print(a, b, c, sep=" : ")

first_name = "Sachin"
last_name = "Tendulkar"
runs = 145
print("My name is " + first_name + " and I am also known as " + last_name)
print("My name is", first_name, "and I am also known as", last_name)

print("My name is " + first_name + " and I am also known as " + last_name + " with runs",  runs)

# interpolation
print(f"My name is {first_name} and I am alsp known as {last_name}")

print("-" * 60)

frt1 = "Apple"
frt2 = "Orange"
wgt = 5
cst = 345
print(f"{frt1}'s in available in all seasons than {frt2}")

print(f"We got a discount of 20% on {frt1} as there was a discount on purchases more than 3 kgs, for 5 kgs we paid : {wgt * cst * 0.8}")

print("-" * 60)
# strings are enclosed in "" or ''
team_name = "Royal Challengers"
print(team_name)

team_name = "Royal 'Challengers'"
print(team_name)

team_name = 'Royal "Challengers"'
print(team_name)

team_name = 'Royal \'Challengers\''
print(team_name)


print("=" * 60)
if __name__ == '__main__':
    print("Hello World")
