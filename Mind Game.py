a=1
while(a<=6):
    a=int(input("Enter the Number"))
    if a==20:
        print("you Win")
        break
    elif a<20:
        print("no is Smaller ")
    elif a>20:
        print("no is greater")
    else:
        print("you loose")
        continue
    a= a + 1
