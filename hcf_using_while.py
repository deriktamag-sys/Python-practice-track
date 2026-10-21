a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

mn = min(a,b)

while(True):
    if a%mn ==0 and b%mn==0:
        hcf = mn
        break
    mn-= 1
print("The required HCF is :",hcf)