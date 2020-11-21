m=int(input("enter starting number"))
n=int(input("enter ending number"))
x=m
if x%2!=0:
    x=m+1

while(x<=n):
    print(x)
    x+=2
