"""Statistics Module.

Provides the structures to collect statistics from overall program
executions and for each execution in particular.

"""


OK = 0
PRUNED = 1
FAIL = 2
EXCEPTION = 3
TIMEOUT = 4


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

    def status_count(self, status, time):
        if status != PRUNED:
            if time > self.max_ok_time:
                self.max_ok_time = time
            if status == OK:
                self.successes += 1
            elif status == FAIL:
                self.failures += 1
            elif status == EXCEPTION:
                self.exceptions += 1
            elif status == TIMEOUT:
                self.timeouts += 1

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
