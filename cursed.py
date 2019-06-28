from archespore import Archespore
from berserker import Berserker
from botchling import Botchling

def Cursed():
    print("""
    About which Cursed One would you like to learn more?

    - Archespore
    - Berserkers
    - Botchlings
    - Lubberkin
    - Ulfhedinn
    - Werewolves
    """)

    val = input("> ")
    if val == "Archespore" or val == "archespore":
        Archespore()
    elif val == "Berserker" or val == "berserker":
        Berserker()
    elif val == "Botchling" or val == "botchling":
        Botchling()

    else:
        print("not ready yet")
