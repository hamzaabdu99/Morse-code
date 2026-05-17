morse_en = {
    "a": "*-", "b": "-***", "c": "-*-*", "d": "-**", "e": "*", "f": "**-*", "g": "--*", "h": "****", "i": "**",
    "j": "*---", "k": "-*-", "l": "*-**", "m": "--", "n": "-*", "o": "---", "p": "*--*", "q": "--*-",
    "r": "*-*", "s": "***", "t": "-", "u": "**-", "v": "***-", "w": "*--", "x": "-**-", "y": "-*--",
    "z": "--**",
}

symbols = {
    "0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****",
    "7": "--***", "8": "---**", "9": "----*", " ": " ", ".": "*-*-*-", ",": "--**--", "،": "--**--",
    ";": "--**--", "؛": "--**--", ":": "---***", "?": "**--**", "!": "-*-*--", "-": "-****-", "/": "-**-*",
    "(": "-*--*-", ")": "-*--*-", '"': "*-**-*", "'": "*----*", "`": "*----*", "+": "*-*-*", "=": "-***-",
    "_": "**--*-", "$": "***-**-", "@": "*--*-*", "&": "*-***",
}


def english_to_morse(text_message: str) -> str:
    morse_code_lst = []

    txt = text_message.lower()

    for text in txt:
        # if the text user wrote in english morse dictionary come up with the letter code
        if text in morse_en:
            morse_code_lst.append(morse_en[text])

        # if the text user wrote in symbols dictionary come up with that code
        if text in symbols:
            morse_code_lst.append(symbols[text])

    return " ".join(morse_code_lst)


final_output = english_to_morse()  # Write your text here


if final_output != None:
    print("1. \"|\" refers to a space between the words")
    print("2. \" \" refers a space between the letters\n")
    print(
        f"Your Text In Morse Code: \" {final_output.replace('   ', ' | ')} \" ")

else:
    print("Un supported letters found!")
