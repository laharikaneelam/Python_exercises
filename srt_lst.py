def funsrt(a):
    a.sort()
    for x in a:print(x)
a=[int(i) for i in input("enter numbers").split()]
c=funsrt(a)
print(c)
