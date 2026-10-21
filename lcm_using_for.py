a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

if b>a:
    mx = b
else:
    mx = a

for i in range(1, mx+1):
    if a%i ==0 and b%i ==0:
        hcf = i
lcm = (a*b)//hcf
print(f"The lcm of {a} and {b} is : {lcm}")