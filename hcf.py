a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if b > a:
    mn = b
else:
    mn = a

for i in range(1, mn+1):
    if a%i==0 and b%i == 0:
        hcf = i
print("The HCF of these two numbers is:",hcf)

    