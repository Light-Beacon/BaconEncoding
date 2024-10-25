from ..utils.base import EncodingBase

UPPER_A_ASCII = ord('A')

class Alphabet(EncodingBase):
    name = 'a1z26'
    command_help = 'A to 1 ... Z to 26'

    def encode(self,code:str,_parser_args,*_args,**_kwargs) -> str:
        code = code.upper()
        return ' '.join([str(ord(char) - UPPER_A_ASCII + 1) for char in code])

    def decode(self,code:str,_parser_args,*_args,**_kwargs) -> str:
        return ''.join([chr(int(num) + UPPER_A_ASCII - 1) for num in code.split()])

Alphabet()