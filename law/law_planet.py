import math

class LawPlanet:

    def __init__(self,nameplanet,massPlanet,powMassPlanet,radiusPlanet,powMassrad):
        self.mass =  massPlanet
        self.name = nameplanet
        self.radius = radiusPlanet
        self.powMaP = powMassPlanet
        self.powMaRad = powMassrad

    def accelerationG(self):
        
        """ 
         acceleration due to gravity formula = g = G.M1/r2
         Konstanta universal cavendish G =  ( 6,673 x 10⁻¹¹)
         mass planet = M1
         circle radius planet = r2   
        """

        g = 6.67*(10**-11) * self.mass*(10**self.powMaP) / (self.radius*(10**self.powMaRad))**2
        
        return print(self.name, g , " m/s")

    
    def periodeOfRevolu(self):
        pass
    
    
    def info_mass():
        print("""
The planets by mass :

  planet           Mass         Powers      Unit

1. Mercury      3.285 × 10        ^23        Kg
2. Venus        4.867 × 10        ^24        Kg
3. Earth        5.972 × 10        ^24        Kg
4. Mars         6.39  × 10        ^23        Kg
5. Jupiter      1.898 × 10        ^27        Kg
6. Saturn       5.683 × 10        ^26        Kg
7. Uranus       8.681 × 10        ^25        Kg
8. Neptune      1.024 × 10        ^26        Kg
9. pluto        1.309 × 10        ^22        Kg
""")
   
            


