"""PySEAT __main__.py

"""
import subprocess
import time

import sut_parser
from cli_print import welcome, print_formatted_result, report_statistics
from cli_print import print_method_data
from engine import SEEngine
from test_generator import TestCode, append_to_testfile, create_testfile
import data
import arg_parsing


runs = arg_parsing.parse_command_line()

welcome()

for args in runs:

    module_name = args["filepath"]
    class_name = args["class_name"]
    methods_names = args["methods"]

    sut = sut_parser.parse(module_name, class_name, methods_names)
    testfile, mod, folder, filepath = create_testfile(module_name, class_name)

    for method_data in sut.methods_map.values():
        sut.current_method = method_data
        engine = SEEngine(sut, args)

        test_num = 0
        start_time = time.time()

        print_method_data(sut.current_method.name, class_name)

        for run in engine.explore():
            print_formatted_result(sut.get_method(), run, args["quiet"])
            if run.status != data.PRUNED:
                test_num += 1
                test = TestCode(
                    sut, run, test_num, args["method_timeout"], args["test_comments"],
                )
                append_to_testfile(filepath, test.code + "\n\n")

        report_statistics(
            engine.statistics(), test_num, time.time() - start_time, args["verbose"]
        )

    if args["run_tests"]:
        coverage = args["coverage"]
        mutation = args["mutation"]

        print("Running generated tests...")
        if not coverage and not mutation:
            subprocess.call(["pytest", "--disable-warnings", "-q", filepath])

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
                    "-q",
                    "--disable-warnings",
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
                    folder + "mutscore",
                    "--runner",
                    "pytest",
                    "-c",
                    "--coverage",
                    "-p",
                    folder,
                    "-m",
                ]
            )
