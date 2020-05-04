import os
import sys
import signal
from exceptions import TimeOutException


def raise_timeout(signum, frame):
    raise TimeOutException()


class MethodRun:
    def __init__(self, time):
        self.time = time

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        signal.signal(signal.SIGALRM, raise_timeout)
        signal.alarm(self.time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        sys.stdout.close()
        sys.stdout = self._original_stdout


def path_to_str(branch_points):
    strrepr = ""
    for x in branch_points:
        strrepr += str(x.get_branch())
    return strrepr


def keep_first_n(l, n):
    new_list = []
    i = 0
    while i < n:
        new_list.insert(i, l[i])
        i += 1
    return new_list


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


def helper_print_dict(dictionary):
    print("")
    for (k, v) in dictionary.items():
        print(k, "   ", v)
    print("")


def print_list(l: list, indent):
    for elem in l:
        print(indent + str(elem))
