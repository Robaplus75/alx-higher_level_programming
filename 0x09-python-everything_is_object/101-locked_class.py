#!/usr/bin/python3
"""locked class definition"""


class LockedClass:
    """for preventing users from instantiating new LockedClass attributes"""

    __slots__ = ["first_name"]
