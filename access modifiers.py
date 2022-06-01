class Super:
    var1 = None
    _var2 = None
    __var3 = None
    def __init__(self, var1, var2,var3):
        
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    def displayPublicMembers(self):
        print("public Data Member: ", self.var1)
    def _displayProtectedMembers(self):
        print("Protected Data Member: " , self._var2)
    def _displayPrivateMembers(self):
        print("private Data Members: ", self.__var3)
    def accessPrivateMembers(self):    
        self.__displayPrivateMembers()

class sub(super):
    def __init__(self, var1, var2, var3):
            super.__init__(self, var1, var2, var3)
    def accessProctectedMembers(self):
            self._displayProctectedMembers()
obj = sub("KG", 5, "KG !")
obj.displayPublicMembers()
obj.accessProtectMembers()
obj.accessPrivateMembers()
print("object is accessing protected member: ", obj._var2)
            
