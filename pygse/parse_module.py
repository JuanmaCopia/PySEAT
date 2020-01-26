import argparse
import importlib
import copy

from proxy import ProxyObject, is_user_defined


def parse_command_line_args():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("file", action="store", help="Syntax: <program_file>")
    parser.add_argument(
        "-c", "--class_name", action="store", help="Syntax: <class_name>"
    )
    parser.add_argument("method", action="store", help="Syntax: <method_name>")
    parser.add_argument(
        "-d", "--depth", action="store", type=int, default=10, help="Depth limit"
    )

    return parser.parse_args()


def get_objects2(module_name, method_name, max_depth=10, class_name=None):
    result = {}
    result["module"] = importlib.import_module(module_name)
    result["class"] = getattr(result["module"], class_name)
    result["function"] = getattr(result["class"], method_name)
    result["args_types"] = parse_args_types(
        result["function"], result["class"], result["module"]
    )
    result["return_type"] = parse_return(result["function"])
    result["repok"] = parse_repok(result["class"])
    result["class_to_params"] = get_user_defined_objects(
        result["class"], result["module"]
    )
    result["real_to_proxy"] = {
        x.emulated_class: x for x in ProxyObject.__subclasses__()
    }
    result["max_depth"] = max_depth
    result["is_method"] = True
    return result


def get_objects(args):
    result = {}
    result["module"] = importlib.import_module(args.file.strip())
    result["class"] = getattr(result["module"], args.class_name.strip())
    result["function"] = getattr(result["class"], args.method.strip())
    result["args_types"] = parse_args_types(
        result["function"], result["class"], result["module"]
    )
    result["return_type"] = parse_return(result["function"])
    result["repok"] = parse_repok(result["class"])
    result["class_to_params"] = get_user_defined_objects(
        result["class"], result["module"]
    )
    result["real_to_proxy"] = {
        x.emulated_class: x for x in ProxyObject.__subclasses__()
    }
    result["max_depth"] = args.depth
    result["is_method"] = True
    return result


def set_classes(types, module):
    for i, t in enumerate(types):
        if isinstance(t, str):
            types[i] = getattr(module, t)
    return types


def parse_args_types(function, self_class, module):
    types = function.__annotations__
    if "self" not in types:
        types["self"] = self_class
    if "return" in types:
        del types["return"]
    return set_classes(list(types.values()), module)


def parse_args_types_whitout_self(function, module):
    types = function.__annotations__
    if types:
        if "self" in types:
            del types["self"]
        if "return" in types:
            del types["return"]
        return set_classes(list(types.values()), module)
    return []


def parse_return(function):
    types = function.__annotations__
    if types and "return" in types:
        return types["return"]


def parse_repok(class_obj):
    return getattr(class_obj, "rep_ok")


def get_user_defined_objects(user_def_class, module):
    class_to_types = {}
    
    types = parse_args_types_whitout_self(user_def_class.__init__, module)
    class_to_types[user_def_class] = types

    objects_added = copy.deepcopy(class_to_types[user_def_class])

    added = True if objects_added else False

    while added:
        added = False
        new_classes = []
        for c in objects_added:
            if is_user_defined(c) and c not in class_to_types.keys():
                new_classes.append(c)

        if new_classes:
            added = True
            for nc in new_classes:
                class_to_types[nc] = parse_args_types_whitout_self(nc.__init__, module)
                objects_added.extend(class_to_types[nc])

    return class_to_types

