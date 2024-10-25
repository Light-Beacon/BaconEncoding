from ..utils.base import EncodingBase

class Unicode(EncodingBase):
    name = 'unicode'
    command_help = 'Parse Unicode'

    def encode(self,code:str,parser_args,*args,**kwargs) -> str:
        return code.encode('unicode_escape').decode()

    def decode(self,code:str,parser_args,*args,**kwargs) -> str:
        return code.decode('utf-8').encode('utf-8')

Unicode()