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


def seek_cyclically_equivalent_ends(string, middle=None):
    """
    Seek a prefix and suffix pair of string substrings that are cyclically equivalent.
    """
    if middle is None:
        middle = len(string) // 2
    middle_right = middle

    def decrement_middle():
        nonlocal middle, middle_right
        middle -= 1
        middle_right += 1

    def get_prefix():
        return string[:middle]

    def get_suffix():
        return string[middle_right + (middle_right % 2 == 0):]

    prefix = get_prefix()
    suffix = get_suffix()

    while not cyclically_equivalent(prefix, suffix) and middle:
        decrement_middle()
        prefix = get_prefix()
        suffix = get_suffix()

    return prefix, suffix, middle


def compute_cyclically_equivalent_ends_length(string):
    """Compute length of two ends of a string that are cyclically equivalent."""
    return seek_cyclically_equivalent_ends(string)[2]


if __name__ == '__main__':
    print(compute_cyclically_equivalent_ends_length(input()))
