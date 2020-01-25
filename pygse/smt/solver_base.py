import collections

"""
This file defines a generic Solver interface. The SMTSolverBase class need to be
subclassed and the NotImplemented methods overwrited in order to work with SMT
"""

class SMTSolverBase(object):
    """
    Abstract Solver instance
    """
    exceptions = ()
    def __init__(self, formula=(), *args, **kwargs): raise NotImplementedError

    def add(self, formula=None):
        """
        Adds a formula or list of formulas to the solver
        """
        raise NotImplementedError

    def clear(self):
        """
        Deletes all stored formulas
        """
        raise NotImplementedError

    def check(self, *args, **kwargs):
        """
        Returns the string 'sat', 'unsat' or 'unkwnown'
        """
        raise NotImplementedError

    def solve(self, *args, **kwargs):
        """
        Returns a SMTModel containin the resulting model.
        If a model can't be found raises an SMTCantFoundModel
        """
        raise NotImplementedError

    def simplify(self, *args):
        """
        Returns a simplified version of a formula
        """
        raise NotImplementedError

    def evaluate(self, model, expr):
        """
        Evaluate the value of `expr` within the model `model`
        """
        raise NotImplementedError


class SMTModelBase(object):
    """
    Stores a model result
    """
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return repr(self.model)

    def evaluate(self, expr):
        raise NotImplementedError


from .smt import SMTException
class SMTCantFoundModel(SMTException):
    def __init__(self, formulas):
        super().__init__("Can't found a model for the formulas\n\t%s" % formulas)