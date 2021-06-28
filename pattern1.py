n=int(input("Enter n value:"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print (j,end=" ")
    print ( )
for i in range (n,1,-1):
    for j in range (1,i):
        print (j,end=" ")
    print ( )   
    
Output:
Enter n value:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
