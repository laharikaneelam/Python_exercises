def product(a,b):
    return a*b
def add(a,b):
    return a+b
c=(add if True else product)(2,3)
print(c)
