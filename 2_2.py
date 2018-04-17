from math import sqrt
x=list()
flag=1
for i in range(2,100):
    for j in range(2,int(sqrt(i))+1):
        if i%j!=0:
            flag=1
        else:
            flag=0
            break;
    if flag==1:
        x.append(i)
print(x)

y=[p for p in range(2,100) if 0 not in[ p%d for d in range(2,int(sqrt(p))+1)]]
print(y)
