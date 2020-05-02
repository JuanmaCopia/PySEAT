"""PyGSE Command Line Interface

"""
import os
import sys
import subprocess
import time
from optparse import OptionParser

import sut_parser
from reports import report_statistics, print_formatted_result
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
    "-t",
    dest="timeout",
    type="float",
    default=5,
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
    "--cov",
    dest="coverage",
    action="store_true",
    default=False,
    help="Measure code coverage of generated test",
)
parser.add_option(
    "--mut",
    dest="mutation",
    action="store_true",
    default=False,
    help="Measure mutation score",
)
parser.add_option(
    "--complete",
    dest="complete",
    action="store_true",
    default=False,
    help="Measure branch coverage and mutation score",
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
timeout = options.timeout
coverage = options.coverage
mutation = options.mutation
complete = options.complete
verbose = options.verbose

sut = sut_parser.parse(module_name, class_name, methods_names)
folder_name, filepath = testgen.create_testfile(module_name, class_name)

print("\n\n {}  PySEAT  {}\n".format("=" * 34, "=" * 34))
print("Python Symbolic Execution and Automatic Tester")

for method_data in sut.methods_map.values():
    sut.current_method = method_data
    engine = SEEngine(sut, max_depth, max_nodes, max_r_nodes, timeout)

    test_num = 0
    start_time = time.time()

    print("Performing Exploration...")
    print("Method: ", sut.current_method.name)
    print("Class: {}\n".format(class_name))

    for run in engine.explore():
        if run.status != data.PRUNED:
            print_formatted_result(sut.get_method(), run, verbose)
            test_num += 1
            test = testgen.TestCode(sut, run, test_num)
            testgen.append_to_testfile(filepath, test.code + "\n\n")

    print("\nDONE! " + str(test_num) + " Tests were generated")
    print("Elapsed Time:   ---  %s seconds  ---" % (time.time() - start_time))
    report_statistics(engine.statistics())
    print("{}\n\n".format("- " * 39))

print("Running generated tests...\n")

# subprocess.call([sys.executable, filepath])
coverage = True
if coverage:
    subprocess.call(
        [
            "coverage",
            "run",
            "--source=" + folder_name,
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
    subprocess.call(["coverage", "html", "-d", folder_name + "htmlcov"])
else:
    subprocess.call(["pytest", filepath])
