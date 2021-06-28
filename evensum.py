a=range(10)
print(a)
print(type(a))
sum=0
for i in a:
    if i%2==0:
        sum=sum+i
        print("i=",i,"and sum=",sum)
print("Sum of even numbers:")
print ("total=",sum)

Output:
range(0, 10)
<class 'range'>
i= 0 and sum= 0
i= 2 and sum= 2
i= 4 and sum= 6
i= 6 and sum= 12
i= 8 and sum= 20
Sum of even numbers:20
