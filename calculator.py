print("Zero operator terminates the program")
while True:
    o=input("enter the operator(+,-,*,/)")
    if o=='0':
        break
    if o in ("+","-","*",'/'):
        x=float(input("enter x:"))
        y=float(input("enter y:"))
        if o=="+":
            print("%.2f" %(x+y))
        elif o=="-":
            print("%.2f" %(x-y))
        elif o=="*":
            print("%.2f"%(x*y))
        elif o=="/":
            if y!=0:
                print("%.2f"%(x/y))
            else:
                print("invalid as divided by zero")
        else:
            print("invalid oprator")
        
                      
