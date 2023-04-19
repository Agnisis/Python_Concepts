l = list(eval(input("enter the list ->")))
l1 = list()
l2 = list()
for i in range(0, len(l)):
    if(l[i] % 2 == 0):
        l1.append(l[i])
    else:
        l2.append(l[i])

l1.sort()
l2.sort()
print("original list", l)
print("even list ", l1)
print("odd list ", l2)
