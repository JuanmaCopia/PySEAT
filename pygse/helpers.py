def is_special_attr(attr_name):
    return attr_name.endswith("_is_initialized") or attr_name in [
        "_identifier",
        "_recursion_depth",
        "_vector",
        "_id",
    ]


def has_prefix(attr_name):
    return attr_name.startswith("s_")


def remove_prefix(attr_name):
    if attr_name.startswith("s_"):
        return attr_name[2:]
    return attr_name


def add_prefix(attr_name):
    return "s_" + attr_name


def keep_first_n_items(l, n):
    new_list = []
    i = 0
    while i < n:
        new_list.insert(i, l[i])
        i += 1
    return new_list


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


def is_user_defined(obj):
    if obj is None:
        return False
    return hasattr(obj, "_vector")


def set_to_initialized(structure, attr_name):
    if not is_special_attr(attr_name):
        name = attr_name
        if has_prefix(name):
            name = remove_prefix(name)
        init_name = get_initialized_name(name)
        if hasattr(structure, init_name):
            setattr(structure, init_name, True)


def get_initialized_name(attr_name):
    return "_" + attr_name + "_is_initialized"


def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def print_list(l: list, indent):
    for elem in l:
        print(indent + str(elem))
