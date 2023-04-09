
def set_module(module):
    """Private decorator for overriding __module__ on a function or class.

    Example usage::

        @set_module('gmail_rules')
        def example():
            pass

        assert example.__module__ == 'gmail_rules'
    """
    def decorator(func):
        if module is not None:
            func.__module__ = module
        return func
    return decorator

from . import rule
from . import copy_to

__all__ = [
    "Rule",
    "Copy_To"
]

# from . import rule_classes

# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))

# for f in modules:
#     if isfile(f) and not f.endswith('__init__.py'):
#         exec(f"from .{basename(f)[:-3]} import *")
