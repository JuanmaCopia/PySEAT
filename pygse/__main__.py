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
from data import Status


def sum_times(run, eng):
    if run.status == Status.OK:
        if run.time > eng.max_ok_time:
            eng.max_ok_time = run.time
    else:
        if run.time > eng.max_pruned_time:
            eng.max_pruned_time = run.time


usage = "usage: %prog [options] <path to *.py file> <class-name> <method-name>"
parser = OptionParser(usage=usage)
parser.add_option(
    "-d", dest="max_depth", type="int", default=10, help="maximum exploration depth",
)
parser.add_option(
    "-n", dest="max_nodes", type="int", default=5, help="maximum amount structures",
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

sut = sut_parser.parse(module_name, class_name, method_name)
filepath = testgen.create_testfile(module_name, class_name, method_name)

runs = []
test_number = 1
engine = SEEngine(sut, max_depth, max_nodes)
tests_gen = []
test_num = 0

print("\n ========================  PyGSE  =====================\n")
print("Method " + method_name + " of class " + class_name)

start_time = time.time()

print("\nPerforming Exploration...\n")
for run in engine.explore():
    if run:
        sum_times(run, engine)
        print_formatted_result(sut.get_method(), run, verbose)
        if run.status != Status.PRUNED:
            test_num += 1
            test = testgen.TestCode(sut, run, test_num)
            tests_gen.append(test)
            testgen.append_to_testfile(filepath, test.code + "\n\n")

print("\nDONE! " + str(test_num) + " Tests were generated\n")
print("Elapsed Time:   ---  %s seconds  ---" % (time.time() - start_time))
report_statistics(engine.statistics())

testgen.append_test_calls(filepath, tests_gen)

print("\n Max OK time: ", engine.max_ok_time)
print("Max PRUNED time: ", engine.max_pruned_time)


print("Running generated tests...\n")
# subprocess.call([sys.executable, filepath])
subprocess.call(["coverage", "run", "--branch", filepath])
subprocess.call(["coverage", "html"])
