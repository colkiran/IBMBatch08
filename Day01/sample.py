#! c:\python311

print("Hello World")
# this is a comment
print("Hello World")        # this is a comment


# print("Hello World")
# print("Hello World")
# print("Hello World")

"""
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 60)

def fun():
    # function code
    for i in range(1, 31):
        # for loop code
        if i % 3 == 0:
            # if condition code
            print(i)
        # for loop code
        print("hello", i)
    # function code
    print("---WORLD---")

# main module code
fun()