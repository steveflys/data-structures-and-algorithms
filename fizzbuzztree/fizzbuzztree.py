from .bst import BST

def is_divisable(node):

    if node.val % 15 == 0:
        node.val = 'FizzBuzz'
    elif node.val % 3 == 0:
        node.val = 'Fizz'   
    elif node.val % 5 == 0:
        node.val = 'Buzz'


def fizz_buzz_tree(bst):

    bst.in_order(is_divisable)

    return bst