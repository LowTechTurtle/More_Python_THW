class VeryPunyPyParser(object):
    def __init__(self, scanner):
        self.scanner = scanner
        self.parsed = []

    def root(self):
        first = self.scanner.peek()

        if first == 'DEF':
            return self.function_definition()

        elif first == 'NAME':
            name = self.scanner.match('NAME')
            second = self.peek()

            if second == 'LPAREN':
                return self.function_call(name)
        else:
            assert False, "Not a FUNCDEF or FUNCCALL"

    def function_definition(self):
        self.scanner.skip()
        name = self.scanner.match("NAME")
        self.scanner.match("LPAREN")
        params = self.parameters()
        self.scanner.match('RPAREN')
        self.scanner.match("COLON")
        return {'type': 'FUNCDEF', 'name': name, 'params': params}

    def parameters(self):
        params = []
        start = self.scanner.peek()
        while start != 'RPAREN':
            params.append(self.expression())
            start = self.scanner.peek()
            if start != 'RPAREN':
                assert self.scanner.match('COMMA')
        return params
    
    def expression(self):
        start = self.scanner.peek()
        if start == 'NAME':
            name = self.scanner.match('NAME')
            if self.scanner.peek() == 'PLUS':
                return self.plus(name)
            else:
                return name
        elif start == 'INTEGER':
            number = self.scanner.match('INTEGER')
            if self.scanner.peek() == 'PLUS':
                return self.plus(number)
            else:
                return number
        else:
            assert False, "Syntax error %r" % start
    
    def plus(self, left):
        self.scanner.match('PLUS')
        right = self.expression()
        return {'type': 'PLUS', 'left': left, 'right': right}

    def parse(self):
        while self.scanner.tokens:
            self.parsed.append(self.root())
        return results
