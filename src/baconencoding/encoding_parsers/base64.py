import base64
from ..utils.base import EncodingBase

class Base64Encode(EncodingBase):
    name = 'base64'
    command_help = 'base64'

    def encode(self,code:str,_parser_args,*_args,**_kwargs) -> str:
        encoder = base64.b64encode(code.encode('utf-8'))
        if _parser_args.get('hex'):
            return encoder.hex()
        return encoder.decode('utf-8')

    def decode(self,code:str,_parser_args,*_args,**_kwargs) -> str:
        decoder = base64.b64decode(code)
        return decoder.decode()

Base64Encode()