from typing import Union
from ..utils.base import EncodingBase

UPPER_A_ASCII = ord('A')

def get_alphabet_index(char: str) -> int:
    """Get the index of a character in the alphabet."""
    return ord(char.upper()) - UPPER_A_ASCII

def get_alphabet_char(index: int) -> str:
    """Get the character corresponding to an index in the alphabet."""
    return chr(index + UPPER_A_ASCII)

class Scrambler:
    def __init__(self, wiring: str, pos: int = 0):
        self.forward_wiring = [None] * 26
        self.backward_wiring = [None] * 26
        self.set_wiring(wiring)
        self.postion = pos % 26

    def set_wiring(self, wiring: str):
        wiring = wiring.upper()
        self.forward_wiring = [None] * 26
        self.backward_wiring = [None] * 26
        for i, char in enumerate(wiring):
            target_index = get_alphabet_index(char)
            self.forward_wiring[target_index] = i
            self.backward_wiring[i] = target_index

    def forward(self, input_pos: Union[str, int]) -> int:
        """正向通过转盘"""
        if isinstance(input_pos, str):
            if len(input_pos) != 1 or not input_pos.isalpha():
                raise ValueError("Input must be a single alphabet character.")
            input_pos = get_alphabet_index(input_pos)
        return (self.forward_wiring[(input_pos + self.postion) % 26] - self.postion) % 26

    def backward(self, input_pos: Union[str, int]) -> str:
        """反向通过转盘"""
        if isinstance(input_pos, str):
            if len(input_pos) != 1 or not input_pos.isalpha():
                raise ValueError("Input must be a single alphabet character.")
            input_pos = get_alphabet_index(input_pos)
        return (self.backward_wiring[(input_pos + self.postion) % 26] - self.postion) % 26

    def rotate(self, steps: int = 1):
        """转动转盘"""
        self.postion = (self.postion + steps) % 26

    def reset(self):
        """重置转盘位置"""
        self.postion = 0

class EnigmaMachine:
    def __init__(self, scramblers: list[str], reflector: Union[str, None] = None,
                static:bool = False, postions: str = None):
        self.scramblers = []
        self.reversed_scramblers = []
        self.reflector = None
        self.static = static
        if not postions:
            postions = 'A' * len(scramblers)
        for i, wiring in enumerate(scramblers):
            self.scramblers.append(Scrambler(wiring, pos = get_alphabet_index(postions[i])))
        if reflector:
            self.reflector = Scrambler(reflector)
            self.reversed_scramblers = reversed(self.scramblers)

    def encode_single(self, char: str) -> str:
        """单字符编码"""
        if not char.isalpha():
            raise ValueError("Input must be a single alphabet character.")
        if not self.static:
            self.scramblers[0].rotate()
        for scrambler in self.scramblers:
            encoded_char = scrambler.forward(char)
        if self.reflector:
            encoded_char = self.reflector.forward(encoded_char)
            for scrambler in self.reversed_scramblers:
                encoded_char = scrambler.backward(encoded_char)
        return get_alphabet_char(encoded_char)

    def decode_single(self, char: str) -> str:
        """单字符解码"""
        if not char.isalpha():
            raise ValueError("Input must be a single alphabet character.")
        if not self.static:
            self.scramblers[0].rotate()
        decode_char = char
        if self.reflector:
            for scrambler in reversed(self.scramblers):
                decode_char = scrambler.forward(char)
            decode_char = self.reflector.backward(decode_char)
        for scrambler in self.scramblers:
            decode_char = scrambler.backward(decode_char)
        return get_alphabet_char(decode_char)

    def encode(self, code: str) -> str:
        """编码"""
        output = ""
        for char in code:
            if char.isalpha():
                output +=  self.encode_single(char)
            else:
                raise ValueError("Input must be alphabetic characters only.")
        return output

    def decode(self, code: str) -> str:
        """解码"""
        output = ""
        for char in code:
            if char.isalpha():
                output += self.decode_single(char)
            else:
                raise ValueError("Input must be alphabetic characters only.")
        return output

class Enigma(EncodingBase):
    name = 'enigma'
    command_help = 'enigma machine simulation'

    def encode(self, code: str, parser_args, *args, **kwargs) -> str:
        scramblers = parser_args.scrambler.split(',')
        reflector = parser_args.reflector
        static = parser_args.static
        postions = parser_args.positions.upper()
        machine = EnigmaMachine(scramblers=scramblers, reflector=reflector, static=static, postions=postions)
        return machine.encode(code)

    def decode(self, code: str, parser_args, *args, **kwargs) -> str:
        scramblers = parser_args.scrambler.split(',')
        reflector = parser_args.reflector
        static = parser_args.static
        postions = parser_args.positions.upper()
        machine = EnigmaMachine(scramblers=scramblers, reflector=reflector, static=static, postions=postions)
        return machine.decode(code)

    def __init__(self):
        super().__init__()
        self.scramblers = []
        self.reflector = None
        self.parser.add_argument('-s','--scrambler',help='Scrambler wiring', type=str)
        self.parser.add_argument('-r','--reflector',help='Reflector wiring', type=str, default=None)
        self.parser.add_argument('-p','--positions', help='Initial position of the scramblers', type=str, default=None)
        self.parser.add_argument('-S', '--static', action='store_true', help='Static mode, no rotation of scramblers')

Enigma()