from symbolics import Symbolic
from helpers import do_add

import instance_management as im
import symbolics as sym
import copy


def symbolic_instantiation(engine, typ):
    """Creates a symbolic or a partially symbolic instance.

    If it's a supported builtin type it returns the appropiate
    symbolic instance.
    If it's an user-defined class returns a partially symbolic
    instance of that class

    Args:
        typ: The type to be instantiated. Could be builtin or
        user defined.

    Returns:
        A symbolic or partially symbolic instance.
    """
    if sym.Symbolic.is_supported_builtin(typ):
        return sym.symbolic_factory(engine, typ)
    elif isinstance(typ, type(None)):
        return None
    elif im.is_user_defined(typ):
        return create_symbolic_instance(engine, typ)
    return typ()


def create_symbolic_instance(engine, user_def_class):
    """Creates partially symbolic instance of a class.

    Returns an instance of user_def_class with all it's builtin
    instance attributes symbolized and it's user-defined attributes
    initialized to None.

    Args:
        user_def_class: The class to be partially symbolized.

    Returns:
        A partially symbolic instance of user_def_class.
    """
    partial_ins = object.__new__(user_def_class)
    attributes = engine._sut.get_instance_attr_dict(user_def_class)
    # Adding some instrumentation fields
    for attr_name, typ in attributes.items():
        if sym.Symbolic.is_supported_builtin(typ):
            value = sym.symbolic_factory(engine, typ)
            setattr(partial_ins, im.ISINIT_PREFIX + attr_name, True)
        elif isinstance(typ, type(None)) or im.is_user_defined(typ):
            value = None
            setattr(partial_ins, im.ISINIT_PREFIX + attr_name, False)
        else:
            value = typ()
            setattr(partial_ins, im.ISINIT_PREFIX + attr_name, True)

        setattr(partial_ins, im.SYMBOLIC_PREFIX + attr_name, value)

    setattr(partial_ins, "_objid", engine.classes_instances[user_def_class].number)
    engine.classes_instances[user_def_class].number += 1
    user_def_class._vector.append(partial_ins)

    return partial_ins


def concretize(symbolic, model):
    visited = set()
    sym_copy = copy.deepcopy(symbolic)
    if im.is_user_defined(sym_copy):
        visited.add(sym_copy)
    return _concretize(sym_copy, model, visited)


def _concretize(symbolic, model, visited):
    """Creates the concrete object.

    Creates the concrete object from a symbolic (builtin symbolic)
    or a partially symbolic (user-defined) one and the model
    describing it's restrictions.

    Args:
        symbolic: a symbolic builtin or a partially symbolic
            user-defined class.
        model: Model describing the constraints that the object
            must acomplish.

    Returns:
        The concrete object represented by symbolic and the model.
    """
    if symbolic is None:
        return None
    elif isinstance(symbolic, Symbolic):
        return symbolic.concretize(model)
    elif isinstance(symbolic, list):
        for i, x in enumerate(symbolic):
            symbolic[i] = _concretize(x, model, visited)
        return symbolic
    elif im.is_user_defined(symbolic):
        for pref_name, value in im.get_dict_of_prefixed(symbolic).items():
            if not callable(value) and do_add(visited, value):
                setattr(symbolic, pref_name, _concretize(value, model, visited))
        return symbolic
    return symbolic
