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
import instance_managment as im
from helpers import do_add

# from exceptions import MissingTypesError


def parse(module_name, class_name, method_name):
    module = get_module(module_name)
    self_class = getattr(module, class_name)
    method = getattr(self_class, method_name)
    return SUT(self_class, method)


def get_module(module_name):
    module_dir = os.path.dirname(module_name)
    sys.path = [os.path.abspath(os.path.join(module_dir))] + sys.path
    mod_basename = os.path.splitext(os.path.basename(module_name))[0]
    module = importlib.import_module(mod_basename)
    return module


def get_types_dict(method, belonging_cls) -> dict:
    pt_dict = typing.get_type_hints(method)

    defaults = typing._get_defaults(method)
    for name in defaults:
        pt_dict[name] = get_default_type(pt_dict[name])

    if "self" not in pt_dict:
        pt_dict["self"] = belonging_cls
    return pt_dict


def get_default_type(generic_alias):
    args = typing.get_args(generic_alias)
    assert im.is_user_defined(args[0])
    return args[0]


def get_types_list(param_list, types_dict) -> list:
    types = []
    for param_name in param_list.keys():
        types.append(types_dict[param_name])
    return types


def map_all_classes(types_list) -> set:
    classes = set()
    worklist = []
    class_map = {}

    for typ in types_list:
        if im.is_user_defined(typ) and do_add(classes, typ):
            worklist.append(typ)

    while worklist:
        current = worklist.pop(0)

        cls_data = ClassData(current)
        class_map[current] = cls_data

        for typ in cls_data.instance_attr_list:
            if im.is_user_defined(typ) and do_add(classes, typ):
                worklist.append(typ)
    return class_map


class ClassData:
    def __init__(self, this_class):
        self.this_class = this_class
        self.instance_attr_types = typing.get_type_hints(this_class)
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
        self.signature = signature(method)
        self.params = self.signature.parameters
        self.amount_params = len(self.params)

        self.types_dict = get_types_dict(method, belonging_cls)
        self.return_type = self.types_dict.pop("return", None)
        self.types_list = get_types_list(self.params, self.types_dict)
        assert len(self.types_list) == self.amount_params


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

    def __init__(self, the_class, method):
        self.method_data = MethodData(method, the_class)
        self.class_map = map_all_classes(self.method_data.types_list)

    def get_method(self):
        return self.method_data.method

    def get_method_name(self):
        return self.method_data.method.__name__

    def get_method_param_types(self):
        return copy.deepcopy(self.method_data.types_list)

    def get_cls_init_types(self, clss):
        return copy.deepcopy(self.class_map[clss].init_data.types_list)

    def get_params_type_dict(self, clss):
        return copy.deepcopy(self.class_map[clss].init_data.types_dict)

    def get_attr_type(self, clss, attr_name):
        return self.class_map[clss].instance_attr_types[attr_name]

    def get_instance_attr_dict(self, clss):
        return self.class_map[clss].instance_attr_types
