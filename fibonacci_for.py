
k=int(input("enter np"))

k1=1
k2=1
print(k1,k2,end=" ")
for i in range(k-2):
    print(k1+k2,end=" ")
    k1,k2=k2,k1+k2
    
    
