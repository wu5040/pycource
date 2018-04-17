import math
sum=0
for k in range(1000):
    sum+=math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4*(396**(4*k)))
PI=1/(sum*2/9801*math.sqrt(2))
print(PI)
print(math.pi)
