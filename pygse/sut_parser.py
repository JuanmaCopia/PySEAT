"""System Under Test Parser.

Parses all the data about the sut: Module, Class, method under test, types of
classes involved.

"""

import importlib
import copy

from pygse.helpers import is_user_defined
from pygse.engine_errors import MissingTypesError


class SUT:
    """System Under Test.

    Parses and stores the data objects of the sut.

    Attributes:
        sclass (class): The class of the method under test.
        function (function): Method Under Test.
        types (list[type]): Ordered list of the types of the method Pprameters.
        class_params_map (dict): Maps a class to a dict with it's parameters/type
        init method parameter's types.
        is_method (bool): Whether the sut is a method (True) or a Function (False).

    """

    def __init__(self):
        self.sclass = None
        self.function = None
        self.params = []
        self.class_params_map = {}
        self.is_method = False

    def get_init_params(self, typ):
        if typ in self.class_params_map:
            return self.class_params_map[typ]


def parse(module_name, function_name, class_name=None):
    sut = SUT()
    module = importlib.import_module(module_name)
    if class_name:
        sut.is_method = True
        sut.sclass = getattr(module, class_name)
        sut.function = getattr(sut.sclass, function_name)
        sut.params = parse_params(sut.function, sut.sclass, module)
        if sut.function.__code__.co_argcount != len(sut.params):
            raise MissingTypesError("Types missing in: " + function_name)
        sut.class_params_map = get_user_defined_objects(sut.sclass, module)
    return sut


def parse_params(function, sclass, module, include_self=True):
    """Parses the parameters of a function.
    """
    params = {}
    if include_self:
        params["self"] = sclass

    for name, typ in function.__annotations__.items():
        if name != "self" and name != "return":
            if isinstance(typ, str):
                params[name] = getattr(module, typ)
            else:
                params[name] = typ
    return params


def get_user_defined_objects(sclass, module):
    class_to_types = {}
    params = parse_params(sclass.__init__, sclass, module, False)
    class_to_types[sclass] = params

    if params:
        objects_added = copy.deepcopy(list(params.values()))
        added = True

        while added:
            added = False
            new_classes = []

            for typ in objects_added:
                if is_user_defined(typ) and typ not in class_to_types.keys():
                    new_classes.append(typ)

            if new_classes:
                added = True
                for nc in new_classes:
                    class_to_types[nc] = parse_params(nc.__init__, nc, module, False)
                    objects_added.extend(class_to_types[nc].values())
    return class_to_types
