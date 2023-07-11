#!/usr/bin/python3
"""
  Function that defines
  MyInt that inherits from in
"""


class MyInt(int):
    """Operators == and != is invert."""

    def __eq__(self, value):
        """func to change == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Func to chnage != operator with == behavior."""
        return self.real == value
