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
import test_generator as testgen
import data


def get_comma_separated_methods(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(","))


usage = (
    "usage: %prog [options] <path to *.py file> <class-name> -m <method1> [,<method2>]"
)
parser = OptionParser(usage=usage)
parser.add_option(
    "-m",
    "--methods",
    type="string",
    action="callback",
    callback=get_comma_separated_methods,
    dest="methods_names",
)
parser.add_option(
    "-d", dest="max_depth", type="int", default=10, help="maximum exploration depth",
)
parser.add_option(
    "-n", dest="max_nodes", type="int", default=5, help="maximum amount structures",
)
parser.add_option(
    "-r",
    dest="max_r_nodes",
    type="int",
    default=2,
    help="max nodes that repok can add",
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
    help="show statsistics of executions",
)
parser.add_option(
    "--test-comments",
    dest="comments",
    action="store_true",
    default=True,
    help="show statsistics of executions",
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

(options, args) = parser.parse_args()

if len(args) == 0:
    parser.error("Not Arguments Supplied")
    sys.exit(1)
if not os.path.exists(args[0]):
    parser.error("File Not Found")
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
comments = options.comments

sut = sut_parser.parse(module_name, class_name, methods_names)
testfile, mod, folder, filepath = testgen.create_testfile(module_name, class_name)

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
        engine._stats.sum_times(run)
        print_formatted_result(sut.get_method(), run)
        if run.status != data.PRUNED:
            test_num += 1
            test = testgen.TestCode(sut, run, test_num, method_timeout, comments)
            testgen.append_to_testfile(filepath, test.code + "\n\n")

    report_statistics(engine.statistics(), test_num, time.time() - start_time, verbose)


print("Running generated tests...\n")

# subprocess.call([sys.executable, filepath])

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
            # "--disable-warnings",
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
            "mutscore",
            "--runner",
            "pytest",
            "-c",
            "--coverage",
            "-p",
            folder,
            "-m",
        ]
    )

if not coverage and not mutation:
    subprocess.call(["pytest", filepath])
