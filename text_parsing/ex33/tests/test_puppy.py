from punypy.ex33_class import *
from punypy.ex32_class import *
import re
from pprint import pprint

code = [
    "def hello(x, y):",
    "    print(x + y + z + t)",
    "hello(10, 20)",
    ]

TOKENS = [
        (re.compile(r"^def"), "DEF"),
        (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
        (re.compile(r"^[0-9]+"), "INTEGER"),
        (re.compile(r"^\("), "LPAREN"),
        (re.compile(r"^\)"), "RPAREN"),
        (re.compile(r"^\+"), "PLUS"),
        (re.compile(r"^:"), "COLON"),
        (re.compile(r"^,"), "COMMA"),
        (re.compile(r"^\s+"), "INDENT"),
        ]

def test_puppy():
    global code
    global TOKENS
    scanner = Scanner(code, TOKENS)
    pprint(scanner.tokens)
    puppy = VeryPunyPyParser(scanner)
    puppy.parse()
    pprint(puppy.parsed)
