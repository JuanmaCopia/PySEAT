"""Report Module

Contains the methods to print a formatted console output of the statistics
of executions.

"""

import data
import helpers

INDENT4 = "    "
INDENT2 = "  "
INDENT8 = "        "


def print_formatted_result(function, run_data, verbose):
    if verbose:
        if run_data.status != data.Status.PRUNED:
            print("\n#" + str(run_data.number) + " " + run_data.status.name + ":\n")
            print(" Path Condition:")
            helpers.print_list(run_data.pathcondition, INDENT8)
            print(
                " Symbolic input self:\n"
                + INDENT8
                + run_data.symbolic_inself.__repr__()
            )
            print(" Input self:\n" + INDENT8 + run_data.input_self.__repr__())
            print(" Self end states:\n" + INDENT8 + run_data.self_end_state.__repr__())
            print("")
        else:
            print("\n#" + str(run_data.number) + " " + run_data.status.name + ":\n")
            print(" Pruned self:\n" + INDENT8 + run_data.pruned_structure.__repr__())
            if run_data.exception:
                print("  Exception: " + str(run_data.exception))
            print("")
    else:
        print("#" + str(run_data.number) + ": " + run_data.status.name)


def report_statistics(run_data):
    complete_exec = run_data.successes + run_data.failures
    pruned = run_data.get_amount_pruned()

    assert pruned + complete_exec == run_data.total_paths
    print("Exploration Statistiscs:")
    print(
        "\n  "
        + str(complete_exec)
        + " of "
        + str(run_data.total_paths)
        + " paths explored"
    )
    print(INDENT2 + str(run_data.successes) + " passed")
    print(INDENT2 + str(run_data.failures) + " failed")
    verbose = True
    if verbose:
        print(INDENT2 + str(pruned) + " pruned: ")
        print(INDENT4 + str(run_data.pruned_by_depth) + " by depth")
        print(INDENT4 + str(run_data.pruned_by_error) + " by error")
        print(INDENT4 + str(run_data.pruned_invalid) + " by invalid")
        print(INDENT4 + str(run_data.pruned_by_rec_limit) + " by rec limit")
        print(INDENT4 + str(run_data.pruned_by_repok) + " by repok")
        print(INDENT4 + str(run_data.pruned_by_exception) + " by exception\n")
    else:
        print(str(pruned) + " pruned")
