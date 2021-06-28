s=int(input("Enter start number:"))
e=int(input("Enter end number:"))
print("Odd numbers are:")
for i in range (s,e+1):
    if i%2==1:
        print(i,end="\t")
