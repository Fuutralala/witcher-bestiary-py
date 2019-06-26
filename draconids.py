from basilisk import Basilisk
from forktail import Forktail
from cockatrice import Cockatrice

def Draconids():
    print("""
    About which Draconid would you like to learn more?
    - Basilisk
    - Cockatrice
    - Forktail
    """)
    val = input("> ")
    if val == "Cockatrice" or "cockatrice":
        Cockatrice()
    elif val == "Basilisk" or "basilisk":
        Basilisk()
    elif val == "Forktail" or "forktail":
        Forktail()


    else:
        print("not ready yet")
