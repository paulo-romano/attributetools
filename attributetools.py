# coding: utf-8
def set_attributes(func, **dict_attributes):
    for key in dict_attributes:
        func.__setattr__(key, dict_attributes[key])


class attribute():
    def __init__(self, **attributes):
        self.attributes = attributes

    def __call__(self, func):
        set_attributes(func, **self.attributes)
        return func
