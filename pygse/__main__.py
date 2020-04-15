"""PyGSE Command Line Interface

"""
import os
import sys
import subprocess
from optparse import OptionParser

import sut_parser
from reports import report_statistics, print_formatted_result
from engine import SEEngine
import test_generator as testgen
from data import Status


usage = "usage: %prog [options] <path to *.py file> <class-name> <method-name>"
parser = OptionParser(usage=usage)
parser.add_option(
    "-d", dest="max_depth", type="int", default=10, help="maximum exploration depth",
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

sut = sut_parser.parse(module_name, class_name, method_name)
filepath = testgen.create_testfile(module_name, class_name, method_name)

runs = []
test_number = 1
engine = SEEngine(sut, max_depth)
tests_gen = []
test_num = 0

print("\n ========================  PyGSE  =====================\n")
print("Method " + method_name + " of class " + class_name)

print("\nPerforming Exploration...\n")
for run in engine.explore():
    if run:
        print_formatted_result(sut.get_method(), run, verbose)
        if run.status != Status.PRUNED:
            test_num += 1
            test = testgen.TestCode(sut, run, test_num)
            tests_gen.append(test)
            testgen.append_to_testfile(filepath, test.code + "\n\n")

print("\nDONE! " + str(test_num) + " Tests were generated\n")
report_statistics(engine.statistics())

testgen.append_test_calls(filepath, tests_gen)

print("Running generated tests...\n")
subprocess.call(["coverage", "run", "--branch", filepath])
subprocess.call(["coverage", "html"])