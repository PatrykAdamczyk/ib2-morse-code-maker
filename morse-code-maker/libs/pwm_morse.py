class Morse(object):
    encrypted = ""
    decrypted = ""
    d2e_morse_dictionary = {
        # 0 = . | 1 = -
        # Litery Alfabetu Łacińskiego
        "A":"013",
        "B":"10003",
        "C":"10103",
        "D":"1003",
        "E":"03",
        "F":"00103",
        "G":"1103",
        "H":"00003",
        "I":"003",
        "J":"01113",
        "K":"1013",
        "L":"01003",
        "M":"113",
        "N":"103",
        "O":"1113",
        "P":"01103",
        "Q":"11013",
        "R":"0103",
        "S":"0003",
        "T":"13",
        "U":"0013",
        "V":"00013",
        "W":"0113",
        "X":"10013",
        "Y":"10113",
        "Z":"11003",
        # Cyfry
        "1":"011113",
        "2":"001113",
        "3":"000113",
        "4":"000013",
        "5":"000003",
        "6":"100003",
        "7":"110003",
        "8":"111003",
        "9":"111103",
        "0":"111113",
        # Inne Litery
        "Ą":"01013",
        "Ć":"101003",
        "Ę":"001003",
        "Ł":"010013",
        "Ń":"110113",
        "Ó":"11103",
        "Ś":"00010003",
        "Ż":"1100103",
        "Ź":"110013",
        # Znaki
        ".":"0101013",
        ",":"1100113",
        "'":"0111103",
        "\"":"0100103",
        "_":"0011013",
        ":":"1110003",
        ";":"1010103",
        "?":"0011003",
        "!":"1010113",
        "-":"1000013",
        "+":"010103",
        "/":"100103",
        "(":"101103",
        ")":"1011013",
        "=":"100013",
        "@":"0110103",
        # Specjalny Znak
        " ":"2",
        "/ ":"3"
    }
    e2d_morse_dictionary = {v: k for k, v in d2e_morse_dictionary.items()}
    def __init__(self, code="", string=False, *args, **kwargs):
        if string is False:
            self.encrypted = code
            self.__decrypt()
        else:
            self.decrypted = code
            self.__encrypt()
    def __encrypt(self):
        self.encrypted = Morse.Encrypt(self.decrypted)
    def __decrypt(self):
        self.decrypted = Morse.Decrypt(self.encrypted)
    def __md(i):
        ret = []
        for e in Morse.d2e_morse_dictionary.values():
            if len(e) is i:
                ret.append(e)
        return ret
    def Encrypt(string_code):
        characters = Morse.d2e_morse_dictionary.keys()
        ret = ""
        for x in string_code.upper():
            if x in characters:
                ret += Morse.d2e_morse_dictionary[x]
            else:
                print("Alfabet Morse'a nie obsługuje:",x," | Pomijanie...")
        character = [".","-"," ","/"]
        rete = ""
        for r in ret:
            rete += character[int(r)]
        return rete
    def Decrypt(code):
        _md = Morse.d2e_morse_dictionary
        morse_characters = [
            [], #0
            [x for x in Morse.__md(1)], #1
            [x for x in Morse.__md(2)], #2
            [x for x in Morse.__md(3)], #3
            [x for x in Morse.__md(4)], #4
            [x for x in Morse.__md(5)], #5
            [x for x in Morse.__md(6)], #6
            [x for x in Morse.__md(7)], #7
            [x for x in Morse.__md(8)], #8
        ]
        ret = ""
        skip = 0
        code2 = code
        code = ""
        characters = {
            ".":"0",
            "-":"1",
            " ":"2",
            "/":"3"
        }
        for r in code2:
            code += characters[r]
        for x in list(range(len(code))):
            if skip > 0:
                skip = skip - 1
                continue
            if code[x] in morse_characters[1]:
                ret += Morse.e2d_morse_dictionary[code[x]]
            elif code[x:(x+2)] in morse_characters[2]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+2)]]
                skip = 1
            elif code[x:(x+3)] in morse_characters[3]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+3)]]
                skip = 2
            elif code[x:(x+4)] in morse_characters[4]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+4)]]
                skip = 3
            elif code[x:(x+5)] in morse_characters[5]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+5)]]
                skip = 4
            elif code[x:(x+6)] in morse_characters[6]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+6)]]
                skip = 5
            elif code[x:(x+7)] in morse_characters[7]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+7)]]
                skip = 6
            elif code[x:(x+8)] in morse_characters[8]:
                ret += Morse.e2d_morse_dictionary[code[x:(x+8)]]
                skip = 7
            elif code[x] == "2":
                ret += " "
            else:
                raise Exception("Error M#1: Decryption Error")
        return ret
    