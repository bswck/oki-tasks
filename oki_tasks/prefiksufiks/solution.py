def cyclically_equivalent(a, b):
    return ' '.join(a) in ' '.join([' '.join(b)] * 2)


def seek_cyclically_equivalent_ends(string, middle=None):
    if middle is None:
        middle = len(string) // 2
    middle_right = middle + 1 + (middle % 2 != 1)

    def decrement_middle():
        nonlocal middle, middle_right
        middle -= 1
        middle_right += 1

    def get_prefix():
        return string[:middle]

    def get_suffix():
        return string[middle_right:]

    prefix = get_prefix()
    suffix = get_suffix()

    while middle and not cyclically_equivalent(prefix, suffix):
        decrement_middle()
        prefix = get_prefix()
        suffix = get_suffix()

    return prefix, suffix, middle


def compute_cyclically_equivalent_ends_length(string, middle=None):
    return seek_cyclically_equivalent_ends(string, middle)[2]


if __name__ == '__main__':
    print(compute_cyclically_equivalent_ends_length(middle=int(input()) // 2, string=input()))
