#!/usr/bin/python3
"""
  Function that defines an
  an inherited list class MyList
"""


class MyList(list):
    """Implements sorted list printing in ascending order."""

    def print_sorted(self):
        """List in sorted ascending order."""
        print(sorted(self))
