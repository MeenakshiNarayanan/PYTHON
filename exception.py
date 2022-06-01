a = [1, 2, 3]
try:
    print("second element = ",a[1])
    print("fourth element = ",a[3])
except:
    print("An error occured")
    print()

b= [3, 2, 1]
try:
    a==b
except:
       print("they are not equal")
else:
           print("both equal")
           print()
try:
    k=6/0
    print(k)
except ZeroDivisionError:
        print("Can't divide by zero")
finally:
            print("This is always executed")
       
