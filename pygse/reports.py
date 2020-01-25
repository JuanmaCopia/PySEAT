def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k,"   ",v)
    print("")

def report_statistics(stat):
    print("")
    print(str(stat["explored"]) + " of " + str(stat["total_paths"]) + " paths explored")
    print(str(stat["pruned_paths"]) + " pruned")
    print("")