"""PyGSE Command Line Interface

"""
import os
import sys
from optparse import OptionParser
import sut_parser
from reports import report_statistics, print_formatted_result
from engine import SEEngine
import test_generator as testgen
from stats import Status


usage = "usage: %prog [options] <path to a *.py file>"
parser = OptionParser(usage=usage)
parser.add_option(
    "-m", "--max-depth", dest="max_depth", type="int", default=10,
)

(options, args) = parser.parse_args()

if len(args) == 0 or not os.path.exists(args[0]):
    parser.error("Missing app to execute")
    sys.exit(1)


module_name = args[0]
class_name = args[1]
method_name = args[2]
max_depth = options.max_depth


sut = sut_parser.parse(module_name, class_name, method_name)
filepath = testgen.create_testfile(module_name, class_name, method_name)

runs = []
test_number = 1
engine = SEEngine(sut, max_depth)
tests_gen = []
test_num = 0
print("Running tests...\n")
for run in engine.explore():
    if run:
        print_formatted_result(sut.function, run, True)
        if run.status != Status.PRUNED:
            test_num += 1
            test = testgen.TestCode(sut, run, test_num)
            tests_gen.append(test)
            testgen.append_to_testfile(filepath, test.code + "\n\n")

print("DONE! " + str(test_num) + " Tests were generated")
report_statistics(engine.statistics())

testgen.append_test_calls(filepath, tests_gen)

