"""clu_print Module

Contains the methods to print a formatted console output.

"""

import data
from termcolor import colored


def print_result(run_data, quiet):
    exec_num = run_data.number
    if run_data.status == data.PRUNED:
        if not quiet:
            print_white("   #{} PRUNED".format(exec_num))
    elif run_data.status == data.OK:
        print_green("   #{} OK".format(exec_num))
    elif run_data.status == data.FAIL:
        print_red("   #{} FAIL".format(exec_num))
    elif run_data.status == data.EXCEPTION:
        print_magenta("   #{} EXCEPTION".format(exec_num))
    elif run_data.status == data.TIMEOUT:
        print_yellow("   #{} TIMEOUT".format(exec_num))


# def print_statistics(stats, test_num, duration, verbose=False):
#     completed = stats.amount_complete_exec()
#     pruned = stats.get_amount_pruned()
#     print("\n Done! {} Tests were generated".format(test_num))
#     print_white("\n Valid executions: {} of {}".format(completed, stats.total_paths))
#     print_green("   {} passed".format(stats.successes))
#     print_red("   {} failed".format(stats.failures))
#     print_magenta("   {} exceptions".format(stats.exceptions))
#     print_yellow("   {} timeouts".format(stats.timeouts))
#     print_white("   {} pruned".format(pruned))

#     if verbose:
#         print("\n   {} pruned:".format(pruned))
#         print("     {} by repok".format(stats.pruned_by_repok))
#         print("     {} by rec_limit".format(stats.pruned_by_rec_limit))
#         print("     {} by depth".format(stats.pruned_by_depth))
#         print("     {} by exception".format(stats.pruned_by_exception))
#         print("     {} by timeout".format(stats.pruned_by_timeout))
#         print("     {} impossible to build".format(stats.pruned_by_not_builded))
#         print(
#             "       {} of those by timeout during the build".format(
#                 stats.not_builded_by_timeout
#             )
#         )
#         for i, num in enumerate(stats.builded_at):
#             if num != 0:
#                 print("   {} builded by adding {} nodes".format(num, i))
#         print("     {} builded after exception".format(stats.builded_after_exception))
#         print("     {} builded after rec_limit".format(stats.builded_after_rec_limit))
#         print("     {} builded after timeout".format(stats.builded_after_timeout))
#         print("   Max valid execution time: {:.2f}".format(stats.max_ok_time))

#     print_cyan("\n{} {:.2f} seconds {}\n\n".format("-" * 30, duration, "-" * 30))


def print_welcome():
    print_cyan("\n\n {}  PySEAT  {}\n".format("=" * 32, "=" * 32))


def print_method_data(method_name, class_name):
    print_white(" Method: {}".format(method_name))
    print_white(" Class:  {}\n".format(class_name))
    print(" Performing Exploration...")


def print_running_tests():
    print_white("Running generated tests...")


def print_coverage_title():
    print("\n\n{} BRANCH COVERAGE RESULTS {} \n".format("=" * 20, "=" * 20))


def print_bottom():
    print_cyan("\n{}\n\n\n".format("=" * 75))


def print_white(msg):
    print(colored(msg, "white", attrs=["bold"]))


def print_cyan(msg):
    print(colored(msg, "cyan", attrs=["bold"]))


def print_green(msg):
    print(colored(msg, "green", attrs=["bold"]))


def print_red(msg):
    print(colored(msg, "red", attrs=["bold"]))


def print_magenta(msg):
    print(colored(msg, "magenta", attrs=["bold"],))


def print_yellow(msg):
    print(colored(msg, "yellow", attrs=["bold"],))
