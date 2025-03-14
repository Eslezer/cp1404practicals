"""
CP1404/CP5632 Practical
Hexadecimal Colour Code Lookup

"""

COLOUR_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "BLACK": "#000000",
    "BLUEVIOLET": "#8a2be2",
    "CORAL": "#ff7f50",
    "CRIMSON": "#dc143c",
    "DARKCYAN": "#008b8b",
    "DARKGOLDENROD": "#b8860b",
    "DARKORANGE": "#ff8c00"
}

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    try:
        print(f"The hexadecimal code for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()
