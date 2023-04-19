a=int(input("enter the no ->"))
i=1
sum=0
t=a
while(i < a):
    if(a % i == 0):
       sum=sum+i
    i = i+1

if(sum==a):
    print(a," is proper")
else :
    print(a," is not proper")