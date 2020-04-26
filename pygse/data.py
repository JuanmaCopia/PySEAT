"""Statistics Module.

Provides the structures to collect statistics from overall program
executions and for each execution in particular.

"""

from enum import Enum


class Status(Enum):
    OK = 0
    PRUNED = 1
    FAIL = 2


class Mode(Enum):
    CONSERVATIVE_EXECUTION = 0
    METHOD_EXPLORATION = 1
    REPOK_EXPLORATION = 2
    NOMODE = 3
    CONCRETE_EXECUTION = 4


class PathExecutionData:
    def __init__(self, exec_number: int, status=None, exception=None, pruned_s=None):
        self.symbolic_inself = None
        self.self_end_state = None
        self.input_self = None
        self.input_args = []
        self.returnv = None
        self.exception = exception
        self.model = None
        self.pathcondition = []
        self.errors = []
        self.number = exec_number
        self.status = status
        self.pruned_structure = pruned_s
        self.path_repr = ""
        self.time = 0


class ExplorationStats:
    def __init__(self):
        self.total_paths = 0
        self.pruned_by_depth = 0
        self.pruned_by_error = 0
        self.pruned_by_repok = 0
        self.pruned_by_rec_limit = 0
        self.pruned_by_exception = 0
        self.pruned_by_timeout = 0
        self.successes = 0
        self.failures = 0
        self.complete_exec = 0
        self.not_builded = 0
        self.builded_at0 = 0
        self.builded_at1 = 0
        self.builded_at2 = 0
        self.paths_repr = []
        self.max_ok_time = 0
        self.max_pruned_time = 0

    def status_count(self, status):
        if status == Status.OK:
            self.successes += 1
        elif status == Status.FAIL:
            self.failures += 1

    def sum_times(self, run):
        if run.status != Status.PRUNED:
            if run.time > self.max_ok_time:
                self.max_ok_time = run.time
        else:
            if run.time > self.max_pruned_time:
                self.max_pruned_time = run.time

    def get_amount_pruned(self):
        total = self.pruned_by_depth + self.pruned_by_error
        total += self.pruned_by_repok
        total += self.pruned_by_rec_limit
        total += self.pruned_by_timeout
        total += self.pruned_by_exception
        return total
