# -*- coding: utf-8 -*-
"""I/O Utilities.

This package consists of common used utilities for input and output.

"""

# pylint: disable=unused-import
from ._pickle import pickle_dump, pickle_load  # noqa: F401
from ._text import read_text, write_text  # noqa: F401

# pylint: enable=unused-import

__ALL__ = []
__ALL__ += ['pickle_dump', 'pickle_load']
__ALL__ += ['read_text', 'write_text']
