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


# def get_objects2(module_name, method_name, max_depth=10, class_name=None):
#     result = {}
#     result["module"] = importlib.import_module(module_name)

#     if class_name:
#         result["class"] = getattr(result["module"], class_name)
#         result["function"] = getattr(result["class"], method_name)
#         result["is_method"] = True
#         result["class_to_params"] = get_user_defined_objects(result["class"])
#     else:
#         result["class"] = None
#         result["is_method"] = False
#         result["function"] = getattr(result["module"], method_name)

#     result["primitives"] = {x.emulated_class: x for x in ProxyObject.__subclasses__()}
#     result["function_args"] = parse_type_contract(result["function"])
#     result["max_depth"] = max_depth

#     return result


def get_objects(args):
    result = {}
    result["module"] = importlib.import_module(args.file.strip())
    result["class"] = getattr(result["module"], args.class_name.strip())
    result["function"] = getattr(result["class"], args.method.strip())
    result["args_types"] = parse_method_types(result["function"], result["class"])
    result["return_type"] = parse_return(result["function"])
    result["repok"] = parse_repok(result["class"])
    result["class_to_params"] = get_user_defined_objects(result["class"])
    result["real_to_proxy"] = {
        x.emulated_class: x for x in ProxyObject.__subclasses__()
    }
    result["max_depth"] = args.depth
    result["is_method"] = True
    return result


def parse_method_types(function, self_class):
    types = function.__annotations__
    if "self" not in types:
        types["self"] = self_class
    if "return" in types:
        del types["return"]
    result = list(types.values())
    return result


def parse_types(function):
    types = function.__annotations__
    if types:
        if "self" in types:
            del types["self"]
        if "return" in types:
            del types["return"]
        return list(types.values())
    return []


def parse_return(function):
    types = function.__annotations__
    if types and "return" in types:
        return types["return"]


def parse_repok(class_obj):
    return getattr(class_obj, "rep_ok")


def get_user_defined_objects(user_def_class):
    class_to_types = {}
    class_to_types[user_def_class] = parse_types(user_def_class.__init__)

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
                class_to_types[nc] = parse_types(nc.__init__)
                objects_added.extend(class_to_types[nc])

    return class_to_types

