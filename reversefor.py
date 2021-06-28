n=int(input("Enter any number:"))
d=int(input("Enter the number of digits:"))
rev=0
for i in range(0,d):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of the number:",rev)    
    

