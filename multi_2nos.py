i,j=0,0
while True:
    s=input("enter no")
    if not s.isnumeric():
        print("enter any valid numeric")
    else:
        i=int(s)
        if i < 2 or i >100:
            print("enter  no btw 2 and 100")
        else:
            break
while True:
    k=input("enter no")
    if not k.isnumeric():
       print("enter any valid integer")
    else:
        j=int(k)
        if j < 2 or j >100:
            print("enter  no btw 2 and 100")
        else:
            break
print(f"{i} * {j} = {i*j}")    
