from .stack import Stack
import re


def switch(char):
    """this will return the closing bracket for each braket type"""
    if re.match(r"[(]", char):
        return ')'
    if re.match(r"[[]", char):
        return ']'
    if re.match(r"[{]", char):
        return '}'


def multi_bracket_validation(input):
    """this will push any opening brackets into a stack, poping off the stack for every closing bracket, and verifing it matches tnhe last opening bracket pushed""" 
    stack = Stack()
    new = ''
    top = ''
    for char in input:
        if re.match(r"[([{]", char):
            new = switch(char)
            stack.push(new)
        elif re.match(r"[)\]}]", char):
            top = stack.pop()
            if str(top) != char:
                return False
    if stack.top is None:
        return True
    else:
        return False
