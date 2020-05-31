import configparser
import os
import sys
import optparse


DEFAULT_CFG_PATH = "config.ini"


def parse_error(msg):
    print("\narg_parsing.py: {}".format(msg))
    sys.exit(1)


def method_list(method_str):
    return [m.strip() for m in method_str.split(",")]


def parse_config_file(cfg_path=None):
    if not cfg_path:
        folder = os.path.dirname(os.path.dirname(__file__))
        cfg_path = os.path.abspath(os.path.join(folder, DEFAULT_CFG_PATH))

    if not os.path.exists(cfg_path):
        parse_error("File '{}' Not Found".format(cfg_path))

    config = configparser.ConfigParser()
    config.read(cfg_path)
    runs = []
    sections = config.sections()
    if not sections:
        parse_error("No arguments provided in {}".format(cfg_path))
    for r in sections:
        args = {}
        args["filepath"] = config.get(r, "filepath")
        args["class_name"] = config.get(r, "class_name")
        args["methods"] = method_list(config.get(r, "methods"))
        args["max_nodes"] = config.getint(r, "max_nodes")
        args["max_depth"] = config.getint(r, "max_depth")
        args["timeout"] = config.getint(r, "timeout")
        args["coverage"] = config.getboolean(r, "coverage")
        args["mutation"] = config.getboolean(r, "mutation")
        args["quiet"] = config.getboolean(r, "quiet")
        args["run_tests"] = config.getboolean(r, "run_tests")
        args["test_comments"] = config.getboolean(r, "test_comments")
        runs.append(args)
    return runs


def parse_command_line():
    usage = """usage: %prog <path to .py file> <class-name> -m <method1> [,<method2>] [options]\n
        Or\n
        usage: %prog -c [<path to config file (.ini)>]
        """
    parser = optparse.OptionParser(usage=usage)
    parser.add_option(
        "-c",
        "--config",
        dest="config",
        action="store_true",
        default=False,
        help="Read arguments from configuration file",
    )
    parser.add_option(
        "-m",
        "--methods",
        type="string",
        dest="methods_names",
        help="Methods to explore and generate tests",
    )
    parser.add_option(
        "-d",
        "--max-depth",
        dest="max_depth",
        type="int",
        default=10,
        help="Maximum exploration tree depth",
    )
    parser.add_option(
        "-n",
        "--max-nodes",
        dest="max_nodes",
        type="int",
        default=5,
        help="Maximum amount of nodes per structure",
    )
    parser.add_option(
        "-t",
        "--timeout",
        dest="timeout",
        type="int",
        default=5,
        help="Max execution time for each exploration",
    )
    parser.add_option(
        "--no-comments",
        dest="no_comments",
        action="store_true",
        default=False,
        help="Generate comments on test with the structure representation",
    )
    parser.add_option(
        "--coverage",
        dest="coverage",
        action="store_true",
        default=False,
        help="Measure code coverage of generated test",
    )
    parser.add_option(
        "--mutation",
        dest="mutation",
        action="store_true",
        default=False,
        help="Measure mutation score",
    )
    parser.add_option(
        "-q",
        "--quiet",
        dest="quiet",
        action="store_true",
        default=False,
        help="Measure mutation score",
    )
    parser.add_option(
        "--no-test-run",
        dest="no_test_run",
        action="store_true",
        default=False,
        help="Run generated test after the exploration",
    )

    (options, args) = parser.parse_args()

    if not options.config:
        if len(args) == 0:
            parse_error("No Arguments Supplied")
        if not os.path.exists(args[0]):
            parse_error("File '{}' Not Found".format(args[0]))
        if not options.methods_names:
            parse_error("Methods not given")

        pargs = {}
        pargs["filepath"] = args[0]
        pargs["class_name"] = args[1]
        pargs["methods"] = method_list(options.methods_names)
        pargs["max_nodes"] = options.max_nodes
        pargs["max_depth"] = options.max_depth
        pargs["timeout"] = options.timeout
        pargs["coverage"] = options.coverage
        pargs["mutation"] = options.mutation
        pargs["quiet"] = options.quiet
        pargs["run_tests"] = not options.no_test_run
        pargs["test_comments"] = not options.no_comments
        return [pargs]

    if len(args) == 0:
        return parse_config_file()
    else:
        return parse_config_file(args[0])
