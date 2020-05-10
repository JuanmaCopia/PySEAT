import configparser
import os
import sys
import optparse

DEFAULT_CFG_PATH = "PySEAT/config.ini"


def parse_error(msg):
    print("\narg_parsing.py: {}".format(msg))
    sys.exit(1)

def method_list(method_str):
    return [m.strip() for m in method_str.split(",")]


def parse_config_file(cfg_file_path=DEFAULT_CFG_PATH):
    cfg_dir = os.path.dirname(cfg_file_path)
    sys.path = [os.path.abspath(os.path.join(cfg_dir))] + sys.path
    cfg_basename = os.path.basename(cfg_file_path)

    if not os.path.exists(cfg_basename):
        parse_error("File '{}' Not Found".format(cfg_basename))

    config = configparser.ConfigParser()
    config.read(cfg_basename)
    runs = []
    sections = config.sections()
    if not sections:
        parse_error("No arguments provided in {}".format(cfg_file_path))
    for r in sections:
        args = {}
        args["filepath"] = config.get(r, "filepath")
        args["class_name"] = config.get(r, "class_name")
        args["methods"] = method_list(config.get(r, "methods"))
        args["max_nodes"] = config.getint(r, "max_nodes")
        args["max_repok_nodes"] = config.getint(r, "max_repok_nodes")
        args["max_depth"] = config.getint(r, "max_depth")
        args["max_get"] = config.getint(r, "max_get")
        args["method_timeout"] = config.getint(r, "method_timeout")
        args["build_timeout"] = config.getint(r, "build_timeout")
        args["coverage"] = config.getboolean(r, "coverage")
        args["mutation"] = config.getboolean(r, "mutation")
        args["verbose"] = config.getboolean(r, "verbose")
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
        "-r",
        dest="max_repok_nodes",
        type="int",
        default=2,
        help="Max nodes that repok can add",
    )
    parser.add_option(
        "-g",
        dest="max_get",
        type="int",
        default=30,
        help="Max amount of gets whitout initializations",
    )
    parser.add_option(
        "-b",
        "--build-timeout",
        dest="build_timeout",
        type="int",
        default=5,
        help="Max time to build a structure",
    )
    parser.add_option(
        "-t",
        "--method-timeout",
        dest="method_timeout",
        type="int",
        default=2,
        help="Max execution time for each exploration",
    )
    parser.add_option(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show statsistics of executions",
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
        pargs["max_repok_nodes"] = options.max_repok_nodes
        pargs["max_depth"] = options.max_depth
        pargs["max_get"] = options.max_get
        pargs["method_timeout"] = options.method_timeout
        pargs["build_timeout"] = options.build_timeout
        pargs["coverage"] = options.coverage
        pargs["mutation"] = options.mutation
        pargs["verbose"] = options.verbose
        pargs["quiet"] = options.quiet
        pargs["run_tests"] = not options.no_test_run
        pargs["test_comments"] = not options.no_comments
        return [pargs]

    if len(args) == 0:
        return parse_config_file()
    else:
        return parse_config_file(args[0])
