"""Print each level of a k-ary tree with a line break between each level."""
from .k_tree import KTree


def print_level_order(tree):
    """Print each level of a k-ary tree with a line break between each level."""
    last_child = tree.root
    stringed = ''

    def find_row(node):
        nonlocal stringed, last_child
        stringed += str(node.val)
        if node == last_child:
            if not node.children:
                stringed += '\n'
            else:
                last_child = node.children[-1]
                stringed += '\n'

    tree.breadth_first(find_row)

    return stringed
