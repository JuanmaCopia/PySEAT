"""
This module handles the constract system for PyMockear
"""
#coding:utf-8
import inspect as _ins
import re as _re
import sys as _sys
import parser as _parser
from ast import literal_eval
import inspect


class ContractError(Exception):
    pass


class MultipleContractError(ContractError):
    def __init__(self, contract):
        super().__init__("Multiple definition of \"%s\" founded." % contract)


class TypeContractError(ContractError):
    pass


class ContractIsNotValidExpressionError(ContractError):
    def __init__(self, function, expr):
        super().__init__("Can't parse the expression: {}.\nFunction: {} in {}"\
                .format(expr, function.__name__, function.__module__+'.py'))


class PreConditionError(ContractError):
    def __init__(self, assume_contract):
        super().__init__("Precondition failed!")


class PostConditionError(ContractError):
    def __init__(self, ensure_contract):
        super().__init__("Postcondition failed!")


def get_class_that_defined_method(meth):
    if hasattr(meth, 'undecorated'):
        meth = meth.undecorated
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
           if cls.__dict__.get(meth.__name__) is meth:
                return cls
        meth = meth.__func__ # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        cls = getattr(inspect.getmodule(meth),
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        if isinstance(cls, type):
            return cls
    return None


class Contract(object):
    """
    All contracts work as oracles, defining the formal semantic of a
    function/method
    """
    kwdel = ":"
    @classmethod
    def parse(cls, function):
        """
        This classmethod parses a function docstring and returns the
        corresponding Contract (if any).
        """
        result = None
        if function.__doc__:
            docstring = [x.strip() for x in function.__doc__.split('\n')]
            pattern = _re.compile(r"%s\s*%s\s*%s" % \
                                  (cls.kwdel, cls.name, cls.kwdel))
            for line in docstring:
                match = pattern.match(line)
                if match:
                    # Remove contract type patter and comments:
                    matched_text = line[match.end():].split("#")[0].strip()
                    result = cls(function, matched_text)
        if not result:
            result = cls(function)
        return result
                # matched_text = line[match.end():].strip() if match else None
                # return cls(function, matched_text)

    @classmethod
    def create_contract_function(cls, function, augmentedContext={}):
        """
        Allow contracts to execute code with the function body context.
        Returns a function with n + 1 parameters where the latests n are the
        function parameters and the first one is a string that's going to be
        evaluated within the function context.
        augmentedContext is an extra keyword that can be used to add more
        values to the function context.
        """
        i_args = inspect.getfullargspec(function)
        def valid_name(name, others=[]):
            return name not in (i_args.args  + [i_args.varargs] + \
                    [i_args.varkw] + i_args.kwonlyargs + others)
        def fresh_name(base="___anonymous", others=[]):
            while not valid_name(base, others):
                base += "_"
            return base
        # Validate the augmented context
        for x in augmentedContext:
            if not valid_name(x):
                raise ContractError("The keyword %s can't be a function argument" % x)
        # Now, we create a fresh var name for the compiled guard
        guard   = fresh_name("___guard", [x for x in augmentedContext.keys()])
        prototype  = "lambda {guard}, {parameters}: eval({guard})"
        args = [(x, None) for x in i_args.args]
        if (i_args.defaults):
            for i in range(1, len(i_args.defaults) + 1):
                args[-i] = (args[-i][0], i_args.defaults[-i])
        parameters = ",".join([str(x) + ("=%s"%y if y else "") for x,y in args])
        if i_args.varargs:    parameters += ",*" + i_args.varargs
        parameters += "," + ",".join([str(x) + "=%s"%(i_args.kwonlydefaults[x]) for x in i_args.kwonlyargs])
        if i_args.varkw:      parameters += ",**" + i_args.varkw
        # Get context
        f_module = _sys.modules[function.__module__]
        context  = dict([(x, getattr(f_module, x)) for x in dir(f_module)])
        context.update(augmentedContext)
        return eval(prototype.format(guard=guard, parameters=parameters), context)


