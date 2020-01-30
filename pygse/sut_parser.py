import importlib
import copy

from pygse.proxy import is_user_defined
from pygse.engine_errors import MissingTypesError


class SUTParser:
    def __init__(self):
        self.module = None
        self.sclass = None
        self.function = None
        self.types = []
        self.class_params_map = {}
        self.is_method = False

    def parse(self, module_name, function_name, class_name=None):
        self.module = importlib.import_module(module_name)
        if class_name:
            self.sclass = getattr(self.module, class_name)
            self.function = getattr(self.sclass, function_name)
            self.types = self.parse_types()
            self.class_params_map = self.get_user_defined_objects(self.sclass)
            self.is_method = True

    def parse_types(self):
        types = self.function.__annotations__
        not_self = False
        if "self" not in types:
            not_self = True
        if "return" in types:
            del types["return"]
        types_list = self.set_classes(list(types.values()))
        if not_self:
            types_list.insert(0, self.sclass)

        if self.function.__code__.co_argcount != len(types_list):
            raise MissingTypesError("Types missing in: " + self.function.__name__)
        return types_list

    def set_classes(self, types):
        for i, t in enumerate(types):
            if isinstance(t, str):
                types[i] = getattr(self.module, t)
        return types

    def parse_types_whitout_self(self, function):
        types = function.__annotations__
        if types:
            if "self" in types:
                del types["self"]
            if "return" in types:
                del types["return"]
            return self.set_classes(list(types.values()))
        return []

    def get_user_defined_objects(self, user_def_class):
        class_to_types = {}
        types = self.parse_types_whitout_self(user_def_class.__init__)
        class_to_types[user_def_class] = types

        objects_added = copy.deepcopy(class_to_types[user_def_class])

        added = True if objects_added else False

        while added:
            added = False
            new_classes = []
            for c in objects_added:
                if is_user_defined(c) and c not in class_to_types.keys():
                    new_classes.append(c)

            if new_classes:
                added = True
                for nc in new_classes:
                    class_to_types[nc] = self.parse_types_whitout_self(nc.__init__)
                    objects_added.extend(class_to_types[nc])
        return class_to_types
