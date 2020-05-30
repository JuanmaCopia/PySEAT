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
        self.pruned_by_timeout = 0

    def status_count(self, status, time):
        if status != PRUNED:
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
