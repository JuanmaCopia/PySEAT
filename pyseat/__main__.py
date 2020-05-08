"""PySEAT Command Line Interface

"""
import os
import sys
import subprocess
import time
from optparse import OptionParser

import sut_parser
from cli_print import welcome, print_formatted_result, report_statistics
from cli_print import print_method_data
from engine import SEEngine
from test_generator import TestCode, append_to_testfile, create_testfile
import data


def get_comma_separated_methods(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(","))


usage = (
    "usage: %prog <path to *.py file> <class-name> -m <method1> [,<method2>] [options]"
)
parser = OptionParser(usage=usage)
parser.add_option(
    "-m",
    "--methods",
    type="string",
    action="callback",
    callback=get_comma_separated_methods,
    dest="methods_names",
    help="Methods to explore and generate tests",
)
parser.add_option(
    "-d",
    "--max-depth",
    dest="max_depth",
    type="int",
    default=10,
    help="Maximum exploration tree depth",
)
parser.add_option(
    "-n",
    "--max-nodes",
    dest="max_nodes",
    type="int",
    default=5,
    help="Maximum amount of nodes per structure",
)
parser.add_option(
    "-r",
    dest="max_r_nodes",
    type="int",
    default=2,
    help="Max nodes that repok can add",
)
parser.add_option(
    "-b",
    "--build-timeout",
    dest="build_timeout",
    type="int",
    default=5,
    help="Max time to build a structure",
)
parser.add_option(
    "-t",
    "--method-timeout",
    dest="method_timeout",
    type="int",
    default=2,
    help="Max execution time for each exploration",
)
parser.add_option(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    default=False,
    help="Show statsistics of executions",
)
parser.add_option(
    "--no-comments",
    dest="no_comments",
    action="store_true",
    default=False,
    help="Generate comments on test with the structure representation",
)
parser.add_option(
    "--coverage",
    dest="coverage",
    action="store_true",
    default=False,
    help="Measure code coverage of generated test",
)
parser.add_option(
    "--mutation",
    dest="mutation",
    action="store_true",
    default=False,
    help="Measure mutation score",
)
parser.add_option(
    "-q",
    "--quiet",
    dest="quiet",
    action="store_true",
    default=False,
    help="Measure mutation score",
)
parser.add_option(
    "--no-test-run",
    dest="no_test_run",
    action="store_true",
    default=False,
    help="Run generated test after the exploration",
)

(options, args) = parser.parse_args()

if len(args) == 0:
    parser.error("No Arguments Supplied")
    sys.exit(1)
if not os.path.exists(args[0]):
    parser.error("File '{}' Not Found".format(args[0]))
    sys.exit(1)
if not options.methods_names:
    parser.error("Methods not given")
    sys.exit(1)

module_name = args[0]
class_name = args[1]
methods_names = options.methods_names

max_depth = options.max_depth
max_nodes = options.max_nodes
max_r_nodes = options.max_r_nodes
build_timeout = options.build_timeout
method_timeout = options.method_timeout
coverage = options.coverage
mutation = options.mutation
verbose = options.verbose
no_comments = options.no_comments
quiet = options.quiet
no_test_run = options.no_test_run

sut = sut_parser.parse(module_name, class_name, methods_names)
testfile, mod, folder, filepath = create_testfile(module_name, class_name)

welcome()

for method_data in sut.methods_map.values():
    sut.current_method = method_data
    engine = SEEngine(
        sut, max_depth, max_nodes, max_r_nodes, method_timeout, build_timeout
    )

    test_num = 0
    start_time = time.time()

    print_method_data(sut.current_method.name, class_name)

    for run in engine.explore():
        print_formatted_result(sut.get_method(), run, quiet)
        if run.status != data.PRUNED:
            test_num += 1
            test = TestCode(sut, run, test_num, method_timeout, no_comments)
            append_to_testfile(filepath, test.code + "\n\n")

    report_statistics(engine.statistics(), test_num, time.time() - start_time, verbose)

if not no_test_run:
    print("Running generated tests...")
    if not coverage and not mutation:
        subprocess.call(["pytest", "--disable-warnings", "-q", filepath])

    if coverage:
        subprocess.call(
            [
                "coverage",
                "run",
                "--source=" + folder,
                "--omit=" + filepath,
                "--branch",
                "-m",
                "pytest",
                "-q",
                "--disable-warnings",
                filepath,
            ]
        )
        print("\n\n {} BRANCH COVERAGE RESULTS {} \n".format("=" * 20, "=" * 20))
        subprocess.call(["coverage", "report"])
        subprocess.call(["coverage", "html", "-d", folder + "htmlcov"])

    if mutation:
        subprocess.call(
            [
                "mut.py",
                "--target",
                mod,
                "--unit-test",
                testfile,
                "--report-html",
                folder + "mutscore",
                "--runner",
                "pytest",
                "-c",
                "--coverage",
                "-p",
                folder,
                "-m",
            ]
        )
