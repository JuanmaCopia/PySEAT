"""clu_print Module

Contains the methods to print a formatted console output.

"""

import data
from termcolor import colored


def print_result(function, run_data, quiet):
    exec_num = run_data.number
    if run_data.status == data.PRUNED:
        if not quiet:
            print(colored("   #{} PRUNED".format(exec_num), "white", attrs=["bold"]))
    elif run_data.status == data.OK:
        print(colored("   #{} OK".format(exec_num), "green", attrs=["bold"]))
    elif run_data.status == data.FAIL:
        print(colored("   #{} FAIL".format(exec_num), "red", attrs=["bold"]))
    elif run_data.status == data.EXCEPTION:
        print(colored("   #{} EXCEPTION".format(exec_num), "magenta", attrs=["bold"]))
    elif run_data.status == data.TIMEOUT:
        print(colored("   #{} TIMEOUT".format(exec_num), "yellow", attrs=["bold"]))


def print_statistics(stats, test_num, duration, verbose=False):
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
        print("\n   {} pruned:".format(pruned))
        print("     {} by repok".format(stats.pruned_by_repok))
        print("     {} by rec_limit".format(stats.pruned_by_rec_limit))
        print("     {} by depth".format(stats.pruned_by_depth))
        print("     {} by exception".format(stats.pruned_by_exception))
        print("     {} by timeout".format(stats.pruned_by_timeout))
        print("     {} impossible to build".format(stats.pruned_by_not_builded))
        print(
            "       {} of those by timeout during the build".format(
                stats.not_builded_by_timeout
            )
        )
        for i, num in enumerate(stats.builded_at):
            if num != 0:
                print("   {} builded by adding {} nodes".format(num, i))
        print("     {} builded after exception".format(stats.builded_after_exception))
        print("     {} builded after rec_limit".format(stats.builded_after_rec_limit))
        print("     {} builded after timeout".format(stats.builded_after_timeout))
        print("   Max valid execution time: {:.2f}".format(stats.max_ok_time))

    print(
        colored(
            "\n{} {:.2f} seconds {}\n\n".format("-" * 30, duration, "-" * 30),
            "cyan",
            attrs=["bold"],
        )
    )


def print_welcome():
    print(
        colored(
            "\n\n {}  PySEAT  {}\n".format("=" * 32, "=" * 32), "cyan", attrs=["bold"]
        )
    )


def print_method_data(method_name, class_name):
    print(colored(" Method: {}".format(method_name), "white", attrs=["bold"]))
    print(colored(" Class:  {}\n".format(class_name), "white", attrs=["bold"]))
    print(" Performing Exploration...")


def print_running_tests():
    print_white("Running generated tests...")


def print_coverage_title():
    print("\n\n{} BRANCH COVERAGE RESULTS {} \n".format("=" * 20, "=" * 20))


def print_bottom():
    print(colored("\n{}\n\n\n".format("=" * 75), "cyan", attrs=["bold"],))


def print_white(msg):
    print(colored(msg, "white", attrs=["bold"],))
