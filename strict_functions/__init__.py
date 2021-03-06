# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-10-14 13:26:43
# @Last Modified 2018-03-15
# @Last Modified time: 2018-03-15 11:52:06

import sys
import os.path

#sys.path.append(os.path.dirname(__file__))

from .attempt import attempt
from .force_assertions import force_assertions
from .input_types import input_types
from .never_parallel import never_parallel
from .noglobals import noglobals
from .on_fail import on_fail
from .output_type import output_type
from .overload import overload
from .self_aware import self_aware
from .strict_defaults import strict_defaults
from .strict_globals import strict_globals

if sys.version_info >= (3,0):
    from .trace3 import trace
else:
    from .trace2 import trace
try:
    from .lru_cache3 import lru_cache
except:
    from .lru_cache2 import lru_cache
try:
    from .cached3 import cached
except:
    from .cached2 import cached


#sys.path.remove(os.path.dirname(__file__))

del sys
del os
