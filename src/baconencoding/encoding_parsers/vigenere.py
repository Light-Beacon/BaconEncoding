from ..utils.base import EncodingBase
from .caesar import caesar

UPPER_A_ASCII = ord('A')
LOWER_A_ASCII = ord('a')

def getkeylist(key:str, shift_value:int = 0) -> list[int]:
    return [ord(keychar) - UPPER_A_ASCII + shift_value for keychar in key.upper()]

class Vigenere(EncodingBase):
    name = 'vigenere'
    command_help = 'Parse Vigenere'

    def encode(self,code:str,parser_args,*args,**kwargs) -> str:
        keylist = getkeylist(parser_args.key, shift_value=parser_args.shift)
        result = ''
        for i, chara in enumerate(code):
            result += caesar(code = chara, shift = keylist[i%len(keylist)])
        return result

    def decode(self,code:str,parser_args,*args,**kwargs) -> str:
        keylist = getkeylist(parser_args.key, shift_value=-parser_args.shift)
        result = ''
        for i, chara in enumerate(code):
            result += caesar(code = chara, shift = -keylist[i%len(keylist)])
        return result

    def __init__(self):
        super().__init__()
        self.parser.add_argument('-k','--key',help='The key of the cipher')
        self.parser.add_argument('-s','--shift',help='Shift value', type=int, default=0)

Vigenere()