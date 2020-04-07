from pygse.smt.solver_base import SMTSolverBase, SMTModelBase
from pygse.smt.smt import SMTCantFoundModel
import z3


class SMTSolver(SMTSolverBase):
    exceptions = z3.Z3Exception

    def __init__(self, formula=(), *args, **kwargs):
        self.solver = z3.Solver()
        self.checked, self.check_result = True, "sat"
        self.modeled, self.model = False, None
        self.add(formula)

    def add(self, formula=None):
        if formula is not None:
            self.solver.add(formula)
            self.checked = False

    def clear(self):
        self.solver.reset()
        self.checked, self.check_result = True, "sat"
        self.modeled, self.model = False, None

    def check(self, *args, **kwargs):
        if not self.checked:
            self.checked = True
            self.check_result = str(self.solver.check())
            self.modeled = False
        return self.check_result

    def simplify(self, *args):
        return z3.simplify(*args)

    def solve(self, *args, **kwargs):
        if not self.checked:
            self.check()
        if self.check_result == "sat":
            if not self.modeled:
                self.modeled = True
                self.model = self.solver.model()
            return SMTModel(self.model)
        else:
            raise SMTCantFoundModel(self.solver.assertions())


class SMTModel(SMTModelBase):
    def evaluate(self, exp):
        return self.model.evaluate(exp, model_completion=True)

