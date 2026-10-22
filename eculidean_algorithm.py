a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

while b!=0:
    remainder = a%b
    a = b
    b = remainder 

print("Here, the GCD suing the eucildean algorithm is:",a)