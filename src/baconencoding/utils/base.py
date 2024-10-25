from abc import abstractmethod
from baconencoding.utils.command import regist_encoding, add_parser

class EncodingBase():
    name:str
    command_help:str

    @abstractmethod
    def encode(self,code:str,parser_args,*args,**kwargs) -> str:
        """Encode to target Format"""
    
    @abstractmethod
    def decode(self,code:str,parser_args,*args,**kwargs) -> str:
        """Decode from target Format"""
    
    def prase(self,args):
        if args.action == 'encode':
            return self.encode(args.code,args)
        elif args.action == 'decode':
            return self.decode(args.code,args)
    
    def __init__(self):
        regist_encoding(self.name,self.prase)
        self.parser = add_parser(self.name, help=self.command_help)
        self.parser.add_argument('action',
                                choices=['encode','decode'],
                                help="Encode or decode the string")
        self.parser.add_argument('code', type=str,
                                help = "The string to be encode or decode")