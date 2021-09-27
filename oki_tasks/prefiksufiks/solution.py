def cyclically_equivalent(a, b):
    return a in (b + b)


def seek_cyclically_equivalent_ends(string, middle=None):
    if middle is None:
        middle = len(string) // 2
    middle_right = middle + 1 + (middle % 2 != 1)
    prefix = string[:middle]
    suffix = string[middle_right:]

    while middle and not cyclically_equivalent(prefix, suffix):
        middle -= 1
        middle_right += 1
        prefix = string[:middle]
        suffix = string[middle_right:]

    return prefix, suffix, middle


def compute_cyclically_equivalent_ends_length(string, middle=None):
    return seek_cyclically_equivalent_ends(string, middle)[2]


if __name__ == '__main__':
    print(compute_cyclically_equivalent_ends_length(middle=int(input()) // 2, string=input()))
