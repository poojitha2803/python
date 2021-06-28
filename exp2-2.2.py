2.2) Write a program that asks the user for their name and how many times to 
print it. The program should print out the user’s name the specified number of
times

Program:
name=str(input("Enter your name:"))
n=int(input("Enter the value of n:"))
for i in range(n):
    print(name)

Output:
Enter your name:Poojitha
Enter the value of n:5
Poojitha
Poojitha
Poojitha
Poojitha
Poojitha       
