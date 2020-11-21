k=20
for i in range(0,10):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0,i):
        print("*",end=" ")
    print('\r')
