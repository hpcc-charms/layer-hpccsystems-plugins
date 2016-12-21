#!/usr/bin/env python3

import os
import platform
import yaml
import re
#import Configparser
#from subprocess import check_call,check_output,CalledProcessError

from charmhelpers.core import hookenv
from charmhelpers.core.hookenv import  (
    log,
    CRITICAL,
    ERROR,
    WARNING,
    INFO,
    DEBUG
)


from charms.reactive.helpers import is_state
from charms.reactive.bus import (
   set_state,
   get_state,
   remove_state
)
from charms.reactive import when
from charms.reactive import when_not

from charms.layer.hpccsystems_plugin import HPCCSystemsPluginConfig



