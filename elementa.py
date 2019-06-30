from djinn import Djinn
from earthelemental import EarthElemental
from firelemental import FireElemental
from golem import Golem
from gargoyle import Gargoyle

def Elementa():
    print("""
    About which Elementa would you like to learn more?

    - Djinn
    - Earth Elemental
    - Fire Elemental
    - Gargoyle
    - Golem
    - Hound of the Wild Hunt
    - Ice Elemental
    - Pixies
    - Apiarian Phantom
    - Therazane

    """)

    val = input("> ")
    if val == "Djinn" or val == "djinn":
        Djinn()
    elif val == "EarthElemental" or val == "earthelemental" or val == "Earth Elemental" or val == "earth elemental":
        EarthElemental()
    elif val == "FireElemental" or val == "fireelemental" or val == "Fire Elemental" or val == "fire elemental":
        FireElemental()
    elif val == "Golem" or val == "golem":
        Golem()
    elif val == "Gargoyle" or val == "gargoyle":
        Gargoyle()
