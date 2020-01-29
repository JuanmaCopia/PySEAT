from parse_module import parse_command_line_args, get_objects
from reports import report_statistics, helper_print_dict, print_formatted_result
from symbolic_execution_engine import SEEngine


args = parse_command_line_args()
target_data = get_objects(args)

if target_data["is_method"]:
    SEEngine.initialize(target_data)

    executions_stats = SEEngine.explore()
    for run_stats in executions_stats:
        print_formatted_result(
            target_data["function"], run_stats, target_data["verbose"]
        )

    report_statistics(SEEngine.statistics())
else:
    # TODO: Make it support functions (functions that not belong to a class)
    raise NotImplementedError
