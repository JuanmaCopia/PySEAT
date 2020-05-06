"""Report Module

Contains the methods to print a formatted console output of the statistics
of executions.

"""

import data
import helpers
from termcolor import colored


INDENT4 = "    "
INDENT2 = "  "
INDENT8 = "        "


def print_formatted_result(function, run_data, debug=False):
    if debug:
        if run_data.status != data.PRUNED:
            print(
                "\n#" + str(run_data.number) + " " + status_str(run_data.status) + ":\n"
            )
            print(" Path Condition:")
            helpers.print_list(run_data.pathcondition, INDENT8)
            print(
                " \nSymbolic input self:\n"
                + INDENT8
                + run_data.symbolic_inself.__repr__()
            )
            print(" Input self:\n" + INDENT8 + run_data.input_self.__repr__())
            print(" Self end states:\n" + INDENT8 + run_data.self_end_state.__repr__())
            print("")
        else:
            print("\n#" + str(run_data.number) + " " + run_data.status.name + ":\n")
            print(" Path Condition:")
            helpers.print_list(run_data.pathcondition, INDENT8)
            print(
                " \nSymbolic input self:\n"
                + INDENT8
                + run_data.symbolic_inself.__repr__()
            )
            print(" Pruned self:\n" + INDENT8 + run_data.pruned_structure.__repr__())
            if run_data.exception:
                print("  Exception: " + str(run_data.exception))
            print("")
    else:
        exec_num = run_data.number
        if run_data.status == data.PRUNED:
            print(colored("   #{} PRUNED".format(exec_num), "white", attrs=["bold"]))
        elif run_data.status == data.OK:
            print(colored("   #{} OK".format(exec_num), "green", attrs=["bold"]))
        elif run_data.status == data.FAIL:
            print(colored("   #{} FAIL".format(exec_num), "red", attrs=["bold"]))
        elif run_data.status == data.EXCEPTION:
            print(
                colored("   #{} EXCEPTION".format(exec_num), "magenta", attrs=["bold"])
            )
        elif run_data.status == data.TIMEOUT:
            print(colored("   #{} TIMEOUT".format(exec_num), "yellow", attrs=["bold"]))


def status_str(status_num):
    if status_num == data.OK:
        return "OK"
    elif status_num == data.PRUNED:
        return "PRUNED"
    elif status_num == data.EXCEPTION:
        return "EXCEPTION"
    elif status_num == data.TIMEOUT:
        return "TIMEOUT"
    return "FAIL"


def report_statistics(stats, test_num, duration, verbose=False):
    completed = stats.amount_complete_exec()
    pruned = stats.get_amount_pruned()
    print("\n Done! {} Tests were generated".format(test_num))
    print(
        colored(
            "\n Valid executions: {} of {}".format(completed, stats.total_paths),
            "white",
            attrs=["bold"],
        )
    )
    print(colored("   {} passed".format(stats.successes), "green", attrs=["bold"]))
    print(colored("   {} failed".format(stats.failures), "red", attrs=["bold"]))
    print(
        colored("   {} exceptions".format(stats.exceptions), "magenta", attrs=["bold"])
    )
    print(colored("   {} timeouts".format(stats.timeouts), "yellow", attrs=["bold"]))
    print(colored("   {} pruned".format(pruned), "white", attrs=["bold"]))

    if verbose:
        print("\n   {} were imposible to build".format(stats.not_builded))
        print("     {} by timeout".format(stats.not_builded_by_timeout))
        for i, num in enumerate(stats.builded_at):
            if num != 0:
                print("   {} builded by adding {} nodes".format(num, i))
        print("     {} builded after exception".format(stats.builded_after_exception))
        print("     {} builded after rec_limit".format(stats.builded_after_rec_limit))
        print("     {} builded after timeout".format(stats.builded_after_timeout))
        print("   {} pruned:".format(pruned))
        print("     {} by repok".format(stats.pruned_by_repok))
        print("     {} by unsat path".format(stats.pruned_by_unsat))
        print("     {} by rec_limit".format(stats.pruned_by_rec_limit))
        print("     {} by depth".format(stats.pruned_by_depth))
        print("     {} by exception".format(stats.pruned_by_exception))
        print("     {} by timeout".format(stats.pruned_by_timeout))
        print("   Max valid execution time: {:.2f}".format(stats.max_ok_time))

    print(
        colored(
            "\n {} {:.2f} seconds {}\n\n".format("-" * 30, duration, "-" * 30),
            "cyan",
            attrs=["bold"],
        )
    )


def welcome():
    print(
        colored(
            "\n\n {}  PySEAT  {}\n".format("=" * 34, "=" * 34), "cyan", attrs=["bold"]
        )
    )


def print_method_data(method_name, class_name):
    print(colored(" Method: {}".format(method_name), "white", attrs=["bold"]))
    print(colored(" Class:  {}\n".format(class_name), "white", attrs=["bold"]))
    print(" Performing Exploration...")
