import argparse

# 创建解析器
MAIN_PARSER = argparse.ArgumentParser()

SUB_PARSERS = MAIN_PARSER.add_subparsers(
    help='Encoding', dest='encoding')
MAPPING = {}

def add_parser(*args,**kwargs):
    """Add command parser"""
    return SUB_PARSERS.add_parser(*args,**kwargs)

def regist_encoding(name,encoding_parser_func):
    MAPPING[name] = encoding_parser_func

def main():
    args = MAIN_PARSER.parse_args()
    print(MAPPING[args.encoding](args))

if __name__ == '__main__':
    main()
