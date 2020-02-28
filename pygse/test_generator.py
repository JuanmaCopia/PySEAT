"""Test Generator

"""

import pygse.proxy as proxy


class TestCode:

    test_number = 0

    def __init__(self, sut, run_stats):
        self._sut = sut
        self._run_stats = run_stats
        self._code = ""

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
        self_id = self.generate_structure_code(self._run_stats.concrete_self)
        args_ids = self.generate_arguments_code(self._run_stats.concrete_args)
        self.generate_method_call(self_id, self._sut.function.__name__, args_ids)
        # self.generate_assertions(self._sut.concrete_return)

    # def generate_assertions(self, instance):
    #     if proxy.is_user_defined(instance):

    def generate_method_call(self, self_id, method_name, args_ids):
        self._code += self_id + "." + method_name + "(" + args_ids + ")\n"

    def generate_code(self, arg):
        if proxy.is_user_defined(arg):
            return self.generate_structure_code(arg)
        else:
            return str(arg)

    @classmethod
    def take_identifier(cls, typ):
        typ._id += 1
        return typ.__name__.lower() + str(typ._id)

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
        self._code += identifier + "." + field + " = " + str(value) + "\n"

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

        code_line = code_line[:-2] + ")\n"
        self._code += code_line

