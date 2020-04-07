from decorator import decorator
from functools import wraps


def check_comparable_types(comp_fun):
    @wraps(comp_fun)
    def comp(self, other):
        stype = type(self)
        otype = type(other)
        rtype = self.emulated_class
        if otype not in [stype, rtype]:
            raise TypeError(
                "unorderable types: %s(), %s()" % (stype.__name__, otype.__name__)
            )
        else:
            return comp_fun(self, other)

    return comp


def check_equality(eq_fun):
    @wraps(eq_fun)
    def eq(self, other):
        stype = type(self)
        otype = type(other)
        rtype = self.emulated_class
        if otype not in [stype, rtype]:
            return False
        else:
            return eq_fun(self, other)

    return eq


def forward_to_rfun(*args):
    def forward_bin_fun_to_rfun(fun):
        """
        Forward a call to fun the its reverse version if necessary.
        Example: 10 * [1,2,3] ----> [1,2,3] * 10
        """

        def valid_parameter(self, other):
            if args:
                return any([isinstance(other, x) for x in args])
            else:
                return any(
                    [isinstance(other, x) for x in [type(self), self.emulated_class]]
                )

        def forwarder_fun(fun, self, other):
            if not valid_parameter(self, other):
                # This is a bit hardcoded
                rfun_name = "__r" + fun.__name__[2:]
                rfun = getattr(other, rfun_name, None)
                if rfun:
                    return rfun(self)
                else:
                    raise TypeError(
                        "unsupported operand type(s) for %s: '%s' and '%s'"
                        % (fun.__name__, type(self).__name__, type(other).__name__)
                    )
            else:
                return fun(self, other)

        return decorator(forwarder_fun)(fun)

    return forward_bin_fun_to_rfun


def check_self_and_other_have_same_type(fun):
    """
    This function/decorator is usefull in __rfuns__. It checks that the type of
    other is either the type of self or self.emulated_class
    """

    def type_check(fun, self, other):
        if not (
            isinstance(other, type(self)) or isinstance(other, self.emulated_class)
        ):
            raise TypeError(
                "unsupported operand type(s) for %s: '%s' and '%s'"
                % (fun.__name__, type(self).__name__, type(other).__name__)
            )
        else:
            return fun(self, other)

    return decorator(type_check)(fun)
