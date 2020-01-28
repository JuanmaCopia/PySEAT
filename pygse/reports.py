def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def get_concrete_return(result):
    if result["conc_ret"] is not None:
        return result["conc_ret"].__repr__()
    else:
        if result["exception"]:
            return "Exception: " + str(result["exception"])
        return "None"


def get_function_profile(function, result):
    concrete_args = result["conc_args"]
    if concrete_args:
        conc_args = ""
        if len(concrete_args) == 1:
            conc_args = concrete_args[0].__repr__()
        else:
            for x in concrete_args:
                conc_args += str(x) + ","
            conc_args = conc_args[:-1]
        return (
            function.__name__
            + "("
            + result["conc_self"].__repr__()
            + ", "
            + conc_args
            + ")"
            + "  ->  "
            + get_concrete_return(result)
        )
    return (
        function.__name__
        + "("
        + result["conc_self"].__repr__()
        + ")"
        + "  ->  "
        + get_concrete_return(result)
    )


def print_formatted_result(function, result, verbose):
    verbose = True
    if result["status"] != "PRUNED":
        print("")
        print(
            "#"
            + str(result["execution_number"])
            + " ["
            + result["status"]
            + "]: "
            + get_function_profile(function, result)
        )
        if not result["exception"]:
            warns = result["warnings"]
            if warns:
                print("      > Warnings:")
                for w in warns:
                    print("          - " + w)

            if verbose:
                print("      > Path Condition:")
                for c in result["path_condition"]:
                    print("            " + str(c))
                print("      > Symbolic return: " + result["returnv"].__repr__())
                print(
                    "      > Symbolic self:\n           "
                    + str(result["self"].__repr__())
                )


def report_statistics(stat):
    print("")
    print(str(stat["explored"]) + " of " + str(stat["total_paths"]) + " paths explored")
    print(str(stat["pruned_by_depth"]) + " pruned by depth")
    print(str(stat["pruned_by_repok"]) + " pruned by repok")
    print(str(stat["pruned_by_error"]) + " pruned by error")
    print("")
