from draconids import Draconids
from cursed import Cursed

def list():
    print("""
    - Beasts
    - Cursed Ones
    - Draconids
    - Elementa
    - Hybrids
    - Insectoids
    - Necrophages
    - Ogroids
    - Relicts
    - Specters
    - Vampires
    """)

def Bestiary():
    print("""
    Welcome to the Bestiary, where all the evil, malicious and
    devious Creatures are listed.
    Which category of monsters would you like to explore?
    """)
    list()

    val = input("> ")
    if val == "Draconids" or val == "draconids":
        Draconids()
    elif val == "Cursed Ones" or val == "cursed ones" or val == "cursed":
        Cursed()

    else:
        print("not ready yet")
Bestiary()
