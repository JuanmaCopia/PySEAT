
class ConditionalStep:
    def __init__(self):
        self.bool_value = True
        self.fully_covered = False

    def get_branch(self):
        assert(not self.all_branches_covered())
        return self.bool_value

    def all_branches_covered(self):
        return self.fully_covered

    def advance_branch(self):
        if self.bool_value:
            self.bool_value = False
        else:
            self.fully_covered = True

    def is_lazy_step(self):
        return False

class LazyStep:
    def __init__(self, branches):
        self.number_of_branches = branches
        self.current_branch = 0

    def get_branch(self):
        assert(not self.all_branches_covered())
        return self.current_branch

    def all_branches_covered(self):
        return self.current_branch > self.number_of_branches

    def advance_branch(self):
        self.current_branch += 1

    def is_lazy_step(self):
        return True

    

