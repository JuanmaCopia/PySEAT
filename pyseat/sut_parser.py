"""System Under Test Parser.

Parses all the data about the sut: Module, Class, method under test, types of
classes involved.

"""
import os
import sys
import importlib
import typing
import copy
from inspect import signature

from instrumentation import instrument
from helpers import do_add
from symbolics import Symbolic


def type_error(msg):
    print("\nsut_parser.py: In Annotations of: {}".format(msg))
    sys.exit(1)


def parse_error(msg):
    print("\nsut_parser.py: {}".format(msg))
    sys.exit(1)


def parse(module_name, class_name, methods_names):
    module = get_module(module_name)
    if not module:
        parse_error("Error importing module: {}".format(module_name))
    if not hasattr(module, class_name):
        parse_error("Class '{}' not found in {}".format(
                class_name, module_name
            )
        )
    self_class = getattr(module, class_name)
    if not hasattr(self_class, "repok"):
        parse_error("repok method not found in {}".format(self_class.__name__))
    methods = []
    for name in methods_names:
        if not hasattr(self_class, name):
            parse_error("Method '{}' not found in {}".format(name, class_name))
        methods.append(getattr(self_class, name))
    return SUT(self_class, methods)


def get_module(module_name):
    module_dir = os.path.dirname(module_name)
    sys.path = [os.path.abspath(os.path.join(module_dir))] + sys.path
    mod_basename = os.path.splitext(os.path.basename(module_name))[0]
    module = importlib.import_module(mod_basename)
    return module


def get_types_dict(method, belonging_cls) -> dict:
    pt_dict = get_annotations_types(method, belonging_cls)

    defaults = typing._get_defaults(method)
    for name in defaults:
        pt_dict[name] = get_default_type(pt_dict[name])

    if "self" not in pt_dict:
        pt_dict["self"] = belonging_cls
    return pt_dict


def get_default_type(generic_alias):
    args = typing.get_args(generic_alias)
    assert is_user_defined(args[0])
    return args[0]


def get_types_list(param_list, types_dict) -> list:
    types = []
    for param_name in param_list.keys():
        types.append(types_dict[param_name])
    return types


def is_user_defined(typ):
    return typ.__module__ != "builtins"


def is_supported_builtin(typ):
    return typ in Symbolic._supported_types


def map_all_classes(types_list) -> dict:
    classes = set()
    worklist = []
    class_map = {}

    for typ in types_list:
        if is_user_defined(typ) and do_add(classes, typ):
            worklist.append(typ)

    while worklist:
        current = worklist.pop(0)

        cls_data = ClassData(current)
        class_map[current] = cls_data

        for typ in cls_data.instance_attr_list:
            if is_user_defined(typ) and do_add(classes, typ):
                worklist.append(typ)
    return class_map


def get_annotations_types(obj, cls_name=None):
    try:
        types = typing.get_type_hints(obj)
    except NameError as e:
        if cls_name:
            type_error("'{}' of {}, {}".format(obj.__name__, cls_name, e))
        else:
            type_error("'{}', {}".format(obj.__name__, e))
    else:
        for typ in types.values():
            if not is_user_defined(typ) and not is_supported_builtin(typ):
                type_error("'{}', '{}' is not supported yet".format(obj.__name__, typ))
        return types


def check_method_annotations(method_data):
    method_name = method_data.name
    if len(method_data.types_dict) != method_data.amount_params:
        type_error(
            "'{}' of {} There are missing annotations".format(
                method_name, method_data.belonging_cls
            )
        )
    for name, typ in method_data.types_dict.items():
        if name != "self" and is_user_defined(typ) and method_name != "__init__":
            type_error(
                "'{}' of {}, structure args only supported in __init__ methods".format(
                    method_name, method_data.belonging_cls
                )
            )


class ClassData:
    def __init__(self, this_class):
        self.this_class = this_class
        self.instance_attr_types = get_annotations_types(this_class)
        self.instance_attr_list = list(self.instance_attr_types.values())
        self.repok_method = self.get_repok()
        self.init_data = MethodData(this_class.__init__, this_class)

    def get_repok(self) -> callable:
        if hasattr(self.this_class, "repok"):
            return getattr(self.this_class, "repok")
        return None


class MethodData:
    def __init__(self, method, belonging_cls):
        self.belonging_cls = belonging_cls
        self.method = method
        self.name = method.__name__
        self.signature = signature(method)
        self.params = self.signature.parameters
        self.amount_params = len(self.params)
        self.types_dict = get_types_dict(method, belonging_cls)
        self.return_type = self.types_dict.pop("return", None)
        check_method_annotations(self)
        self.types_list = get_types_list(self.params, self.types_dict)


class SUT:
    """System Under Test.

    Parses and stores the data objects of the sut.

    Attributes:

    """

    def __init__(self, the_class, methods):
        self.current_method = None
        self.methods_map = {m.__name__: MethodData(m, the_class) for m in methods}
        types_list = []
        for md in self.methods_map.values():
            types_list += md.types_list
        self.class_map = map_all_classes(types_list)
        for clss, class_data in self.class_map.items():
            instrument(clss, class_data.instance_attr_types.keys())

    def get_method(self):
        return self.current_method.method

    def get_method_name(self):
        return self.current_method.name

    def get_method_param_types(self):
        return copy.deepcopy(self.current_method.types_list)

    def get_cls_init_types(self, clss):
        return copy.deepcopy(self.class_map[clss].init_data.types_list)

    def get_params_type_dict(self, clss):
        return copy.deepcopy(self.class_map[clss].init_data.types_dict)

    def get_attr_type(self, clss, attr_name):
        return self.class_map[clss].instance_attr_types[attr_name]

    def get_instance_attr_dict(self, clss):
        return self.class_map[clss].instance_attr_types
