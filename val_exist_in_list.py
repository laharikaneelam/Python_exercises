lst=[12,"laha",13,"krishna",78,9,65]
a=int(input("enter element"))
for i in lst:
    if a==i:
        print("exists")
        break
else:
    print("not exists")
    
