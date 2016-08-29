a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
if((a>b) and (a>c)):
    print("a is maximum")
elif((b>a) and (b>c)):
    print("b is maximum")
elif((c>a) and (c>b)):
    print("c is maximum")
elif((a==b) or (b==c) or (c==a)):
    print("two numbers are equal")
else:
    print("all are equal")
input("press enter to close:")
