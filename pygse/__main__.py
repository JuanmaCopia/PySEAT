"""PyGSE Command Line Interface

"""

import argparse

from pygse.reports import report_statistics, print_formatted_result
from pygse.symbolic_execution_engine import SEEngine
from pygse.sut_parser import parse
from pygse.run_test import run_tests
from pygse.test_generator import TestCode
from pygse.stats import Status


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

    if sut.is_method:
        SEEngine.initialize(sut, max_depth)
        # maybe initialize test generator
        test_number = 1
        for run in SEEngine.explore():
            print_formatted_result(sut.function, run, True)
            # GenerateTest(run)
            if run.status != Status.PRUNED:
                test = TestCode(sut, run, test_number)
                test_number += 1
                print("\n" + test.get_code() + "\n")

        report_statistics(SEEngine.statistics())
    else:
        # TODO: Make it support functions (functions that not belong to a class)
        raise NotImplementedError
