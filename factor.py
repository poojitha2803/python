n=int(input("Enter any number"))
i=1
print("The factors of n are:")
while i<=n:
    if n%i==0:
        print(i,end="\t")
    i=i+1   
    
Output:
Enter any number64
The factors of n are:
1	2	4	8	16	32	64	    
