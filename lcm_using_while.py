a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

maxNum = max(a, b)

while(True):
    if maxNum% a ==0 and maxNum%b ==0:
        break
    maxNum+= 1
print(f"The lcm of {a} and {b} is : {maxNum}")