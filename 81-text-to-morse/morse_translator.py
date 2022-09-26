from data_manager import DataManager


class MorseTranslator:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.morse_code = []

    def translate(self, message: str):
        for word in message.split(" "):
            code = ""
            for letter in word:
                code += self.data_manager.morse_library[letter]
                self.morse_code.append(code)
                code = " "
            self.morse_code.append("/")

        morse = "".join(self.morse_code[:-1]).rstrip()
        self.morse_code = []
        return morse
