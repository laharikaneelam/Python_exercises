while True:
    sInput=input("what is 10+20 ? ").strip()
    if not sInput.isnumeric():
        print("sorry it is not a integer")
        continue
    if sInput == "30":
        print("correct")
        break
    else:
        print("try again")
