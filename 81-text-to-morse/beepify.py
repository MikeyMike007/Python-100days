# Dit: 1 unit
# Dah: 3 units
# Intra-character space (the gap between dits and dahs within a character): 1 unit
# Inter-character space (the gap between the characters of a word): 3 units
# Word space (the gap between two words): 7 units


def beepify(morse: str):
    beeps = []

    for code in morse:
        if code == ".":
            beeps += dit()
        elif code == "-":
            beeps += dah()
        elif code == " ":
            beeps += inter_character()
        elif code == "/":
            beeps += word_space()
        else:
            print("ERROR")

    return beeps


def dit():
    return ["SOUND-1-UNIT", "PAUSE-1-UNIT"]


def dah():
    return ["SOUND-3-UNITS", "PAUSE-1-UNIT"]


def inter_character():
    return ["PAUSE-3-UNITS"]


def word_space():
    return ["PAUSE-7-UNITS"]
