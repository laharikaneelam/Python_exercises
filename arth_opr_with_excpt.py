def getOperator():
    while True:
        rtnStrOperator=input("which operator to use?(Type exit to end)[Type +,-,x,'/']").strip()
        if rtnStrOperator.upper() not in ('+','-','X','/','EXIT'):
            print("not a valid operator")
            continue
        else:
            return rtnStrOperator
    
def isValidNumber(aStrInput):
    try:
        fNum=float(aStrInput)
        return True
    except TypeError:
        return False

def getResult(aStrNum1,aStrNum2,aStrOperator):
    rtnfResult=0.0
    if aStrOperator=='+':
        rtnfResult=float(aStrNum1)+float(aStrNum2)
    elif aStrOperator == 'x':
        rtnfResult=float(aStrNum1)* float(aStrNum2)
    elif aStrOperator=='-':
        rtnfResult=float(aStrNum1)- float(aStrNum2)
    elif aStrOperator=='/':
        try:
            rtnfResult=float(aStrNum1)/float(aStrNum2)
        except ZeroDivisionError:
            raise ZeroDivisionError
    return rtnfResult

print("welcome to solving basic math problems using python")

while True:
    strOperator=getOperator()
    if strOperator.upper()=="EXIT":
        print("**********thank you*********")
        break
    strNum=[0,0]
    for i in range(2):
        while True:
            strNum[i]=input("enter number"+ str(i+1)+": ").strip()
            if not isValidNumber(strNum[i]):
                print(strNum[i]," is not valid number")
                continue
            else:
                break
    strPrintText=strNum[0]+'  '+strOperator+'  '+' '+strNum[1]
    try:
        fResult=getResult(strNum[0], strNum[1], strOperator)
        print(strPrintText+" = ",fResult)
    except ZeroDivisonError:
        print("Oops, cannot divide by zero!!")
            


    












        
