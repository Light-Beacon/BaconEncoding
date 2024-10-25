from ..utils.base import EncodingBase

class Ascii(EncodingBase):
    name = 'ascii'
    command_help = 'Parse Ascii'

    def encode(self,code:str,parser_args,*args,**kwargs) -> str:
        return ' '.join([str(ord(char)) for char in code])

    def decode(self,code:str,parser_args,*args,**kwargs) -> str:
        return ''.join([chr(int(num)) for num in code.split()])

Ascii()