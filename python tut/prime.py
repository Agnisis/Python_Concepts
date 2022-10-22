a=int(input("enter the no "))

flag=0

#for(int i=2;i<a;i++)

for i in range (2,a):
    if(a%i==0):
     flag=1
     break
if(flag==0):
    print(a," is prime")
else :
    print(a, " is not prime")