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
