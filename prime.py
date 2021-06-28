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
