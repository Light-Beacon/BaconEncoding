import pkgutil
import importlib

from .utils.command import main as command_main, MAIN_PARSER

package = importlib.import_module('baconencoding.encoding_parsers')
for loader, name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
    if not is_pkg:
        module = importlib.import_module(name)

try:
    import argcomplete
    argcomplete.autocomplete(MAIN_PARSER)
finally:
    pass

def main():
    command_main()

if __name__ == '__main__':
    command_main()
