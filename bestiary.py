import draconids
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
Bestiary()
val = input("> ")
if val == "Draconids":
    Draconids()
else:
    print("not ready yet")