class TypeContract (Contract):
    name = "types?"

    def __init__(self, function, matched_text=None):
        """
        Obtains the type of function/method parameters.
        """
        self._function = function
        self._types = {}
        self.matched_text = matched_text
        if not matched_text:
            return
        regex = r"\[|\]|\:|,|[^\d\W][\w\.]*" # valid ident with [, ], : and ,
        l = _re.findall(regex, matched_text)
        for i, x in enumerate(l):
            # make things string for eval
            if x not in ['[', ']', ':', ',']:
                l[i] = "'" + x + "'"
        to_eval = "{" + "".join(l) + "}"
        self._types = literal_eval(to_eval)
        for k, v in self._types.items():  # Make all args types a list
            if not isinstance(v, list):
                self._types[k] = [v]
        for key, value in self._types.items():
            if isinstance(value, list):
                new_value = [self.eval_type_name(x) for x in value]
            else:
                new_value = self.eval_type_name(value)
            self._types[key] = new_value
        #TODO: warning/error si se declaran tipos en argumentos no declarados


    @property
    def types(self, varargs_default_type=list, varkwargs_default_type=dict):
        """
        :returns: {args: [arg0_type, arg1_type, ],
                   varargs: list or None
                   kwargs: {kwarg0:kwarg0_type, }}
                   varkwargs: dict or None
        """
        result = {'args': [], 'kwargs': {}, 'varargs':None, 'varkwargs': None}
        fullargspec = _ins.getfullargspec(self._function)
        args, varargs, varkwargs, defaults, _, kwargs, _ = fullargspec
        # TODO: tener en cuenta kwargs sin defauts ej: def fun(*args, a):
        kwargs = kwargs if kwargs else {}
        defaults = defaults if defaults else []
        kwargs.update({x:v for x,v in zip(args[-len(defaults):], defaults)})
        if defaults:
            args = args[:-len(defaults)]
        if not self.matched_text:
            cls = get_class_that_defined_method(self._function)
            if args and len(args) > 1 or not cls:
                raise ContractError("Can't guess types in method {0}.".format(\
                                    self._function.__name__))
            result['args'].append(cls)
        else:
            result['args'] = [self._types.get(a) for a in args]
            for i, x in enumerate(result['args'][1:], 1):
                if x is None:
                    raise ContractError("Type of argument '%s' is unknown"\
                        " in method %s." % (args[i], self._function.__name__))
            if get_class_that_defined_method(self._function) and not result['args'][0]:
                result['args'][0] = get_class_that_defined_method(self._function)
            result['kwargs'] = {k: self._types.get(k, []) for k, v in kwargs.items()}
            for k, v in kwargs.items():
                # Adding defaults kwargs values if their type is not present.
                if type(v) not in result['kwargs'][k]:
                    result['kwargs'][k].append(v)
        result['varargs'] = varargs_default_type if varargs else None
        result['varkwargs'] = varkwargs_default_type if varkwargs else None
        return result

    def eval_type_name(self, type_name):
        # First, we check if it is a builtin
        obj = __builtins__.get(type_name)
        if not obj:
            obj = type(None) if type_name in ['NoneType', 'None'] else None
        # If it is not...
        if not obj:
            # Check if the type is defined/included in the function module
            module = _sys.modules[self._function.__module__]
            type_names = type_name.split('.')
            try:
                for name in type_names:
                    module = getattr(module, name)
            except AttributeError:
                raise ContractError("Class %s not found" % type_name)
            obj = module
        return obj if type(obj) == type else type_name


class AssumeContract(Contract):
    name = "assumes?"

    def __init__(self, function, matched_text=None):
        """
        Precondition contracts
        """
        self._function = function
        self.matched_text = matched_text
        if not matched_text:
            return
        try:
            exp = _parser.expr(matched_text)
        except SyntaxError:
            raise ContractIsNotValidExpressionError(function, matched_text)
        self.function = function
        self.guard = exp

    def validate(self, *args, **kwargs):
        if not self.matched_text:
            return True
        ccf = self.create_contract_function(self._function)
        ret = ccf(self.guard.compile(), *args, **kwargs)
        is_valid = all(ret) if type(ret) == tuple else ret
        if not is_valid:
            raise PreConditionError(self)


class EnsureContract(Contract):
    name = "ensures?"

    def __init__(self, function, matched_text=None):
        """
        Precondition contracts
        """
        self._function = function
        self.matched_text = matched_text
        if not matched_text:
            return
        try:
            exp = _parser.expr(matched_text)
        except SyntaxError:
            raise ContractIsNotValidExpressionError(function, matched_text)
        self.function = function
        self.guard = exp

    def validate(self, returnv, *args, **kwargs):
        if not self.matched_text:
            return True
        try:
            ccf = self.create_contract_function(self._function, {"returnv": returnv})
            ret = ccf(self.guard.compile(), *args, **kwargs)
            result = all(ret) if type(ret) == tuple else ret
            if not result:
                raise PostConditionError(self)
        except Exception as e:
            raise ContractError("In function %s's ensure contract: %s" %\
                                        (self.function.__name__, e))



class ExceptionContract(Contract):
    name = "raises?"

    def __init__(self, function, matched_text=None):
        """
        Exception contracts
        """
        self._function = function
        self.matched_text = matched_text
        if not matched_text:
            return
        regex = r"[:\n]" #FIXME: add support for dicts in the expression
        l = _re.split(regex, matched_text)
        for i, x in enumerate(l):
            # make things string for eval
            if i % 2 == 0:
                x = "isinstance(__exception__, " + x + ") and "
            else:
                x = "not all([" + x.strip() + "]), "
            l[i] = "'" + x + "'"
        l.insert(0, "'['")
        l.append("']'")
        to_eval = "".join(l)
        self._exceptions = literal_eval(to_eval)
        try:
            exp = _parser.expr(self._exceptions)
        except SyntaxError:
            raise ContractIsNotValidExpressionError(function, matched_text)
        self.function = function
        self.guard = exp

    def validate(self, exception, *args, **kwargs):
        if not self.matched_text:
            return False
        check_contracts = self.create_contract_function(self._function,
                                            {'__exception__': exception})
        errors = check_contracts(self.guard.compile(), *args, **kwargs)
        return any(errors)



def find_all_contracts(function):
    """
    Generate the contract system for a given function.
    contractTypes is a iterable of contract classes to find in the given
    function, if contractTypes is None all types of constracts will be searched
    """
    result = dict([(x, None) for x in Contract.__subclasses__()])
    for contract_class in result:
        contract = contract_class.parse(function)
        if contract:
            result[contract_class] = contract
    return result