from basilisk import Basilisk
from forktail import Forktail
from cockatrice import Cockatrice
from royalwyvern import Royalwyvern
from shrieker import Shrieker
from silverbasilisk import Silverbasilisk
from slyzards import Slyzard

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
    elif val == "Shrieker" or val == "shrieker":
        Shrieker()
    elif val == "Silverbasilisk" or val == "silverbasilisk" or val == "silver basilisk" or val == "Silver Basilisk":
        Silverbasilisk()
    elif val == "Slyzard" or val == "slyzard" or val == "dracolizard" or val == "Dracolizard":
        Slyzard()

    else:
        print("not ready yet")
