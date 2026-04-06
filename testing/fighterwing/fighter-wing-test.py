


import time
import os 
from afem.config import Settings
from afem.geometry import *
from afem.oml import *
from afem.structure import *
from afem.topology import *

Settings.log_to_console()

def buildFighterWingbox(wing, params):
    """
    Building a multispar wingbox that is typical for a high-performance fighter
    
    """

    # Set units to ft. 
    Settings.set_units('ft')
    
    # Initial Setup Parameters
    _default = {'rib spacing':6. ,
                'fspar chord':0.25, 
                'rspar chord': 0.75, 
                'root span': 0.0, 
                'tip span': 0.96, 
                'group name': 'RH wingbox',
                'root rib axes': 'xz',
                'part tol': 0.01, 
                } 
    