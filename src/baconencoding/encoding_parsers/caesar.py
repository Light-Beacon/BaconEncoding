from ..utils.base import EncodingBase
from ..utils.checks import char_is_between

UPPER_A_ASCII = ord('A')
LOWER_A_ASCII = ord('a')
ZERO_ASCII = ord('0')

def shifting(char,base,shift,loop_length = 26):
    shift %= loop_length
    return chr((ord(char) - base + shift + loop_length)%loop_length + base)

def caesar(code,shift,shfiting_numbers = False):
    string = ''
    for char in code:
        if char_is_between(char,'a','z'):
            string += shifting(char=char,base=LOWER_A_ASCII,shift=shift)
        elif char_is_between(char,'A','Z'):
            string += shifting(char=char,base=UPPER_A_ASCII,shift=shift)
        elif shfiting_numbers and char_is_between(char,'0','9'):
            string += shifting(char=char,base=ZERO_ASCII,shift=shift,loop_length=10)
        else:
            string += char
    return string

class Caesar(EncodingBase):
    name = 'caesar'
    command_help = 'Caesar, character shifting'

    def encode(self,code:str,parser_args,*_args,**_kwargs) -> str:
        return caesar(code, parser_args.shift, parser_args.numbers)

    def decode(self,code:str,parser_args,*_args,**_kwargs) -> str:
        return caesar(code, -parser_args.shift, parser_args.numbers)

    def __init__(self):
        super().__init__()
        self.parser.add_argument('-s','--shift',type=int,required=True,help="Shift value")
        self.parser.add_argument('-n','--numbers', action='store_true', help="Command will also shifitng numbers")

Caesar()