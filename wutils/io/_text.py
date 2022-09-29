# -*- coding: utf-8 -*-
"""Text Utilities.

This module consists of text-documents utilities.

"""


def read_text(file: str, encoding: str = 'utf-8') -> str:
    """Read content from text file."""
    with open(file, 'r', encoding=encoding) as src:
        ret = src.read()
    return ret


def write_text(data: str, file: str, encoding: str = 'utf-8'):
    """Write content into text file."""
    with open(file, 'w', encoding=encoding) as dst:
        dst.write(data)
