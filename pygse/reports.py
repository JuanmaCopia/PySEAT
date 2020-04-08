"""Report Module

Contains the methods to print a formatted console output of the statistics
of executions.

"""

from stats import Status


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
    result = stats.concrete_input_self.__repr__()
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
        + "   -->   "
        + get_concrete_return(stats)
    )


def get_header_str(stats):
    return "#" + str(stats.number) + " [" + stats.status.name + "]: "


def print_list(l: list):
    for elem in l:
        print(INDENT_LIST + str(elem))


def print_formatted_result(function, stats, verbose):
    verbose = False
    if verbose:
        if stats.status != Status.PRUNED:
            print(get_header_str(stats))
            print(" Path Condition:\n")
            print_list(stats.pathcondition)
            print(" In self:\n        " + stats.input_self.__repr__())
            print(" Builded input:\n        " + stats.builded_in_self.__repr__())
            print(" Conc end self:\n        " + stats.concrete_end_self.__repr__())
        else:
            print(get_header_str(stats))
            print(" Pruned self:\n\n" + stats.pruned_structure.__repr__())
            if stats.exception:
                print("  Exception: " + str(stats.exception))
    else:
        print("#" + str(stats.number) + ": " + stats.status.name)


def report_statistics(stats):
    complete_exec = stats.successes + stats.failures
    pruned = stats.get_amount_pruned()

    assert pruned + complete_exec == stats.total_paths
    print(
        "\n" + str(complete_exec) + " of " + str(stats.total_paths) + " paths explored"
    )
    print(str(stats.successes) + " passed")
    print(str(stats.failures) + " failed")
    verbose = True
    if verbose:
        print(str(pruned) + " pruned: ")
        print("  " + str(stats.pruned_by_depth) + " by depth")
        print("  " + str(stats.pruned_by_error) + " by error")
        print("  " + str(stats.pruned_invalid) + " by invalid")
        print("  " + str(stats.pruned_by_rec_limit) + " by rec limit")
        print("  " + str(stats.pruned_by_repok) + " by repok" + "\n")
    else:
        print(str(pruned) + " pruned")
