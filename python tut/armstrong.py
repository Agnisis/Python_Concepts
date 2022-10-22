a=int(input("enter the number"))
t=a
sum=0
digit=0

while(a!=0):
    digit=a%10
    sum=sum+(digit**3)
    a=a//10

if(t==sum):
    print("its armstrong")
else:
    print("not armstronbg")


 

