# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-10-14 13:26:43
# @Last Modified 2018-03-05
# @Last Modified time: 2018-03-05 10:32:14

import sys
import os.path

sys.path.append(os.path.dirname(__file__))

del sys
del os

from c_version import c_version
from force_assertions import force_assertions
from input_types import input_types
from never_parallel import never_parallel
from noglobals import noglobals
from on_fail import on_fail
from output_type import output_type
from overload import overload
from self_aware import self_aware
from strict_defaults import strict_defaults
from strict_globals import strict_globals

