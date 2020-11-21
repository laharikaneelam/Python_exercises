def returner(data1,data2):
    return {data1,data2}
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
z=returner(tuple(list1),tuple(list2))
print(z,type(z))
