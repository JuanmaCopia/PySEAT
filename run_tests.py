import subprocess
import sys

subprocess.call([sys.executable, "pyseat/__main__.py", "-c", "PySEAT/tests_cfg.ini"])
