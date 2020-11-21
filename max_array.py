from random import random
arr=[]
for i in range(10):
    arr.append(random())
    print(round(arr[i],2),end=' ')
max=0
for i in arr:
    if i>max:
        max=i
print("maximum is",round(max,2))
    
    
