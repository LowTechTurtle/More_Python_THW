from scanner import * #imagine module that will have 4 function peek, match, skip and scan
from pprint import pprint

def root(tokens):
    first = peek(tokens)
    
    if first == "DEF":
        return function_definition(tokens)
    elif first == "NAME":
        name = match(tokens, "NAME")
        second = peek(tokens)

        if second == "LPAREN":
            return function_call(tokens, name)
        else:
            assert False, "Not a FUNCDEF or FUNCCALL"

def function_definition(tokens):
    skip(tokens)
    name = match(tokens, "NAME")
    match(tokens, "LPAREN")
    params = parameters(tokens)
    match(tokens, "RPAREN")
    match(tokens, "COLON")
    return {"type": "FUNCDEF", "name": name, "params": params}

def parameters(tokens):
    params = []
    start = peek(tokens)
    while start != "RPAREN":
        params.append(expression(token))
        start = peek(tokens)
        if start != "RPAREN":
            assert match(tokens, "COMMA")
    return params

def expression(tokens):
    start = peek(tokens)
    
    if start == "NAME":
        name = match(tokens, "NAME")
        if peek(tokens) == "PLUS":
            return plus(tokens, name)
        else:
            return name

    elif start == "INTEGER":
        number = match(tokens, "INTEGER")
        if peek(tokens) == "PLUS":
            return plus(tokens, number)
        else:
            return number

    else:
        assert False, f"Syntax Error {start}"

def plus(tokens, left):
    match(tokens, "PLUS")
    right = expression(tokens)
    return {"type": "PLUS", "left": left, "right": right}

def function_call(tokens, name):
    match(tokens, "LPAREN")
    params = parameters(tokens)
    match(tokens, "RPAREN")
    return {"type": "FUNCCALL", "NAME": name, 'params': params}

def main(tokens):
    results = []
    while tokens:
        results.append(root(tokens))
    return results


parsed = main(scan(code))
pprint(parsed)
