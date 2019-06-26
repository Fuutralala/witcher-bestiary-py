import cockatrice
def Draconids():
    print("""
    About which Draconid would you like to learn more?
    - Basilisk
    - Cockatrice
    """)
    name = input("> ")
    if name == "Cockatrice":
        Cockatrice()
    else:
        print("not ready yet")
