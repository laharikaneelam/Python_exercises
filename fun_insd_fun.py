def a(b):
    def c():
        res=b()
        return res+2
    return c
def b():
    return 98
d=a(b)
print("result",d())
