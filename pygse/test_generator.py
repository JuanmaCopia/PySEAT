"""Test Generator

"""

from helpers import is_special_attr, is_user_defined, do_add, remove_prefix
import os


def create_testfile(module_name, class_name, method_name):
    def remove_instrumented(module_name):
        if module_name.endswith("_instrumented"):
            return module_name[: -len("_instrumented")]
        return module_name

    mod_basename = os.path.splitext(os.path.basename(module_name))[0]
    mod_basename = remove_instrumented(mod_basename)
    foldername = os.path.dirname(module_name) + "/"
    filename = mod_basename + "_" + method_name + "_tests.py"
    filepath = foldername + filename
    importstr = "from " + mod_basename + " import Node, " + class_name + "\n\n"
    create_file(filepath, importstr)
    return filepath


def append_test_calls(filepath, tests_gen):
    append_to_testfile(filepath, "if __name__ == '__main__':")
    for test in tests_gen:
        append_to_testfile(filepath, "    " + test.name)


def create_file(filepath, str):
    file = open(filepath, "w")
    file.write(str + "\n")
    file.close()


def append_to_testfile(filepath, str):
    file = open(filepath, "a")
    file.write(str + "\n")
    file.close()


class TestCode:
    def __init__(self, sut, run_stats, number):
        self._sut = sut
        self.run_data = run_stats
        self.test_number = number
        self.code = ""
        self.name = sut.get_method_name() + "_test" + str(number) + "()"
        self.generate_test_code()

    def _add_line(self, line):
        self.code += "\n    " + line

    def generate_arguments_code(self, instance):
        args_ids = ""
        for arg in instance:
            if is_user_defined(arg):
                args_ids += self.generate_structure_code(arg) + ", "
            else:
                args_ids += str(arg) + ", "
        return args_ids[:-2]

    def generate_test_code(self):
        self.gen_test_header()
        self.gen_test_comment()
        self._add_line("# Self Generation")
        self_id = self.generate_structure_code(self.run_data.input_self)
        self._add_line("# Repok check")
        self.add_repok_check(self.run_data.input_self)
        self._add_line("# Method call")
        self.generate_method_call(
            self_id, self._sut.get_method_name(), self.run_data.returnv
        )
        self._add_line("# Assertions")
        self.gen_returnv_assert(self.run_data.returnv)
        self._add_line("# Repok check")
        self.add_repok_check(self.run_data.self_end_state)
        self.gen_structure_assertions(self.run_data.self_end_state)
        self._add_line("print('Test" + str(self.test_number) + ": OK')")

    def gen_test_comment(self):
        self._add_line("'''")
        self._add_line("Self:")
        self._add_line("    " + self.run_data.input_self.__repr__())
        self._add_line("Return:")
        self._add_line("    " + self.run_data.returnv.__repr__())
        self._add_line("End Self:")
        self._add_line("    " + self.run_data.self_end_state.__repr__())
        self._add_line("'''")

    def gen_test_header(self):
        self.code += (
            "def "
            + self._sut.get_method_name()
            + "_test"
            + str(self.test_number)
            + "():"
        )

    def add_repok_check(self, structure):
        self._add_line("assert " + structure._identifier + ".repok()")

    def create_return_assert_code(self, value):
        self._add_line("assert returnv == " + str(value))

    def create_assert_code(self, identifier, field, value):
        if value is not None:
            comp = " == "
        else:
            comp = " is "
        self._add_line("assert " + identifier + "." + field + comp + str(value))

    def gen_returnv_assert(self, returnv):
        if is_user_defined(returnv):
            self.gen_structure_assertions(returnv, "returnv")
        else:
            if returnv:
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
            worklist.append((structure, structure._identifier))
        while worklist:
            current = worklist.pop(0)
            curstruct = current[0]
            curident = current[1]
            structdict = self.get_attr_value_dict(curstruct)
            for attr_name, value in structdict.items():
                if is_user_defined(value):
                    if do_add(visited, value):
                        worklist.append((value, curident + "." + attr_name))
                else:
                    self.create_assert_code(curident, attr_name, value)

    def generate_method_call(self, self_id, method_name, returnv=None):
        args_ids = self.generate_arguments_code(self.run_data.input_args)
        if returnv:
            self._add_line(
                "returnv = " + self_id + "." + method_name + "(" + args_ids + ")"
            )
        else:
            self._add_line(self_id + "." + method_name + "(" + args_ids + ")")

    @classmethod
    def get_attr_value_dict(cls, instance):
        return {
            remove_prefix(key): value
            for (key, value) in instance.__dict__.items()
            if not is_special_attr(key)
        }

    def generate_structure_code(self, instance, visited=set()):
        if not instance:
            return
        if not do_add(visited, instance):
            return instance._identifier

        identifier = instance._identifier
        attr = self.get_attr_value_dict(instance)
        self.create_constructor_call(
            identifier,
            type(instance),
            attr,
            self._sut.get_params_type_dict(type(instance)),
        )
        userdef = []
        for field, value in attr.items():
            if not is_user_defined(value):
                self.create_assign_code(identifier, field, value)
            else:
                userdef.append((field, value))
        field_id = ""
        for field, value in userdef:
            field_id = self.generate_structure_code(value, visited)
            self.create_assign_code(identifier, field, field_id)
        return identifier

    def create_assign_code(self, identifier, field, value):
        self._add_line(identifier + "." + field + " = " + str(value) + "")

    def create_constructor_call(self, identifier, typ, ins_dict, params_dict):
        if "self" in params_dict:
            del params_dict["self"]
        ctor_params = {}
        for name in params_dict:
            if name in ins_dict:
                ctor_params[name] = ins_dict[name]
            else:
                assert False

        if ctor_params:
            code_line = identifier + " = " + typ.__name__ + "("

            for name, value in ctor_params.items():
                obj_name = ""
                if is_user_defined(value):
                    obj_name = self.generate_structure_code(value)
                    code_line += obj_name + ", "
                else:
                    code_line += str(ctor_params[name]) + ", "

            code_line = code_line[:-2] + ")"
        else:
            code_line = identifier + " = " + typ.__name__ + "()"
        self._add_line(code_line)
