import argparse
import importlib
import copy

from contracts import TypeContract, ContractError
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

    if class_name:
        result["class"] = getattr(result["module"], class_name)
        result["function"] = getattr(result["class"], method_name)
        result["is_method"] = True
        result["class_to_params"] = get_user_defined_objects(result["class"])
    else:
        result["class"] = None
        result["is_method"] = False
        result["function"] = getattr(result["module"], method_name)

    result["primitives"] = {x.emulated_class: x for x in ProxyObject.__subclasses__()}
    result["function_args"] = parse_type_contract(result["function"])
    result["max_depth"] = max_depth

    return result

def get_objects(args):
    result = {}
    result["module"] = importlib.import_module(args.file.strip())

    if args.class_name:
        result["class"] = getattr(result["module"], args.class_name.strip())
        result["function"] = getattr(result["class"], args.method.strip())
        result["is_method"] = True
        result["class_to_params"] = get_user_defined_objects(result["class"])
    else:
        result["class"] = None
        result["is_method"] = False
        result["function"] = getattr(result["module"], args.method.strip())

    result["primitives"] = {x.emulated_class: x for x in ProxyObject.__subclasses__()}
    result["function_args"] = parse_type_contract(result["function"])
    result["max_depth"] = args.depth

    return result

def parse_type_contract(function):
    try:
        t_contract = TypeContract.parse(function)
        args = t_contract.types["args"]
        # TODO: return also kwargs
        # Also check if exists other kind of arguments in python functions,
        # like vargargs etc

        # TODO: there is a problem here, a list of int class is returned in one
        # of the arguments, when should be just an int class. hardcoded solution_
        res = []
        for i, arg in enumerate(args):
            if type(arg) == list:
                res.append(arg[0])
            else:
                res.append(arg)
        return res
    except ContractError as error:
        exc_name, exc_msg = repr(error).split("(", 1)
        print("\n{}: {}\n".format(exc_name, exc_msg[1:-2]))


def get_user_defined_objects(user_def_class):
    class_to_types = {}
    class_to_types[user_def_class] = get_init_param_types(user_def_class)

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
                class_to_types[nc] = get_init_param_types(nc)
                objects_added.extend(class_to_types[nc])

    return class_to_types


def get_init_param_types(user_def_class):
    attributes = parse_type_contract(user_def_class.__init__)
    # Remove self reference
    return attributes[1:]
