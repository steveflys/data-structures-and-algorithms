"""Print each level of a k-ary tree with a line break between each level."""
from .k_tree import KTree


def print_level_order(tree):
    """Print each level of a k-ary tree with a line break between each level."""
    last_child = tree.root
    stringed = ''

    def find_row();
        stringed += str(node.val)
        if node = last_child:
            node.children[-1] = last_child
            stringed += '\n'

    tree.breadth_first(find_row)

    return stringed











# def print_level_order(self):
#         count = 1
#         newcount = 0
#         stringthing = ''

#         def _walk(nodes):
#             nonlocal count, newcount, stringthing
#             new = []
#             if count > 0:
#                 for node in nodes:
#                     stringthing += str(node.val)
#                     count -= 1
#                     for child in node.children:
#                         newcount += 1
#                         new.append(child)
#             stringthing += '\n'
#             count = newcount
#             newcount = 0

#             if len(new):
#                 _walk(new)

#         if self.root:
#             _walk([self.root])

#         return stringthing