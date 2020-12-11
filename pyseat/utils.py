import subprocess
import cli_print as cli


def measure_branch_coverage(folder, filepath):
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


def measure_mutation_score(mod, testfile, folder):
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