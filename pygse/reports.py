def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def report_statistics(stat):
    print("")
    print(str(stat["explored"]) + " of " + str(stat["total_paths"]) + " paths explored")
    print(str(stat["pruned_by_depth"]) + " pruned by depth")
    print(str(stat["pruned_by_repok"]) + " pruned by repok")
    print(str(stat["pruned_by_error"]) + " pruned by error")
    print("")
