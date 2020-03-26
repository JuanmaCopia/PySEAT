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


def create_testfile(filename, module_name):
    file = open(filename + ".py", "w")
    file.write("from " + module_name + " import *\n\n\n")
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
    filename = foldername + function_name + "_tf"
    create_testfile(filename, module_name)

    SEEngine.initialize(sut, max_depth)
    # maybe initialize test generator
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
                    print("run " + str(run.number) + "Could not be builded")
        else:
            print("una corrida retorno None")

    report_statistics(SEEngine.statistics())
    print(tests_gen)

