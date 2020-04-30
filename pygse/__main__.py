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

usage = "usage: %prog [options] <path to *.py file> <class-name> <method-name>"
parser = OptionParser(usage=usage)
parser.add_option(
    "-d", dest="max_depth", type="int", default=10, help="maximum exploration depth",
)
parser.add_option(
    "-n", dest="max_nodes", type="int", default=5, help="maximum amount structures",
)
parser.add_option(
    "-c",
    "--coverage",
    dest="coverage",
    action="store_true",
    default=False,
    help="Measure code coverage of generated test",
)
parser.add_option(
    "-r",
    dest="max_r_nodes",
    type="int",
    default=2,
    help="max nodes that repok can add",
)
parser.add_option(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    default=False,
    help="show results of each execution",
)
(options, args) = parser.parse_args()

if len(args) == 0 or not os.path.exists(args[0]):
    parser.error("File Not Found")
    sys.exit(1)

module_name = args[0]
class_name = args[1]
method_name = args[2]
max_depth = options.max_depth
verbose = options.verbose
max_nodes = options.max_nodes
max_r_nodes = options.max_r_nodes
coverage = options.coverage

sut = sut_parser.parse(module_name, class_name, method_name)
folder_name, filepath = testgen.create_testfile(module_name, class_name, method_name)

runs = []
test_number = 1
engine = SEEngine(sut, max_depth, max_nodes, max_r_nodes)
test_num = 0

print("\n ========================  PyGSE  =====================\n")
print("Method " + method_name + " of class " + class_name)

start_time = time.time()

print("\nPerforming Exploration...\n")
for run in engine.explore():
    if run.status != data.PRUNED:
        print_formatted_result(sut.get_method(), run, verbose)
        test_num += 1
        test = testgen.TestCode(sut, run, test_num)
        testgen.append_to_testfile(filepath, test.code + "\n\n")

print("\nDONE! " + str(test_num) + " Tests were generated\n")
print("Elapsed Time:   ---  %s seconds  ---" % (time.time() - start_time))
report_statistics(engine.statistics())

print("Running generated tests...\n")
# subprocess.call([sys.executable, filepath])
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
    subprocess.call(["coverage", "html"])
else:
    subprocess.call(["pytest", filepath])
