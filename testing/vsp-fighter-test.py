# First attempt at using AFEM to model an internal structure with a zoned mesh
# OML: comes from OpenVSP
# Structural Components: comes from AFEM
# Nodes + Connectivity: comes from AFEM
# Partitioning: using pyNastran (if needed)
# Visualization: write .bdf to .vtk format using conversion script.


# Importing required + useful modules

# general usage modules
import time
import os
import pathlib
import numpy as np

# pyNastran modules
from pyNastran.bdf.bdf import BDF

# AFEM modules
from afem.config import Settings
from afem.geometry import *
from afem.exchange import ImportVSP, StepWrite
from afem.oml import Body
from afem.structure import *
from afem.topology import *
# from afem.graphics import Viewer # If I can get the WSL2 gui apps working, then uncomment

Settings.log_to_console()

def build_VSP_wingbox(wing, params):

    # This creates an assembly to store parts in
    wingboxAssem = GroupAPI.create_group('wingbox-group')
    
    
    # COME BACK TO THIS IF OPENVSP MAPPING DOES NOT WORK WELL. 
    
    