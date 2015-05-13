import numpy as np
import sys

from schrodinger.trajectory.desmondsimulation import create_simulation
import optparse, sys
from optparse import OptionParser

_usage=("$SCHRODINGER/run mean_volume_frame.py -e .ene file -c cms file -t trajectory folder -l length of initial data to exclude\n"
        "Accepts .cms files along with desmond trajectory and writes a .cms file corresponding to the frame with system volume nearest to the mean.")
_version = '$Revision: 1.0 $'


parser = OptionParser()
parser.add_option("-c", "--cms_file", dest="cms_file", type="string", help="input cms file for NPT equilibration MD run.")
parser.add_option("-t", "--desmond_trajectory", dest="trj", type="string", help="trajectory path")

(options, args) = parser.parse_args()

dsim = create_simulation(options.cms_file, options.trj)
print "Total number of frames: ", dsim.total_frame
