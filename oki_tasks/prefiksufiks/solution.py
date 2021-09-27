middle = int(float(input()) // 2)
text = input()


def shift_left(string):
    """
    Move the first letter of a string to the end of the string.
          ←   ←
    | a | b | c |   |   ->  |   | b | c | a |
      ↓  →  →  →  ↑
    """
    start, *rest = string
    return ''.join((*rest, start))


def cyclically_equivalent(shifted, referred):
    """
    Check if two strings are cyclically equivalent.
    """
    for i in range(shifted):
        if shifted == referred:
            return True
        shifted = shift_left(shifted)
    return False
