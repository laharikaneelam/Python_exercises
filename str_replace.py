x="laha, sarva, rebbe, rishi, vaish"

x1=input("enter value to replace")
x2=input("enter value to be replaced with")
l=len(x1)
if x.find(x1) >0:
    k=x.find(x1)
    s=x[:k]+x2[:]+x[len(x1)+k:]
    print(s)
