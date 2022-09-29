# -*- coding: utf-8 -*-
"""Contexts common used in this test package."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../..')))

# pylint: disable=wrong-import-position, unused-import, wrong-import-order
from wutils.io import pickle_dump, pickle_load  # noqa: E402, F401

# pylint: enable=wrong-import-position, unused-import, wrong-import-order
