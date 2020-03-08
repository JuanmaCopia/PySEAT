"""Test Generator

"""

import pygse.proxy as proxy


class TestCode:
    def __init__(self, sut, run_stats, number):
        self._sut = sut
        self._run_stats = run_stats
        self._code = ""
        self.test_number = number

    def _add_line(self, line):
        self._code += "\n    " + line

    def get_code(self):
        self.generate_test_code()
        return self._code

    def generate_arguments_code(self, instance):
        args_ids = ""
        for arg in instance:
            if proxy.is_user_defined(arg):
                args_ids += self.generate_structure_code(arg) + ", "
            else:
                args_ids += str(arg) + ", "
        return args_ids[:-2]

    def generate_test_code(self):
        self.gen_test_header()
        self._add_line("# Input Generation")
        self_id = self.generate_structure_code(self._run_stats.concrete_input_self)
        self._add_line("# Repok check")
        self.add_repok_check(self._run_stats.concrete_input_self)
        self._add_line("# Method call")
        self.generate_method_call(
            self_id, self._sut.function.__name__, self._run_stats.concrete_return
        )
        self._add_line("# Assertions")
        self.gen_returnv_assert(self._run_stats.concrete_return)
        self._add_line("# Repok check")
        self.add_repok_check(self._run_stats.concrete_end_self)
        self.gen_structure_assertions(self._run_stats.concrete_end_self)


    def gen_test_header(self):
        self._code += (
            "def "
            + self._sut.function.__name__
            + "_test"
            + str(self.test_number)
            + "():"
        )

    def add_repok_check(self, structure):
        self._add_line("assert " + structure._identifier + ".repok()")

    def gen_returnv_assert(self, returnv):
        if proxy.is_user_defined(returnv):
            self.create_return_assert_code(returnv._identifier)
            self.gen_structure_assertions(returnv)
        else:
            if returnv:
                self.create_return_assert_code(returnv)

    def create_return_assert_code(self, value):
        self._add_line("assert returnv == " + str(value))

    def create_assert_code(self, identifier, field, value):
        if value is not None:
            comp = " == "
        else:
            comp = " is "
        self._add_line("assert " + identifier + "." + field + comp + str(value))

    def gen_structure_assertions(self, instance, defined_identifier=None):
        if not instance._generated:
            instance._generated = True

            if defined_identifier:
                identifier = defined_identifier
            else:
                identifier = instance._identifier

            attr = self.get_attr_value_dict(instance)

            userdef = []
            for field, value in attr.items():
                if proxy.is_user_defined(value):
                    userdef.append((field, value))
                    # self.create_assert_code(identifier, field, value._identifier)
                else:
                    self.create_assert_code(identifier, field, value)

            for field, value in userdef:
                self.gen_structure_assertions(value, identifier + "." + field)

    def generate_method_call(self, self_id, method_name, returnv=None):
        args_ids = self.generate_arguments_code(self._run_stats.concrete_args)
        if returnv:
            self._add_line(
                "returnv = " + self_id + "." + method_name + "(" + args_ids + ")"
            )
        else:
            self._add_line(self_id + "." + method_name + "(" + args_ids + ")")

    @classmethod
    def is_special_attr(cls, attr_name):
        return attr_name.endswith("_is_initialized") or attr_name in [
            "_marked",
            "_concretized",
            "_identifier",
            "_generated",
        ]

    @classmethod
    def get_attr_value_dict(cls, instance):
        return {
            key: value
            for (key, value) in instance.__dict__.items()
            if not cls.is_special_attr(key)
        }

    def generate_structure_code(self, instance):
        if not instance:
            return "Attempted to generate the code for a None self\n"
        if instance._generated:
            return instance._identifier

        instance._generated = True
        identifier = instance._identifier

        attr = self.get_attr_value_dict(instance)
        self.create_constructor_call(
            identifier, type(instance), attr, self._sut.get_init_params(type(instance)),
        )

        userdef = []
        for field, value in attr.items():
            if not proxy.is_user_defined(value):
                self.create_assign_code(identifier, field, value)
            else:
                userdef.append((field, value))
        field_id = ""
        for field, value in userdef:
            field_id = self.generate_structure_code(value)
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

        code_line = identifier + " = " + typ.__name__ + "("

        for name, value in ctor_params.items():
            obj_name = ""
            if proxy.is_user_defined(value):
                obj_name = self.generate_structure_code(value)
                code_line += obj_name + ", "
            else:
                code_line += str(ctor_params[name]) + ", "

        code_line = code_line[:-2] + ")"
        self._add_line(code_line)

