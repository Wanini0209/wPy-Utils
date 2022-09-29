# -*- coding: utf-8 -*-
"""Tests for `io.pickle` Module."""

import os

from ._context import pickle_dump, pickle_load


def test_pickle_dump_and_load():
    """Test for `pickle_dump` and `pickle_load`."""
    file = '_tempory_file_for_test_pickle_dump_and_load.pkl'
    obj = 1
    pickle_dump(obj, file)
    recv = pickle_load(file)
    os.remove(file)
    assert type(obj) is type(recv) and obj == recv
