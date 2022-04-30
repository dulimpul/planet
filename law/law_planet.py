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
        
        print(self.name, g , " m/s")

   
            
bumi = LawPlanet("erth",6,24,6.4,6)

bumi.accelerationG()

