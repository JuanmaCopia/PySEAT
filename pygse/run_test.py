from pygse.reports import report_statistics, print_formatted_result
from pygse.symbolic_execution_engine import SEEngine
from pygse.sut_parser import parse


def symbolically_execute_method(module_name, class_name, function_name, max_depth=10):
    sut = parse(module_name, function_name, class_name)
    SEEngine.initialize(sut, max_depth)
    for result in SEEngine.explore():
        print_formatted_result(sut.function, result, True)
    report_statistics(SEEngine.statistics())


def run_tests():
    symbolically_execute_method("pygse.tests.node_test", "Node", "swap_node", 10)
    symbolically_execute_method("pygse.tests.node_test", "Node", "is_sorted", 10)
    symbolically_execute_method("pygse.tests.test2", "C", "test_method", 4)
    symbolically_execute_method(
        "pygse.tests.linked_list_test", "LinkedList", "insert", 10
    )
    symbolically_execute_method(
        "pygse.tests.linked_list_test", "LinkedList", "size", 10
    )
    symbolically_execute_method(
        "pygse.tests.linked_list_test", "LinkedList", "search", 10
    )
    symbolically_execute_method(
        "pygse.tests.linked_list_test", "LinkedList", "delete", 10
    )
    # symbolically_execute_method("pygse.tests.fail_tests", "LinkedList", "delete", 10)
    symbolically_execute_method(
        "pygse.tests.node_test", "Node", "swap_node_with_garbage", 10
    )

