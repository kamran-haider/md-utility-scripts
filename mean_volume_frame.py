import numpy as np
import sys

from schrodinger.trajectory.desmondsimulation import create_simulation
import optparse, sys
from optparse import OptionParser

_usage=("$SCHRODINGER/run mean_volume_frame.py -e .ene file -c cms file -t trajectory folder -l length of initial data to exclude\n"
        "Accepts .cms files along with desmond trajectory and writes a .cms file corresponding to the frame with system volume nearest to the mean.")
_version = '$Revision: 1.0 $'


parser = OptionParser()
parser.add_option("-e", "--ene_file", dest="ene_file", type="string", help=".ene file from an NPT equilibration MD run.")
parser.add_option("-c", "--cms_file", dest="cms_file", type="string", help="input cms file for NPT equilibration MD run.")
parser.add_option("-t", "--desmond_trajectory", dest="trj", type="string", help="trajectory path")
parser.add_option("-l", "--exclude_region", dest="exclude_region", type=float, help="Initial duration of trajectory to exclude from calculation (ps).")

(options, args) = parser.parse_args()
ene_data = open(options.ene_file, "r").readlines()
traj_data = {}

print "WARNING: Current version of the script assumes that both energies and coordinates are stored at the same time interval."

#FIXME use a more robust way of skipping header of ene file
print "Reading data from ene file..."
for l in ene_data[10:]:
    #print l
    float_converted_data = [float(x) for x in l.strip("\n").split()[1:]]
    traj_data[l.strip("\n").split()[0]] = float_converted_data

vol_list = []
print "Calculating distribution of volumes from the trajectory excluding first %.1f picosecond" % options.exclude_region
for k in traj_data.keys():
  #print k, traj_data[k][7]
  if float(k) > options.exclude_region:
    vol_list.append(traj_data[k][7])

mean_vol = np.mean(np.asarray(vol_list))
sd_vol = np.std(np.asarray(vol_list))
print "Mean system volume is %.2f with fluctuations %.3f" % (mean_vol, sd_vol)
chemical_time_of_frame = 0
"WARNING: Current version of the script assumes that both energies and coordinates are stored at the same time interval."
min_diff = 999999999
for k in traj_data.keys():
  #print k, traj_data[k][7]
  if float(k) > options.exclude_region:
    frame_vol = traj_data[k][7]
    if abs(frame_vol - mean_vol) < min_diff:
      min_diff = abs(frame_vol - mean_vol)
      #print k, int((float(k)/1002)*1000), frame_vol, min_diff
      chemical_time_of_frame = int((float(k)/1002)*1000)
print "The frame corresponding to mean volume %i, writing into a cms file ..." % chemical_time_of_frame
dsim = create_simulation(options.cms_file, options.trj)
dsim.cst.writeCms("test_mean_vol_config.cms", dsim.getFrame(chemical_time_of_frame))
