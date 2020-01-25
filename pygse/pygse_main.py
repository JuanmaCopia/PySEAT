
from parse_module import parse_command_line_args, get_objects
from reports import report_statistics, helper_print_dict
from symbolic_execution_engine import SEEngine


args = parse_command_line_args()
r = get_objects(args)

if r["is_method"]:
    SEEngine.initialize(r["function"], r["function_args"], r["max_depth"], r["class_to_params"], r["primitives"], r["class"])

executions_results = SEEngine.exploration()
for result in executions_results:
    helper_print_dict(result)

report_statistics(SEEngine.statistics())
