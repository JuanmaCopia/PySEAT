import pygse.proxy as proxy


def is_supported_builtin(obj):
    return proxy.ProxyObject.is_supported_builtin(obj)


def is_special_attr(attr_name):
    return attr_name.endswith("_is_initialized") or attr_name in [
        "_concretized",
        "_identifier",
        "_generated",
        "_vector",
        "_id",
    ]


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


def is_symbolic(obj):
    return isinstance(obj, proxy.ProxyObject)


def is_symbolic_bool(obj):
    return isinstance(obj, proxy.BoolProxy)


def is_user_defined(obj):
    return hasattr(obj, "_vector")


def get_initialized_name(attr_name):
    return "_" + attr_name + "_is_initialized"


def timeout_handler(signum, frame):
    raise Exception("Timeout")
