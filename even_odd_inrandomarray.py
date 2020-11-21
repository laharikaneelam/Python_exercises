from random import *

x=[]
for i in range(10):
    x.append(int(random()*100))
print(x)
even=odd=0

for i in x:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("even",even)
print("odd",odd)
