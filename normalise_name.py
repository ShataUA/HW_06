import re


def normalize(file_name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}


    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = t  # transliteration small symbols
        TRANS[ord(c.upper())] = t.upper()  # transliteration large symbols


    normalised_name = re.sub(r'\W', '_', file_name.translate(TRANS))  # file name translation and replacing all extra characters in the file name with "_" (excluding letters, numbers and "_")
    return normalised_name
