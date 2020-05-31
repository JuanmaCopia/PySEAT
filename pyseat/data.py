"""Statistics Module.

Provides the structures to collect statistics from overall program
executions and for each execution in particular.

"""


OK = 0
PRUNED = 1
FAIL = 2
EXCEPTION = 3
TIMEOUT = 4


class Statistics:
    def __init__(self, build_time):
        self.build_time = build_time
        self.successes = 0
        self.failures = 0
        self.exceptions = 0
        self.timeouts = 0

    def status_count(self, run_data):
        if run_data.status == OK:
            self.successes += 1
        elif run_data.status == FAIL:
            self.failures += 1
        elif run_data.status == EXCEPTION:
            self.exceptions += 1
        elif run_data.status == TIMEOUT:
            self.timeouts += 1
