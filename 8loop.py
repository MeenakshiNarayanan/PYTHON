a = int(input( 'Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = a
while temp >0:
     r = temp % 10
     sum += r ** 3
     temp //= 10
if a == sum:
    print(a, " is an armstrong number")
else :
    print(a, " is not an armstrong number")
    
