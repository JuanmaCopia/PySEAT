def instrument(clss, attr_names):
    for attr_name in attr_names:
        add_property(clss, attr_name)

    setattr(clss, "_engine", None)
    setattr(clss, "_vector", [])
    setattr(clss, "_id", 0)
    # setattr(clss, "_objid", -1)
    setattr(clss, "_recursion_depth", 0)


def add_property(clss, prop_name):
    code = format_property_code(prop_name)
    d = {}
    exec(code.strip(), globals(), d)
    setattr(clss, prop_name, d[prop_name])


def format_property_code(prop_name):
    code = """
@property
def {n}(self):
    return self._engine.lazy_initialization(self, "{n}")

@{n}.setter
def {n}(self, value):
    return self._engine.lazy_set_attr(self, "{n}", value)
    """.format(
        **{"n": prop_name}
    )
    return code
