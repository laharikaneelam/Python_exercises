a=5
b=12
def fun():
    a=6
    print(a)
    x=globals()['b']
    print(x)
fun()
