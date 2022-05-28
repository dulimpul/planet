import math
import pathlib
import sys

# path folder
tetst =  pathlib.Path.cwd()
sys.path.insert(0,tetst)

from decoration.color import colors

class LawPlanet:

    def __init__(self,nameplanet,massPlanet,powMassPlanet,radiusPlanet,powMassrad):
        self.mass =  massPlanet
        self.name = nameplanet
        self.radius = radiusPlanet
        self.powMaP = powMassPlanet
        self.powMaRad = powMassrad

    # acceleration gravity
    def accelerationG(self):
        
        """ 
         acceleration due to gravity formula = g = G.M1/r2
         Konstanta universal cavendish G =  ( 6,673 x 10⁻¹¹)
         mass planet = M1
         circle radius planet = r2 
         example :
         g = ( 6,673 x 10⁻¹¹) * 5.972 × 10^24 / 6.37 x 10^6

        """

        g = 6.67*(10**-11) * self.mass*(10**self.powMaP) / (self.radius*(10**self.powMaRad))**2
        
        return print(f"{self.name} {colors.CRED}{g}{colors.CEND} m/s")

    # calculate the Revolution of the planet
    def RevoluPlan(self,AuDistanceSun):
        """
        use kepler's law 
        if the distance is only in the solar systemif the distance is only in the solar system
        law III
        T1^2/r1^3 = T2^2/r2^3 or (T1/T2)^2 = (r1/r2)^3

        refers to the earth
        T1 =  365 day
        r1 = 1 As/Au (Astronimical Unit)
        r2 = the distance from the planet you want to know the revolution = var AuDistanceSun

        """
        
        Ttow = math.sqrt((1/AuDistanceSun)**3)
        
        return print(f"the revolution is {colors.CRED}{(365/Ttow)/365}{colors.CEND} yer conversion day is {colors.CRED}{365/Ttow}{colors.CRED} ")

    # 
    
    








            


