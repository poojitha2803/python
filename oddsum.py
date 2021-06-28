a=range(10)
print(a)
print(type(a))
sum=0
for i in a:
    if i%2==1:
        sum=sum+i
        print("i=",i,"and sum=",sum)
print("Sum of even numbers:")
print ("total=",sum)

Output:
range(0, 10)
<class 'range'>
i= 1 and sum= 1
i= 3 and sum= 4
i= 5 and sum= 9
i= 7 and sum= 16
i= 9 and sum= 25
Sum of even numbers:25   
