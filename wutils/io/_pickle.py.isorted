# -*- coding: utf-8 -*-
"""Pickle Utilities.

This module consists of pickle utilities.

"""

import pickle


def pickle_load(file: str) -> object:
    """Loda a pickle file to an object."""
    with open(file, 'rb') as src:
        ret = pickle.load(src)
    return ret


def pickle_dump(obj: object, file: str):
    """Save an object to a pickle file."""
    with open(file, 'wb') as dst:
        pickle.dump(obj, dst)
