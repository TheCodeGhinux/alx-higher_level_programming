#!/usr/bin/python3
"Defines a class LockedClass"


class LockedClass:
    """To prevents the user from dynamically
      creating new instance attributes, except if the
      new instance attribute is called first_name"""

    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"Cannot create new instance attr '{name}'")
        self.__dict__[name] = value
