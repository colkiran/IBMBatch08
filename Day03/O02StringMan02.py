
print("find".center(60, "-"))
st = "hello world"
print(f"st :{st}")

indx = st.find("w")
print(f"Index of w :{indx}")

indx = st.find("l")
print(f"Index of 1st l :{indx}")

# hard coded
# indx = st.find("l", 5)
# print(f"Index of 3rd l :{indx}")

indx = st.find("l", st.find("l") + 1)
print(f"Index of 2nd l :{indx}")

indx = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"Index of 3rd l :{indx}")

print("replace".center(60, "-"))
st = "hello world"
print(f"st :{st}")

res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print(st[:6] + st[6:].replace("l", "L"))

print("-" * 60)
# isalpha
# isnumeric

st = "123468678754564python1234"

print(st[0].isnumeric())
print(st[4].isalpha())

for i in range(0, len(st)):
    if st[i].isalpha():
        print(i)
        break
