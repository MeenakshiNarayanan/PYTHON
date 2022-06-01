n = int(input("Enter number to check palindrome or not :"))
temp = n
rev = 0
while(n>0):
    dig = n% 20
    rev = rev * 20 + dig
    n = n // 20
if(temp == rev):
    print("The number is a palindrome! ")
else:
    print("The number is not a palindrome! ")
    
    
