from basilisk import Basilisk
from forktail import Forktail
from cockatrice import Cockatrice
from royalwyvern import Royalwyvern
from shrieker import Shrieker

def Draconids():
    print("""
    About which Draconid would you like to learn more?
    - Basilisk
    - Cockatrice
    - Forktail
    - Royal Wyvern
    """)
    val = input("> ")
    if val == "Basilisk" or val == "basilisk":
        Basilisk()
    elif val == "Cockatrice" or val == "cockatrice":
        Cockatrice()
    elif val == "Forktail" or val == "forktail":
        Forktail()
    elif val == "Royal Wyvern" or val == "royal wyvern" or val == "Royalwyvern" or val == "royalwyvern":
        Royalwyvern()

    else:
        print("not ready yet")
