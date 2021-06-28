n=int(input("Enter any number:"))#asking for the number
rev=0#initiating rev = 0
while (n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print ("Reverse of the number is:",rev)#printing the reverse of number

Output:
Enter any number:56789
Reverse of the number is: 98765  

Enter any number:82369
Reverse of the number is: 96328      
