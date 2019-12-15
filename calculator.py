print("!!!Pyhton Claculater Program!!!")
a=int(input("Enter The Number"))
b=int(input("Enter The Number"))
print("Choose an operater \n1 addition(+)\n2 subtraction(-)\n3 multiplication(*)\n4  Division(/)")
operator = input("Choice your operator:")

if operator=='+':
    print("Answer is  : ",a+b)
elif operator=='-':
    print("Answer is  : ",a-b)
elif operator=='*':
    print("Answer is  : ",a*b)
elif operator=='/':
    print("Answer is   :",a/b)
else :
    print("Invalid inpur !")