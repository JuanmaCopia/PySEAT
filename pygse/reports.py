from symbolic_execution_engine import Status


INDENT = "        "
INDENT_LIST = "            "


def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def get_concrete_return(stats):
    if stats.concrete_return is not None:
        return stats.concrete_return.__repr__()
    else:
        if stats.exception:
            return "Exception: " + str(stats.exception)
        return "None"


def get_concrete_args_str(stats):
    result = stats.concrete_self.__repr__()
    if not stats.concrete_args:
        return result

    conc_args = ""
    if len(stats.concrete_args) == 1:
        conc_args = stats.concrete_args[0].__repr__()
    else:
        for x in stats.concrete_args:
            conc_args += str(x) + ","
        conc_args = conc_args[:-1]

    return result + ", " + conc_args


def get_function_profile_str(function, stats):
    return (
        function.__name__
        + "("
        + get_concrete_args_str(stats)
        + ")"
        + "  ->  "
        + get_concrete_return(stats)
    )


def get_header_str(stats):
    return "#" + str(stats.number) + " [" + stats.status.name + "]: "


def print_list(l: list):
    for elem in l:
        print(INDENT_LIST + str(elem))


def print_formatted_result(function, stats, verbose):
    verbose = True
    if stats.status != Status.PRUNED:
        print("\n" + get_header_str(stats) + get_function_profile_str(function, stats))
        if not stats.exception:
            print_list(stats.errors)

            if verbose:
                print(INDENT + "Path Condition:  ")
                print_list(stats.pathcondition)
                print(INDENT + "Symbolic return:  " + stats.returnv.__repr__())
                print(INDENT + "Symbolic self:    " + stats.self_structure.__repr__())


def report_statistics(stat):
    print("")
    print(str(stat["explored"]) + " of " + str(stat["total_paths"]) + " paths explored")
    print(str(stat["successes"]) + " passed")
    print(str(stat["failures"]) + " failures")
    print(str(stat["pruned_by_depth"]) + " pruned by depth")
    print(str(stat["pruned_by_repok"]) + " pruned by repok")
    print(str(stat["pruned_by_error"]) + " pruned by error")
    print("")
