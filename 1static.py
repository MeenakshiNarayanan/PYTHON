class Python:
    #access through class
    
 staticVariable = 9
print(Python.staticVariable)

    #change within the class
Python.staticVariable = 12
print(Python.staticVariable)

    #access through instance
instance = Python()
print(instance.staticVariable)
 #change within an instance
instance.staticVariable = 15
print(instance.staticVariable)
print(Python.staticVariable)
    
    
    
    
    
