a=int(input("enter the no ->"))
rev=0
digit=0
while(a!=0):
    digit=a%10
    rev=(rev*10)+digit
    a=a//10

print("reverse is ",rev)