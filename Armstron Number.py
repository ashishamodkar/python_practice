import math

num = int(input("Enter The Number  "))

sum = 0
times = 0
temp = num
while temp > 0:
    times += 1
    temp//= 10

temp = num
while temp > 0:
    remainder = temp % 10
    sum += pow(remainder, times)
    temp //=10
    
if num == sum: 
    print(num, "is Armstrong Number. ")
else:
    print(num, "is Not a Armstrong Number. ")