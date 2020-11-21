print("simple calculator")
i,j,sum=0,0,0
while True:
    sInput=input("enter a number or exit")
    if sInput.isnumeric():
        i=i+1
        j=int(sInput)
        sum=sum+j
        if i == 1:
            printsum=sInput
        else:
            printsum=printsum+ "+" + sInput
            print(f"{printsum} = {sum}")
    else:
        if sInput.upper()=="EXIT":
            print("Thank you")
            break
        else:
            print(f"{sInput} is not integer")
