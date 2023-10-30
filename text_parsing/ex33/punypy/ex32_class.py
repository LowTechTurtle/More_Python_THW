import re

code = [
    "def hello(x, y):",
    "    print(x + y)",
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

class Scanner(object):
    def __init__(self, code, regex):
        self.tokens = []
        self.scan(code, regex)

    def scan(self, code, regex):
        for line in code:
            i = 0
            while i < len(line):
                start = line[i:]
                for re, token in regex:
                    match = re.match(start)
                    if match:
                        begin, end = match.span()
                        i += end
                        #self.tokens.append((token, start[:end], i, end))
                        if token != "INDENT":
                            self.tokens.append((token, start[:end]))
                        break
    
    def push(self, token, name):
        self.tokens.append((token, name))
    
    def match(self, token):
        for i in range(0, len(self.tokens)):
            if self.tokens[i][0] == token:
                x = self.tokens.pop(i)
                return x[1]
        return None

    def peek(self):
        if self.tokens[0]:
            return self.tokens[0][0]
        else:
            return None
    
    def skip(self):
        self.match(self.tokens[0][0])
