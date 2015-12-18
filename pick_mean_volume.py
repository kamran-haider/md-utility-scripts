import numpy as np
import sys
from schrodinger.trajectory.desmondsimulation import create_simulation
#import schrodinger.infra.mm as mm
#import copy
#from schrodinger.structure import StructureWriter, Structure

"""
fs = framesettools.FrameSet(sys.argv[1])
print "myframeset has", len(fs), "frames from time", fs.times()[0], "to", fs.times()[-1]
# assumes a normal WRAPPED_V_2 Desmond trajectory
for frame in fs:
    x = frame.POSITION[0:3]
    print " ", frame.CHEMICALTIME, "atom 0 has position", x


"""
ene_data = open(sys.argv[1], "r").readlines()
traj_data = {}

for l in ene_data[10:]:
    #print l
    float_converted_data = [float(x) for x in l.strip("\n").split()[1:]]
    traj_data[l.strip("\n").split()[0]] = float_converted_data

vol_list = []

for k in traj_data.keys():
  #print k, traj_data[k][7]
  if float(k) > 400:
    vol_list.append(traj_data[k][7])

mean_vol = np.mean(np.asarray(vol_list))
print "The mean volume is: ", mean_vol
frame_of_interest = 0
min_diff = 999999999
mean_frame_time = 0
mean_frame_vol = 0
mean_frame_index = 0

for k in traj_data.keys():
  #print k, traj_data[k][7]
  if float(k) > 400:
    frame_vol = traj_data[k][7]
    if (frame_vol - mean_vol)**2 < min_diff:
      min_diff = abs(frame_vol - mean_vol)
      #print k, float(k)/1000, frame_vol, min_diff
      mean_frame_time = k
      mean_frame_index = int(float(k))
      mean_frame_vol = frame_vol
mean_cms_name = "mean_vol_config.cms"
print "Frame %i has the closest volume (%f) to the mean." % (mean_frame_index, mean_frame_vol)
print "Writing frame %i to %s." % (mean_frame_index, mean_cms_name)
dsim = create_simulation(sys.argv[2], sys.argv[3])
dsim.cst.writeCms(mean_cms_name, dsim.getFrame(mean_frame_index))

"""
comp_cts = []
for ffst in dsim.cst.ffsts:
    comp_cts.append(copy.copy(ffst.parent_structure))

oxygen_atids = self._water_oxygen_atoms[0:self._nwater]

atids = self._getCombinedAtids(oxygen_atids)

new_ct = mm.mmct_ct_duplicate(dsim.cst.handle)
full_ct = Structure(new_ct, True )
full_ct = full_ct.extract(atids, copy_props=True)

full_ct.property['s_chorus_trajectory_file'] = trjidx

writer = StructureWriter(name)
writer.append(full_ct)
for ct in comp_cts:
    writer.append(ct)
writer.close()




    comp_cts = []
    for ffst in self._dsim.cst.ffsts:
            if ffst.parent_structure.property['s_ffio_ct_type'] == 'solvent':

                if self._nwater == 0:
                    continue

                # reduce the number of water to self._nwater in solvent ct
                solvent_ct = ffst.parent_structure.copy()
                natoms = self._nwater * self._index_mapper.natoms
                if self._nwater > self._index_mapper.nmols:
                    raise Exception("number of water (%d) to be retained is larger than total number of water %d."%(self._nwater, self._index_mapper.nmols))
                solvent_ct = solvent_ct.extract([x for x in xrange(1, natoms+1)])
                for k in ffst.parent_structure.property.keys():
                    solvent_ct.property[k] = ffst.parent_structure.property[k]

                # handle ffio block
                solvent_ff_handle = mm.mmffio_ff_duplicate(ffst.ff_handle)

                # resize ffpseudo block
                npseudo = mm.mmffio_ff_get_num_pseudos(solvent_ff_handle)
                #for i in xrange(npseudo, 0 , -1):
                for i in xrange(npseudo, solvent_ff_handle-1, -1):
                    mm.mmffio_delete_pseudo(solvent_ff_handle, i)
                # clear restraint block
                nrestraint = mm.mmffio_ff_get_num_restraints(solvent_ff_handle)
                for i in xrange(nrestraint, 0 , -1):
                    mm.mmffio_delete_restraint(solvent_ff_handle, i)
                mm.mmffio_ff_mmct_put(solvent_ff_handle, solvent_ct)
                comp_cts.append(solvent_ct)
            else:
                comp_cts.append(copy.copy(ffst.parent_structure))

        oxygen_atids = self._water_oxygen_atoms[0:self._nwater]

        atids = self._getCombinedAtids(oxygen_atids)

        new_ct = mm.mmct_ct_duplicate(self._dsim.cst.handle)
        full_ct = Structure(new_ct, True )
        full_ct = full_ct.extract(atids, copy_props=True)

        full_ct.property['s_chorus_trajectory_file'] = trjidx

        writer = StructureWriter(name)
        writer.append(full_ct)
        for ct in comp_cts:
            writer.append(ct)
        writer.close()

"""
