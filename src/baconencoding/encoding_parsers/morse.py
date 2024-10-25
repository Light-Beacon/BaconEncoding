from ..utils.base import EncodingBase

CHAR_MORSE_MAPPING = {
    'A': '.-',  'B': '-..', 'C': '-.-.',
    'D': '-..', 'E': '.',   'F': '..-.',
    'G': '--.', 'H': '....','I': '..',
    'J': '.---','K': '-.-', 'L': '.-..',
    'M': '--',  'N': '-.',  'O': '---',
    'P': '.--.','Q': '--.-','R': '.-.',
    'S': '...', 'T': '-',   'U': '..-',
    'V': '...-','W': '.--', 'X': '-..-',
    'Y': '-.--','Z': '--.',
    '1': '.----',   '2': '..---',
    '3': '...--',   '4': '....-',
    '5': '.....',   '6': '-....',
    '7': '--...',   '8': '---..',
    '9': '----.',   '0': '-----',
    '?': '..--..',  '/': '-..-.',
    '(': '-.--.-',  '-': '-....-',
    '.': '.-.-.-',
}

MORSE_CHAR_MAPPING = {}
for v,k in CHAR_MORSE_MAPPING.items():
    MORSE_CHAR_MAPPING[k] = v

class Morse(EncodingBase):
    name = 'morse'
    command_help = 'Parse Morse'

    def encode(self,code:str,_parser_args,*args,**kwargs) -> str:
        return ' '.join([CHAR_MORSE_MAPPING.get(char,'!NOTDEF!')for char in code.upper()])

    def decode(self,code:str,_parser_args,*args,**kwargs) -> str:
        return ''.join([' ' if chiper == '\\'
                        else MORSE_CHAR_MAPPING.get(chiper,'!NOTDEF!')
                        for chiper in code.split()])

Morse()