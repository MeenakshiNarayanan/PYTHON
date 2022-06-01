class A:
    def __init__(self):
        self.name="Kashish"
    def print_A(self):
        print(self.name)
            
obj = A()
obj.print_A()

class B(A):
    def __init_(self):
        self.name = "KG"
    def print_B(self):
        print (self.name)
obj1 = B()
obj1.print_B()
class C:
    name = None
    _roll = None
    __branch = None
    def _init_(self, name, roll, branch):
        self.name = name
        self._roll= roll
        self. branch = branch
    def dsiplayName(self):
        print("Name: ", self.name)
    def _displayRoll(self):
        print("Roll: ", self._roll)
    def _displayBranch( se1f):
        print("Branch: ", self._branch)
    def access_displayBranch (self):
        self._displayBranch()
class D(C):
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)
    def access_displayRoll(self):
         self._displayRoll()
obj = D("Kashish", 5, "CSE") 
obj.displayName()
obj.access_displayRoll()
obj.access__displayBranch()








