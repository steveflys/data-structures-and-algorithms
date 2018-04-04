from .stack import Stack
import re


def switch(char):
    if re.match(r"[(]", char):
        return ')'
    if re.match(r"[[]", char):
        return ']'
    if re.match(r"[{]", char):
        return '}'


def multi_bracket_validation(input):

    stack = Stack()
    new = ''
    top = ''
    for char in input:
        if re.match(r"[([{]", char):
            new = switch(char)
            # import pdb; pdb.set_trace()
            stack.push(new)
        elif re.match(r"[)\]}]", char):
            # import pdb; pdb.set_trace()
            top = stack.pop()
            if str(top) != char:
                return False
    if stack.top is None:
        return True
    else:
        return False
