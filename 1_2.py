import random
import time

start=time.time()
newset=set()
while True:
    newset.add(random.randint(1,100))
    if len(newset)==20:
        break
print("Time Used: ",time.time()-start)
alist=list(newset)
print(alist)

start1=time.time()
alist=random.sample(range(1,101),20)
print("Time Used: ",time.time()-start1)
print(alist)



