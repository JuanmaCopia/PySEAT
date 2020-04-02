"""PyGSE Command Line Interface

"""

import argparse

from pygse.reports import report_statistics, print_formatted_result
from pygse.symbolic_execution_engine import SEEngine
from pygse.sut_parser import parse
from pygse.run_test import run_tests
from pygse.test_generator import TestCode
from pygse.stats import Status
from pygse.engine_errors import CouldNotBuildError

import pygse.proxy as proxy
import copy
import sys


# a = proxy.IntProxy()
# b = proxy.IntProxy()
# c = 5

# SEEngine.initialize(None, 10)

# if a == b:
#     pass
# if b == c:
#     pass

# path = SEEngine._path_condition
# print(SEEngine._path_condition)

# print("b es: ")
# print(str(b))
# print(SEEngine.concretize(b, proxy.smt.get_model(path)))

# print("copia de b es: ")
# print(str(copy.deepcopy(b)))
# print(SEEngine.concretize(copy.deepcopy(b), proxy.smt.get_model(path)))

# print("a es: ")
# print(str(a))
# print(SEEngine.concretize(a, proxy.smt.get_model(path)))

# print("copia de a es: ")
# print(str(copy.deepcopy(a)))
# print(SEEngine.concretize(copy.deepcopy(a), proxy.smt.get_model(path)))

# sys.exit()


def parse_command_line_args():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-t", "--test", action="store_true", help="run all tests")
    subparser = parser.add_subparsers(help="run")
    parser2 = subparser.add_parser("run", help="Symbolically execute a function")
    parser2.add_argument(
        "mod_class_func", action="store", help="Syntax: <module>:<class>:<function>"
    )
    parser2.add_argument(
        "-d", "--depth", action="store", type=int, default=10, help="Depth limit"
    )
    parser2.add_argument(
        "-v", "--verbose", action="store_true", help="Detailed execution"
    )
    return parser.parse_args()


def remove_instrumented(module_name):
    x = module_name.split(".")
    orig = x[2].split("_")
    return orig[0]


def create_testfile(filename, module_name, class_name):
    file = open(filename + ".py", "w")
    file.write(
        "from "
        + remove_instrumented(module_name)
        + " import Node, "
        + class_name
        + "\n\n\n"
    )
    file.close()


def append_line_testfile(filename, str):
    file = open(filename + ".py", "a")
    file.write(str + "\n")
    file.close()


def append_to_testfile(filename, str):
    file = open(filename + ".py", "a")
    file.write(str + "\n\n\n")
    file.close()


args = parse_command_line_args()

if args.test:
    run_tests()
else:
    mod_cls_func = args.mod_class_func.strip().split(":")
    module_name = mod_cls_func[0].strip()
    class_name = mod_cls_func[1].strip()
    function_name = mod_cls_func[2].strip()
    max_depth = args.depth

    sut = parse(module_name, function_name, class_name)

    runs = []
    test_number = 1
    foldername = "generated_tests/"
    filename = (
        foldername + remove_instrumented(module_name) + "_" + function_name + "_tests"
    )
    create_testfile(filename, module_name, class_name)

    SEEngine.initialize(sut, max_depth)

    tests_gen = []
    for run in SEEngine.explore():
        if run:
            print_formatted_result(sut.function, run, True)
            if run.status != Status.PRUNED:
                if run.builded_in_self:
                    test = TestCode(sut, run, run.number)
                    code = test.get_code()
                    append_to_testfile(filename, code)
                    tests_gen.append(run.number)
                    print("\n" + code + "\n")
        else:
            print("una corrida retorno None")

    report_statistics(SEEngine.statistics())

    print(tests_gen)

    append_line_testfile(filename, "if __name__ == '__main__':")
    for n in tests_gen:
        append_line_testfile(filename, "    " + function_name + "_test" + str(n) + "()")

