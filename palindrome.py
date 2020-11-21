def check(st):
    rev=st[::-1]
    print("string:",st)
    print("reverse:",rev)
    if(st==rev):
        print("palin")
    else:
        print("no") 
x=input("enter string")
check(x)

