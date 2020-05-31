"""PySEAT __main__.py

"""
import subprocess
import time
import os
import sut_parser
import cli_print as cli
from data import Statistics
from engine import SEEngine
from test_generator import TestCode, append_to_testfile, create_testfile
import arg_parsing


runs = arg_parsing.parse_command_line()

cli.print_welcome()

for args in runs:

    module_name = args["filepath"]
    class_name = args["class_name"]
    methods_names = args["methods"]

    quiet = args["quiet"]

    sut = sut_parser.parse(module_name, class_name, methods_names)
    testfile, mod, folder, filepath = create_testfile(module_name, class_name)
    path = os.path.abspath(os.path.join(filepath))

    engine = SEEngine(sut, args)

    start_time = time.time()

    cli.print_blue(" Generating instances of {}...".format(class_name))
    input_structures = engine.generate_structures()
    if not quiet:
        cli.print_white(" Done!")
    else:
        cli.print_white(" DONE!\n Exploring...")

    build_time = time.time() - start_time

    stats = Statistics(build_time)
    amount_tests = 0

    for method in methods_names:
        test_num = 0
        sut.current_method = sut.methods_map[method]
        if not quiet:
            cli.print_method_data(method)
        for i, conditions in input_structures:
            for run in engine.explore(method, i, conditions):
                amount_tests += 1
                stats.status_count(run)
                test_num += 1
                run.number = test_num
                if not quiet:
                    cli.print_result(run)
                test = TestCode(
                    sut, run, test_num, args["timeout"], args["test_comments"],
                )
                append_to_testfile(filepath, test.code + "\n\n")

    stats.total_time = time.time() - start_time
    cli.print_statistics(stats, amount_tests, path)

    if args["run_tests"]:
        coverage = args["coverage"]
        mutation = args["mutation"]

        cli.print_running_tests()
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
            cli.print_coverage_title()
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

    cli.print_bottom()
