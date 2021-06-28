amount=int(input("Enter the total bill"))
if amount>=1000 and amount<=2000:
    dis=amount*.1
    print("Discount is ",dis)
    print("Bill amount is ",amount-dis) 
elif amount>=2000 and amount<=3000:
    dis=amount*.2
    print("Discount is ",dis)
    print("Bill amount is ",amount-dis)     
elif amount>=3000 and amount<=5000:
    dis=amount*.3
    print("Discount is ",dis)
    print("Bill amount is ",amount-dis)    
elif amount>=5000:
    dis=amount*.4
    print("Discount is ",dis)
    print("Bill amount is ",amount-dis) 
else:
    print("No discount")
    print("Bill amount is ",amount) 
