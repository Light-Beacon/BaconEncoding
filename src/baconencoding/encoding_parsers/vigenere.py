from ..utils.base import EncodingBase
from .caesar import caesar

UPPER_A_ASCII = ord('A')
LOWER_A_ASCII = ord('a')

def getkeylist(key:str):
    return [ord(keychar) - UPPER_A_ASCII for keychar in key.upper()]

class Vigenere(EncodingBase):
    name = 'vigenere'
    command_help = 'Parse Vigenere'

    def encode(self,code:str,parser_args,*args,**kwargs) -> str:
        keylist = getkeylist(parser_args.key)
        result = ''
        for i in range(len(code)):
            result += caesar(code = code[i], shift = keylist[i%len(keylist)])
        return result

    def decode(self,code:str,parser_args,*args,**kwargs) -> str:
        keylist = getkeylist(parser_args.key)
        result = ''
        for i in range(len(code)):
            result += caesar(code = code[i], shift = -keylist[i%len(keylist)])
        return result

    def __init__(self):
        super().__init__()
        self.parser.add_argument('-k','--key',help='The key of the cipher')

Vigenere()