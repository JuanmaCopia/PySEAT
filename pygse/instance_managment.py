SYMBOLIC_PREFIX = "_pygse_"
ISINIT_PREFIX = "_pygse_is_init"
SYM_PREFIX_LEN = len(SYMBOLIC_PREFIX)


def is_special_attr(attr_name):
    return attr_name.startswith(ISINIT_PREFIX) or attr_name in [
        "_objid",
    ]


def has_prefix(attr_name):
    return attr_name.startswith(SYMBOLIC_PREFIX)


def remove_prefix(attr_name):
    if attr_name.startswith(SYMBOLIC_PREFIX):
        return attr_name[SYM_PREFIX_LEN:]
    return attr_name


def is_user_defined(obj):
    if obj is None:
        return False
    return hasattr(obj, "_engine")


def is_initialized(obj, attr_name):
    init_name = ISINIT_PREFIX + attr_name
    if hasattr(obj, init_name):
        return getattr(obj, init_name)
    else:
        setattr(obj, init_name, False)
        return False


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
