x=int(input("enter number to reverse"))
y=0
while x!=0:
    digit=x%10
    x//=10
    y*=10
    y+=digit
print(y)
