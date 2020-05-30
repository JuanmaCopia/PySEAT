def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def print_list(l: list, indent):
    for elem in l:
        print(indent + str(elem))
