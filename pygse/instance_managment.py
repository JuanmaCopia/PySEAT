PREFIX = "s_"
ISINIT_PREFIX = "_"
ISINIT_POSFIX = "_is_initialized"


def is_special_attr(attr_name):
    return attr_name.endswith(ISINIT_POSFIX) or attr_name in [
        "_objid",
        "_recursion_depth",
    ]


def has_prefix(attr_name):
    return attr_name.startswith(PREFIX)


def remove_prefix(attr_name):
    if attr_name.startswith(PREFIX):
        return attr_name[2:]
    return attr_name


def add_prefix(attr_name):
    return PREFIX + attr_name


def is_user_defined(obj):
    if obj is None:
        return False
    return hasattr(obj, "_engine")


def is_initialized(obj, attr_name):
    assert not has_prefix(attr_name)
    init_name = get_initialized_name(attr_name)
    if hasattr(obj, init_name):
        return getattr(obj, init_name)
    else:
        setattr(obj, init_name, False)
        return False


def set_to_initialized(structure, name):
    if has_prefix(name):
        name = remove_prefix(name)
    assert not has_prefix(name)
    init_name = get_initialized_name(name)
    setattr(structure, init_name, True)


def get_initialized_name(attr_name):
    assert not has_prefix(attr_name)
    return ISINIT_PREFIX + attr_name + ISINIT_POSFIX


def get_attr(obj, attr_name):
    return getattr(obj, add_prefix(attr_name))


def set_attr(obj, attr_name, value):
    return setattr(obj, add_prefix(attr_name), value)


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


def is_tracked(obj):
    return hasattr(obj, "_objid")
