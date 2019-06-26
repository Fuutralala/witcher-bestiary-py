import cockatrice
def Draconids():
    print("""
    About which Draconid would you like to learn more?
    - Basilisk
    - Cockatrice
    """)
    val = input("> ")
    if val == "Cockatrice" or "cockatrice":
        Cockatrice()
    else:
        print("not ready yet")
Draconids()
