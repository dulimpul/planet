from pickletools import int4
import sys
import argparse

from law.law_planet import LawPlanet
from decoration.color import colors
from info.infoPlanet import *


# 
def infoMenu():
    info_distancePlane()
    info_mass()
    infoRadiusPlanet()

def lawMenus(name):

    Xlaw = LawPlanet(
        nameplanet=name,
        massPlanet=float(input(colors.CBLUE2+"Input mass planet"+colors.CEND+"\t:")),
        powMassPlanet=int(input(colors.CBLUE2+"Inpu pow mass planet"+colors.CEND+"\t:")),
        radiusPlanet=float(input(colors.CBLUE2+"Input radius planet"+colors.CEND+"\t:")),
        powMassrad=int(input(colors.CBLUE2+"Input pow radius planet"+colors.CEND+" :"))

    )
    print("\n")
    Xlaw.accelerationG()

def planex():
    print(colors.CBLUE2 + """
PPPPPP   LL          A      NN N     NN EEEEEEE  TTTTTTTTTT
PP    p  LL         AAAA    NN  N    NN EE           TT
PPPPPP   LL        AA  AA   NN   N   NN EEEEEEE      TT
PP       LL       AA AA AA  NN    N  NN EE           TT
PP       LLLLLL  AA      AA NN     N NN EEEEEEE      TT   
    
""" + colors.CEND)
 

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(add_help= True, description=planex())
    parser.add_argument('-planet',action='store', help = "just planetary calculations")
    parser.add_argument('-sun',action='store', help="just sun calculations" )
    parser.add_argument('-satelit',action='store', help="just satelit calculations" )
    parser.add_argument('-info',action='store_true', help="info planet")

    if len(sys.argv) ==1:
        parser.print_help()
        sys.exit(1)

    options = parser.parse_args()
    
    planetOpt =  options.planet
    sunOpt = options.sun
    satelitOpt =  options.satelit
    infoOpt = options.info
    

    if planetOpt:
        lawMenus(planetOpt)
    elif sunOpt:
        print(sunOpt)
    elif infoOpt:
        infoMenu()