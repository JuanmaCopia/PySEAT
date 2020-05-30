"""PySEAT __main__.py

"""
import subprocess
import time

import sut_parser
import cli_print as cli
from engine import SEEngine
from test_generator import TestCode, append_to_testfile, create_testfile
import arg_parsing


runs = arg_parsing.parse_command_line()

cli.print_welcome()

for args in runs:

    module_name = args["filepath"]
    class_name = args["class_name"]
    methods_names = args["methods"]

    sut = sut_parser.parse(module_name, class_name, methods_names)
    testfile, mod, folder, filepath = create_testfile(module_name, class_name)

    engine = SEEngine(sut, args)

    cli.print_blue(" Generating {}...".format(class_name))
    input_structures = engine.generate_structures()
    cli.print_white(" Done!")

    for method in methods_names:
        test_num = 0
        sut.current_method = sut.methods_map[method]
        cli.print_method_data(method)
        for i, conditions in input_structures:
            for run in engine.explore(method, i, conditions):
                cli.print_result(run, args["quiet"])
                test_num += 1
                test = TestCode(
                    sut, run, test_num, args["method_timeout"], args["test_comments"],
                )
                append_to_testfile(filepath, test.code + "\n\n")

    # cli.print_statistics(engine.statistics(), test_num, 0, args["verbose"])

    # for method_data in sut.methods_map.values():
    #     sut.current_method = method_data
    #     engine = SEEngine(sut, args)

    #     test_num = 0
    #     start_time = time.time()

    #     cli.print_method_data(sut.current_method.name, class_name)

    #     for run in engine.explore():
    #         cli.print_result(sut.get_method(), run, args["quiet"])
    #         if run.status != data.PRUNED:
    #             test_num += 1
    #             test = TestCode(
    #                 sut, run, test_num, args["method_timeout"], args["test_comments"],
    #             )
    #             append_to_testfile(filepath, test.code + "\n\n")

    #     cli.print_statistics(
    #         engine.statistics(), test_num, time.time() - start_time, args["verbose"]
    #     )

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
