"""Find the first repeated word in a string."""


def repeated_word(string):
    """Find the first repeated word in a string."""
    word = ''
    words = [] * len(string)
    index = -1
    leters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

    for char in string:
        if char in leters:
            word += char
        else:
            if word in words:
                repeat = ''
                for char in word:
                    repeat += char
                    return repeat
            else:
                index += 1
                words[index] = word
                word = ''
