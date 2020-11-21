s=input("enter string to test palindrome  ")
len_s=len(s)

for i in range(len_s//2):
    if s[i]!=s[-1-i]:
        print("it is not palindrome")
        quit()
print("palindrome")
    
