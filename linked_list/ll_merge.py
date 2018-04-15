from .linked_list import Linked_List


def ll_merge(ll_1, ll_2):

    head = ll_1.head
    current = ll_1.head
    cache = ll_2 head

    while cache:
        temp = current.next
        current.next = cache
        cache = temp
        current = current.next

    return head