def is_special_attr(attr_name):
    return attr_name.endswith("_is_initialized") or attr_name in [
        "_identifier",
        "_generated",
        "_recursion_depth",
        "_vector",
        "_id",
    ]


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
    init_name = get_initialized_name(attr_name)
    if hasattr(structure, init_name):
        setattr(structure, init_name, True)


def get_initialized_name(attr_name):
    return "_" + attr_name + "_is_initialized"
