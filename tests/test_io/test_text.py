# -*- coding: utf-8 -*-
"""Tests for `io.text` Module."""

import os

from ._context import read_text, write_text


def test_write_and_read_text():
    """Test for `write_text` and `read_text`."""
    file = '_tempory_file_for_test_write_and_read_text.txt'
    text = "a \n c"
    write_text(text, file)
    recv = read_text(file)
    os.remove(file)
    assert text == recv
