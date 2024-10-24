from pprint import pprint

r = int(input("Enter the number of rows :"))
c = int(input("Enter the number of cols :"))

mat = []
for i in range(r):
    temp = []
    for j in range(c):
        if i == j:
            temp.append(1)
        else:
            temp.append(0)
    mat.append(temp)

pprint(mat)

