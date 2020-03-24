"""Statistics Module.

Provides the structures to collect statistics from overall program
executions and for each execution in particular.

"""

from enum import Enum


class Status(Enum):
    OK = 0
    PRUNED = 1
    FAIL = 2


class ExecutionStats:
    def __init__(self, exec_number: int, status=None, exception=None):

        self.input_self = None
        self.concrete_input_self = None
        self.end_self = None
        self.concrete_end_self = None
        self.builded_in_self = None
        self.args = []
        self.concrete_args = []
        self.returnv = None
        self.concrete_return = None
        self.exception = exception
        self.model = None
        self.pathcondition = []
        self.errors = []
        self.number = exec_number
        self.status = status


class GlobalStats:
    def __init__(self):
        self.total_paths = 0
        self.pruned_by_depth = 0
        self.pruned_by_error = 0
        self.pruned_by_repok = 0
        self.successes = 0
        self.failures = 0
        self.complete_exec = 0

    def status_count(self, status):
        if status == Status.OK:
            self.successes += 1
        else:
            self.failures += 1
