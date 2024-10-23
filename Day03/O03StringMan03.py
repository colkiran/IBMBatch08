
print("maketrans".center(60, "-"))
# chage the data byte by byte
st = "hello world"
print(f"st :{st}")

# length of a and b should be the same
a = "helowrd"
b = "HELOWRD"

resTbl = st.maketrans(a, b)
print(resTbl)

print("Translate".center(60, "-"))

res = st.translate(resTbl)
print(res)

print("-" * 60)
st = ("****hello****")
print(f"st :{st}")

print(st.lstrip("*"))

print(st.rstrip("*"))

print(st.strip("*"))
