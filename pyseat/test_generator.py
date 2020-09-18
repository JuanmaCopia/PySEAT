"""Test Generator

"""

from helpers import do_add
from instance_management import get_dict, var_name, is_user_defined
import data
import os


def create_testfile(module_name, class_name):
    mod_basename = os.path.splitext(os.path.basename(module_name))[0]
    foldername = os.path.dirname(module_name) + "/"
    filename = "test_" + mod_basename + ".py"
    filepath = foldername + filename
    importstr = "from " + mod_basename + " import *"
    importstr += "\nimport pytest\n\n"
    create_file(filepath, importstr)
    return "test_" + mod_basename, mod_basename, foldername, filepath


def create_file(filepath, str):
    file = open(filepath, "w")
    file.write(str + "\n")
    file.close()


def append_to_testfile(filepath, str):
    file = open(filepath, "a")
    file.write(str + "\n")
    file.close()


class TestCode:
    def __init__(self, sut, run_stats, number, timeout, comments):
        self._sut = sut
        self.run_data = run_stats
        self.status = run_stats.status
        self.test_number = number
        self.input_code = ""
        self.code = ""
        self.name = "test_" + sut.get_method_name() + str(number) + "()"
        self.timeout = timeout
        self.comments = comments
        self.generate_test_code()

    def _add_line(self, line, isinput=False):
        self.code += "\n    " + line
        if isinput:
            self.input_code += line

    def generate_arguments_code(self, instance):
        args_ids = ""
        for arg in instance:
            if is_user_defined(arg):
                args_ids += self.generate_structure_code(arg) + ", "
            else:
                args_ids += str(arg) + ", "
        return args_ids[:-2]

    def generate_test_code(self):
        if self.status == data.TIMEOUT:
            self.code += "@pytest.mark.timeout({})\n".format(self.timeout)
        self.code += "def " + self.name + ":"
        if self.comments:
            self.gen_test_comment()
        self._add_line("# Input Creation")
        self_id = self.generate_structure_code(self.run_data.input_self)
        self._add_line("# Repok check")
        self.add_repok_check(self.run_data.input_self)
        self._add_line("# Method call")
        self.generate_method_call(
            self_id, self._sut.get_method_name(), self.run_data.returnv
        )
        self._add_line("# Repok check")
        self.add_repok_check(self.run_data.input_self)
        if self.status == data.OK or self.status == data.FAIL:
            self._add_line("# Assertions")
            self.gen_returnv_assert(self.run_data.returnv)
            self.gen_structure_assertions(self.run_data.self_end_state)

    def gen_test_comment(self):
        self._add_line("'''")
        self._add_line("Self:")
        self._add_line("    " + self.run_data.input_self.__repr__())
        if self.status != data.TIMEOUT and self.status != data.EXCEPTION:
            self._add_line("Return:")
            self._add_line("    " + self.run_data.returnv.__repr__())
            self._add_line("End Self:")
            self._add_line("    " + self.run_data.self_end_state.__repr__())
        self._add_line("'''")

    def add_repok_check(self, structure):
        self._add_line("assert " + var_name(structure) + ".repok()")

    def create_return_assert_code(self, value):
        if value is None:
            self._add_line("assert returnv is None", True)
        else:
            self._add_line("assert returnv == " + str(value), True)

    def create_assert_code(self, identifier, field, value):
        if value is not None:
            comp = " == "
        else:
            comp = " is "
        self._add_line("assert " + identifier + "." + field + comp + str(value), True)

    def gen_returnv_assert(self, returnv):
        if is_user_defined(returnv):
            self.gen_structure_assertions(returnv, "returnv")
        else:
            self.create_return_assert_code(returnv)

    def gen_structure_assertions(self, structure, identifier=None):
        if not is_user_defined(structure):
            return
        visited = set()
        visited.add((structure))
        worklist = []
        if identifier:
            worklist.append((structure, identifier))
        else:
            worklist.append((structure, var_name(structure)))
        while worklist:
            current = worklist.pop(0)
            curstruct = current[0]
            curident = current[1]
            structdict = get_dict(curstruct)
            for attr_name, value in structdict.items():
                if is_user_defined(value):
                    if do_add(visited, value):
                        worklist.append((value, curident + "." + attr_name))
                else:
                    self.create_assert_code(curident, attr_name, value)

    def generate_method_call(self, self_id, method_name, returnv=None):
        args_ids = self.generate_arguments_code(self.run_data.input_args)
        self._add_line(
            "returnv = " + self_id + "." + method_name + "(" + args_ids + ")", True
        )

    def generate_structure_code(self, instance, visited=set()):
        if not instance:
            return
        if not do_add(visited, instance):
            return var_name(instance)

        identifier = var_name(instance)

        self.create_constructor_call(
            identifier,
            type(instance),
            self._sut.get_params_type_dict(type(instance)),
        )
        userdef = []
        for field, value in get_dict(instance).items():
            if not is_user_defined(value):
                if value is None or isinstance(value, (bool, int, float, str)):
                    self.create_assign_code(identifier, field, value)
            else:
                userdef.append((field, value))
        field_id = ""
        for field, value in userdef:
            field_id = self.generate_structure_code(value, visited)
            self.create_assign_code(identifier, field, field_id)
        return identifier

    def create_assign_code(self, identifier, field, value):
        self._add_line(identifier + "." + field + " = " + str(value) + "", True)

    def create_constructor_call(self, identifier, typ, params_dict):
        if "self" in params_dict:
            del params_dict["self"]
        ctor_params = {}
        for name, t in params_dict.items():
            if is_user_defined(t):
                ctor_params[name] = None
            else:
                ctor_params[name] = t()

        if ctor_params:
            code_line = identifier + " = " + typ.__name__ + "("

            for name, value in ctor_params.items():
                obj_name = ""
                if is_user_defined(value):
                    obj_name = "None"
                    code_line += obj_name + ", "
                else:
                    code_line += str(ctor_params[name]) + ", "

            code_line = code_line[:-2] + ")"
        else:
            code_line = identifier + " = " + typ.__name__ + "()"
        self._add_line(code_line, True)
