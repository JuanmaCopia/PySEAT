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
        self.reset_id_numbers()
        self.generate_test_code()
        return self._code

    def reset_id_numbers(self):
        for udclass in self._sut.class_params_map:
            udclass._id = 0

    def generate_test_code(self):
        self_id = self.generate_structure_code(self._run_stats.concrete_self)
        # args_ids = ""
        # for arg in self._run_stats.concrete_args:
        #     args_ids += self.generate_code(arg) + ","
        # if args_ids:
        #     args_ids = args_ids[:-1]

        # self.generate_method_call(self_id, self._sut.function.__name__, args_ids)

    def generate_method_call(self, self_id, function_name, args):
        self._code += self_id + "." + function_name + "(" + args + ")\n"

    def generate_code(self, arg):
        if proxy.is_user_defined(arg):
            return self.generate_structure_code(arg)
        else:
            return str(arg)

    @classmethod
    def take_identifier(cls, typ):
        identifier = typ.__name__.lower() + str(typ._id)
        typ._id += 1
        return identifier

    def generate_structure_code(self, instance):
        if instance._identifier:
            return instance._identifier
        attr = {
            key: value
            for (key, value) in instance.__dict__.items()
            if key
            not in ["_next_is_initialized", "_marked", "_concretized", "_identifier",]
        }

        identifier = self.take_identifier(type(instance))

        instance._identifier = identifier

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
        ctor_dict = {}
        for name in params_dict:
            if name in ins_dict:
                ctor_dict[name] = ins_dict[name]
            else:
                assert False

        code_line = identifier + " = " + typ.__name__ + "("

        for k, v in ctor_dict.items():
            obj_name = ""
            if proxy.is_user_defined(v):
                obj_name = self.generate_structure_code(v)
                code_line += obj_name + ","
            else:
                code_line += str(ctor_dict[k]) + ","

        code_line = code_line[:-1] + ")\n"
        self._code += code_line

