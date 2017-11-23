# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-10-14 13:26:43
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 21:45:03

import sys
import os.path

sys.path.append(os.path.dirname(__file__))

del sys
del os

from input_types import input_types
from noglobals import noglobals
from on_fail import on_fail
from output_type import output_type
from strict_defaults import strict_defaults
from strict_globals import strict_globals
