import subprocess
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "-f":
        subprocess.call(
            [sys.executable, "pyseat/__main__.py", "-c", "tests/fail_tests_cfg.ini"]
        )
    else:
        print("usage1: run_tests.py")
        print("usage2: run_tests.py -f (Run test of structures that contains bugs)")
        sys.exit(-1)
else:
    subprocess.call([sys.executable, "pyseat/__main__.py", "-c", "tests/tests_cfg.ini"])
