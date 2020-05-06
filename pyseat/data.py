"""Statistics Module.

Provides the structures to collect statistics from overall program
executions and for each execution in particular.

"""


OK = 0
PRUNED = 1
FAIL = 2
EXCEPTION = 3
TIMEOUT = 4


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
        self.successes = 0
        self.failures = 0
        self.exceptions = 0
        self.timeouts = 0
        self.pruned_by_depth = 0
        self.pruned_by_not_builded = 0
        self.pruned_by_repok = 0
        self.pruned_by_rec_limit = 0
        self.pruned_by_exception = 0
        self.pruned_by_timeout = 0

        self.not_builded_by_timeout = 0
        self.builded_at = [0, 0, 0, 0, 0, 0]
        self.builded_after_exception = 0
        self.builded_after_rec_limit = 0
        self.builded_after_timeout = 0

        self.max_ok_time = 0

    def status_count(self, status):
        if status == OK:
            self.successes += 1
        elif status == FAIL:
            self.failures += 1
        elif status == EXCEPTION:
            self.exceptions += 1
        elif status == TIMEOUT:
            self.timeouts += 1

    def sum_times(self, run):
        if run.status != PRUNED:
            if run.time > self.max_ok_time:
                self.max_ok_time = run.time

    def amount_complete_exec(self):
        total = self.successes + self.failures
        total += self.exceptions
        total += self.timeouts
        return total

    def get_amount_pruned(self):
        total = self.pruned_by_depth
        total += self.pruned_by_repok
        total += self.pruned_by_rec_limit
        total += self.pruned_by_timeout
        total += self.pruned_by_exception
        total += self.pruned_by_not_builded
        return total
