from symbolics import is_symbolic
from helpers import do_add

import instance_managment as im
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
        instance = symbolize_partially(engine, typ)
        typ._vector.append(instance)
        return instance
    return typ()


def symbolize_partially(engine, user_def_class):
    """Creates partially symbolic instance of a class.

    Returns an instance of user_def_class with all it's builtin
    instance attributes symbolized and it's user-defined attributes
    initialized to None.

    Args:
        user_def_class: The class to be partially symbolized.

    Returns:
        A partially symbolic instance of user_def_class.
    """
    init_types = engine._sut.get_cls_init_types(user_def_class)[1:]

    init_args = [make_symbolic(engine, a) for a in init_types]
    if init_args:
        partial_ins = user_def_class(*init_args)
    else:
        partial_ins = user_def_class()
    attr_names = engine._sut.get_instance_attr_dict(user_def_class).keys()
    # Adding some instrumentation fields
    for attr_name in attr_names:
        setattr(partial_ins, im.ISINIT_PREFIX + attr_name, False)
    setattr(partial_ins, "_objid", engine._ids)
    engine._ids += 1

    return partial_ins


def instrument_instance(instance, user_def_class, attr_names, ins_id):
    for attr_name in attr_names:
        setattr(instance, im.ISINIT_PREFIX + attr_name, False)
    setattr(instance, "_objid", ins_id)


def make_symbolic(engine, typ):
    """Creates a symbolic instance.

    If it's a supported builtin type it returns the appropiate
    symbolic instance.
    If it's an user-defined class returns None

    Args:
        typ: The type to be instantiated. Could be builtin or
        user defined.

    Returns:
        A symbolic instance of a builtin type or None.
    """
    if sym.Symbolic.is_supported_builtin(typ):
        return sym.symbolic_factory(engine, typ)
    elif isinstance(typ, type(None)) or im.is_user_defined(typ):
        return None
    return typ()


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
    elif is_symbolic(symbolic):
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


def fill_class_vectors(structure):
    if not im.is_user_defined(structure):
        return
    visited = set()
    visited.add(structure)
    worklist = []
    worklist.append(structure)
    while worklist:
        current = worklist.pop(0)
        current._vector.append(current)
        for value in im.get_dict_of_prefixed(current).values():
            if im.is_user_defined(value) and do_add(visited, value):
                worklist.append(value)


def search_obj(obj, structure):
    visited = set()
    visited.add(structure)
    worklist = []
    worklist.append(structure)
    while worklist:
        current = worklist.pop(0)
        if obj._objid == current._objid:
            return current
        for value in im.get_dict_of_prefixed(current).values():
            if im.is_user_defined(value) and do_add(visited, value):
                worklist.append(value)
    return None
