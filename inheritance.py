class A():
    def display(dp):
        print("Display Inside class A ")
    def show(self):
        print("Show Inside class A")
class B (A):
    def show(pt):
        print("Print Inside class B")
    def show(self):
        print("Show Inside class B")
class C (B):
    def show(self):
        print("Show Inside class B")
s = A()
s.display()
k= B()
k.show()
g = C()
g.show()
