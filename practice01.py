# """ conditonal in one line"""
# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# print("Yes") if a >=b else print("No")



# name = input("Enter the name:")
# print(len(name))
# print(name.count("e"))
# print(name.endswith("ik"))

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))
if (a>=b and a>=c):
    print("a is greatest")
elif (b>=c and b>=a):
    print("b is greatest")
else:
    print("c is greatest")

