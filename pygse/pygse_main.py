import argparse

from pygse.reports import report_statistics, print_formatted_result
from pygse.symbolic_execution_engine import SEEngine
from pygse.sut_parser import SUTParser


def parse_command_line_args():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("file", action="store", help="Syntax: <program_file>")
    parser.add_argument(
        "-c", "--class_name", action="store", help="Syntax: <class_name>"
    )
    parser.add_argument("function", action="store", help="Syntax: <function_name>")
    parser.add_argument(
        "-d", "--depth", action="store", type=int, default=10, help="Depth limit"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="an optional argument"
    )
    return parser.parse_args()


args = parse_command_line_args()

module_name = args.file.strip()
class_name = args.class_name.strip()
function_name = args.function.strip()
max_depth = args.depth

sut = SUTParser()
sut.parse(module_name, function_name, class_name)

if sut.is_method:
    SEEngine.initialize(sut, max_depth)

    for run in SEEngine.explore():
        print_formatted_result(sut.function, run, True)

    report_statistics(SEEngine.statistics())
else:
    # TODO: Make it support functions (functions that not belong to a class)
    raise NotImplementedError
