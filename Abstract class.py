
from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Traingle(Polygon):
    def noofsides(self):
        print("Triangle: I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("Pentagon: i have 5 sides")
class Hexagon(Polygon):
    def noofsides(self):
        print("Hexagon: i have 6 sides ")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("Quadrilateral : i have 4 sides")

R= Triangle()
R.noofsides()

K= Quadrilateral()
K.noofsides()

R= Pentagon()
R.noofsides()

K= Hexagon()
K.noofsides()

    
        
