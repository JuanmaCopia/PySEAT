def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def print_formatted_result(function, result, verbose):
    print("")
    concrete_args = result["conc_args"]
    if concrete_args:
        func = function.__name__ + "(" + result["conc_args"].__repr__() + ")"
    else:
        func = function.__name__ + "(self)"
    print(
        "#"
        + str(result["execution_number"])
        + ": "
        + func
        + "  ->  "
        + result["conc_ret"].__repr__()
    )

    print("      > self end state:\n           " + result["conc_self"].__repr__())
    warns = result["warnings"]
    if warns:
        print("      > Warnings:")
        for w in warns:
            print("          - " + w)
    verbose = True
    if verbose:
        print("      > Path Condition:")
        for c in result["path_condition"]:
            print("            " + str(c))
        print("      > Return: " + result["returnv"].__repr__())
        print("      > Self  : " + result["self"].__repr__())


def report_statistics(stat):
    print("")
    print(str(stat["explored"]) + " of " + str(stat["total_paths"]) + " paths explored")
    print(str(stat["pruned_by_depth"]) + " pruned by depth")
    print(str(stat["pruned_by_repok"]) + " pruned by repok")
    print(str(stat["pruned_by_error"]) + " pruned by error")
    print("")
