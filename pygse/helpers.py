def is_special_attr(attr_name):
    return attr_name.endswith("_is_initialized") or attr_name in [
        "_objid",
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
    return hasattr(obj, "_engine")


def is_initialized(obj, attr_name):
    assert not has_prefix(attr_name)
    return hasattr(obj, get_initialized_name(attr_name))


def set_to_initialized(structure, prefixed_name):
    assert has_prefix(prefixed_name)
    name = remove_prefix(prefixed_name)
    init_name = get_initialized_name(name)
    setattr(structure, init_name, True)


def get_initialized_name(attr_name):
    assert not has_prefix(attr_name)
    return "_" + attr_name + "_is_initialized"


def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def print_list(l: list, indent):
    for elem in l:
        print(indent + str(elem))


def get_dict(instance):
    return {
        remove_prefix(key): value
        for (key, value) in instance.__dict__.items()
        if not is_special_attr(key)
    }


def get_dict_of_prefixed(instance):
    return {key: value for (key, value) in instance.__dict__.items() if has_prefix(key)}


def var_name(obj):
    if hasattr(obj, "_objid"):
        return type(obj).__name__.lower() + str(obj._objid)
    assert False


def is_same(obj1, obj2):
    return obj1._objid == obj2._objid and isinstance(obj1, type(obj2))


def search_obj(obj, structure):
    visited = set()
    visited.add(structure)
    worklist = []
    worklist.append(structure)
    while worklist:
        current = worklist.pop(0)
        if is_same(obj, current):
            return current
        for name, value in current.__dict__.items():
            if is_user_defined(value) and has_prefix(name) and do_add(visited, value):
                worklist.append(value)
    return None
