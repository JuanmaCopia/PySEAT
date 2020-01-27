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
    parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument')

    return parser.parse_args()


def get_objects2(module_name, method_name, max_depth=10, class_name=None):
    target_data = {}
    target_data["module"] = importlib.import_module(module_name)
    target_data["class"] = getattr(target_data["module"], class_name)
    target_data["function"] = getattr(target_data["class"], method_name)
    target_data["args_types"] = parse_args_types(
        target_data["function"], target_data["class"], target_data["module"]
    )
    target_data["return_type"] = parse_return(target_data["function"])
    target_data["repok"] = parse_repok(target_data["class"])
    target_data["class_to_params"] = get_user_defined_objects(
        target_data["class"], target_data["module"]
    )
    target_data["real_to_proxy"] = {
        x.emulated_class: x for x in ProxyObject.__subclasses__()
    }
    target_data["max_depth"] = max_depth
    target_data["is_method"] = True
    return target_data


def get_objects(args):
    target_data = {}
    target_data["module"] = importlib.import_module(args.file.strip())
    target_data["class"] = getattr(target_data["module"], args.class_name.strip())
    target_data["function"] = getattr(target_data["class"], args.method.strip())
    target_data["args_types"] = parse_args_types(
        target_data["function"], target_data["class"], target_data["module"]
    )
    target_data["return_type"] = parse_return(target_data["function"])
    target_data["repok"] = parse_repok(target_data["class"])
    target_data["class_to_params"] = get_user_defined_objects(
        target_data["class"], target_data["module"]
    )
    target_data["real_to_proxy"] = {
        x.emulated_class: x for x in ProxyObject.__subclasses__()
    }
    target_data["max_depth"] = args.depth
    target_data["is_method"] = True
    target_data["verbose"] = args.verbose
    return target_data


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

