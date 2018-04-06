from .stack import Stack


def finished():
    if (peg_a.peek() is None and peg_b.peek() is None and beg_c.peek() == 1):
        finished = True

done = 0

a = 0

b = 0

c = 0


def towers_of_hanoi(n):
    global a, b, c
    i = list(range(1, n + 1))
    i.reverse()
    peg_a = Stack(i)
    peg_b = Stack()
    peg_c = Stack()

    def a_to_b():
        if peg_b.peek() is False:
            peg_b.push(peg_a.pop())
        elif peg_a.peek() < peg_b.peek():
            peg_b.push(peg_a.pop())
        elif peg_a.peek() is False:
            peg_a.push(peg_b.pop())
        elif peg_b.peek() < peg_a.peek():
            peg_a.push(peg_b.pop())

    def a_to_c():
        if peg_c.peek() is False:
            peg_c.push(peg_a.pop())
        elif peg_a.peek() < peg_c.peek():
            peg_c.push(peg_a.pop())
        elif peg_a.peek() is False:
            peg_a.push(peg_c.pop())
        elif peg_c.peek() < peg_a.peek():
            peg_a.push(peg_c.pop())

    def b_to_c():
        if peg_c.peek() is False:
            peg_c.push(peg_b.pop())
        elif peg_b.peek() < peg_c.peek():
            peg_c.push(peg_b.pop())
        elif peg_b.peek() is False:
            peg_b.push(peg_c.pop())
        elif peg_c.peek() < peg_b.peek():
            peg_b.push(peg_c.pop())

    finished is False
    if n % 2 == 0:
        while finished is False:
            finished()
            a_to_b()
            finished()
            a_to_c()
            finished()
            b_to_c()
        done = 1
    else:
        while finished is False:
            finished()
            a_to_c()
            finished()
            a_to_b()
            finished()
            b_to_c()
        done = 1
    a = peg_a.peek()
    b = peg_b.peek()
    c = peg_c.peek().val
    return 'finished'
