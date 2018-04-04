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
    """this will push any opening brackets into a stack, poping off the stack for every closing bracket, and verifing it matches tnhe last opening"""
    stack = Stack()

    for char in input:
        if re.match(r"[([{]", char):
            stack.push(switch(char))
        elif re.match(r"[)\]}]", char):
            if str(stack.pop()) != char:
                return False
    if stack.top is None:
        return True
    else:
        return False
