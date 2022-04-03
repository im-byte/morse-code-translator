import re

morsecode_list = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}

running = True
while running:
    task = input("1. Morse Code -> Text\n2. Text -> Morse Code\n")

    if task.isdigit():
        if int(task) == 1:  # Morse Code -> Text
            morsecode_input = input("Input: ")
            morsecode_split = morsecode_input.split(" ")
            text_output = ""

            for morsecode in morsecode_split:
                for key in morsecode_list:
                    code = morsecode_list[key]
                    if morsecode == code:
                        text_output += key
            print("Output: " + text_output)
        elif int(task) == 2:  # Text -> Morse Code
            text_input = input("Input: ")
            text_split = list(text_input.upper())
            morsecode_output = ""

            for character in text_split:
                if character in morsecode_list:
                    morsecode_output += morsecode_list[character] + " "

            print("Output: " + morsecode_output)
    print("\n")
