import struct

def floatToBits(f):
    s = struct.pack('>f', f)
    return struct.unpack('>l', s)[0]

def bitsToFloat(b):
    s = struct.pack('>l', b)
    return struct.unpack('>f', s)[0]

def printHelp():
    print("Commands:")
    print("'exit', 'e', 'quit', 'q': Quit this program")
    print("'switch', 's': Switch conversion mode")
    print("'help', 'h': Reprint this help section")
    print()

if __name__ == "__main__":
    print("Welcome to the pdxvar conversion tool")
    print("Store mode takes a floating point variable and outputs its corresponding value to store it in a pdxvar")
    print("Extract mode takes a pdxvar's stored value and outputs its actual value if parsed as a float")
    print()
    printHelp()
    toFloat = True
    while True:
        if toFloat:
            inputString = input("Store float in a pdxvar: ")
        else:
            inputString = input("Extract the value of a pdxvar: ")
        if inputString.lower() == "exit" or inputString.lower() == "e" or inputString.lower() == "quit" or inputString.lower() == "q":
            break

        if inputString.lower() == "switch" or inputString.lower() == "s":
            toFloat = not toFloat
            continue
        if inputString.lower() == "help" or inputString.lower() == "h":
            printHelp()
            continue
        try:
            inputFloat = float(inputString)

            if toFloat:
                output = floatToBits(inputFloat) / 1000.0
                print(f"{output:.3f}")
            else:
                output = bitsToFloat(round(inputFloat * 1000))
                print(output)
        except:
            print("Could not parse input")

