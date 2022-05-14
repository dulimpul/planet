from law import LawPlanet, law_planet
from info import info_mass,info_distancePlane,infoRadiusPlanet


# maypalanet = LawPlanet("bumi",5.972)

# maypalanet.accelerationG()

# object class in law_planet
bumi = LawPlanet("erth",6,24,6.4,6)
venus =  LawPlanet("Venus",4.867,24,6.05,6)


# acceleration function
bumi.accelerationG()
venus.accelerationG()
# revolusi function 
bumi.RevoluPlan(39.5)

# info mass planet
info_mass()

# info distance from planet to earth
info_distancePlane()

# info radius planets
infoRadiusPlanet()