from djinn import Djinn
from earthelemental import EarthElemental

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
