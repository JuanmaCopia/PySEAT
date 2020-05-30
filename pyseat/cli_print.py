"""clu_print Module

Contains the methods to print a formatted console output.

"""

import data
from termcolor import colored


def print_result(run_data):
    exec_num = run_data.number
    if run_data.status == data.OK:
        print_green("   #{} OK".format(exec_num))
    elif run_data.status == data.FAIL:
        print_red("   #{} FAIL".format(exec_num))
    elif run_data.status == data.EXCEPTION:
        print_magenta("   #{} EXCEPTION".format(exec_num))
    elif run_data.status == data.TIMEOUT:
        print_yellow("   #{} TIMEOUT".format(exec_num))


def print_statistics(stats, test_num, filepath):
    print_cyan("\n{} {} Tests generated {}\n".format("-" * 23, test_num, "-" * 23))
    print_green(" {} passed".format(stats.successes))
    print_red(" {} failed".format(stats.failures))
    print_magenta(" {} exceptions".format(stats.exceptions))
    print_yellow(" {} timeouts".format(stats.timeouts))
    print_blue("\n Build time: {:.2f}s".format(stats.build_time))
    print_white("\n File: {}".format(filepath))
    print_cyan("\n{} {:.2f}s {}\n".format("-" * 30, stats.total_time, "-" * 30))


def print_welcome():
    print_cyan("\n\n {}  PySEAT  {}\n".format("=" * 32, "=" * 32))


def print_method_data(method_name):
    print_white("\n Performing Exploration of {}... \n".format(method_name))


def print_running_tests():
    print_white("\nRunning generated tests...")


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
    print(colored(msg, "magenta", attrs=["bold"]))


def print_yellow(msg):
    print(colored(msg, "yellow", attrs=["bold"]))


def print_blue(msg):
    print(colored(msg, "blue", attrs=["bold"]))
