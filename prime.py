n=int(input("Enter any number:"))
i=1
flag=0
while i<=n:
    if n%i==0:
        flag+=1
    i+=1
if flag==2:
    print("N is prime")
else:
    print("N is not a prime number")

Output:

Enter any number:67
N is prime

Enter any number:1280
N is not a prime number    
