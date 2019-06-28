from archespore import Archespore
from berserker import Berserker
from botchling import Botchling
from lubberkin import Lubberkin
from ulfhedinn import Ulfhedinn
from werewolf import Werewolf

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
    elif val == "Lubberkin" or val == "lubberkin":
        Lubberkin()
    elif val == "Ulfhedinn" or val == "ulfhedinn":
        Ulfhedinn()
    elif val == "Werewolf" or val == "werewolf":
        Werewolf()

    else:
        print("not ready yet")
