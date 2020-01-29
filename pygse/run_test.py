from parse_module import parse_command_line_args, get_objects2
from reports import report_statistics, helper_print_dict, print_formatted_result
from symbolic_execution_engine import SEEngine


def symbolically_execute_method(module_name, class_name, method_name, max_depth=10):
    target_data = get_objects2(module_name, method_name, max_depth, True, class_name)
    SEEngine.initialize(target_data)
    executions_results = SEEngine.explore()
    for result in executions_results:
        # helper_print_dict(result)
        print_formatted_result(target_data["function"], result, target_data["verbose"])
    report_statistics(SEEngine.statistics())


symbolically_execute_method("pygse.tests.node_test", "Node", "swap_node", 10)
symbolically_execute_method("pygse.tests.node_test", "Node", "is_sorted", 10)
symbolically_execute_method("pygse.tests.test2", "C", "test_method", 4)
symbolically_execute_method("pygse.tests.linked_list_test", "LinkedList", "insert", 10)
symbolically_execute_method("pygse.tests.linked_list_test", "LinkedList", "size", 10)
symbolically_execute_method("pygse.tests.linked_list_test", "LinkedList", "search", 10)
symbolically_execute_method("pygse.tests.linked_list_test", "LinkedList", "delete", 10)
# symbolically_execute_method("pygse.tests.fail_tests", "LinkedList", "delete", 10)
    