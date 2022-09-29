# -*- coding: utf-8 -*-
"""Contexts common used in this test package."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../..')))

# pylint: disable=wrong-import-position, unused-import, wrong-import-order
from wutils.io import (  # noqa: E402, F401
    pickle_dump,
    pickle_load,
    read_text,
    write_text,
)

# pylint: enable=wrong-import-position, unused-import, wrong-import-order
