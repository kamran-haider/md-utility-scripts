## md-utility-scripts
Some useful scripts for post-processing molecular dynamics results. 
# *mean_volume_frame.py*
This works only for Desmond trajectories. You can use this when you have run an NPT equilibration and wish to start a production run from a configuration that corresponds to the mean volume. As NPT run would generate a distribution of volumes for your system, obtaining mean volume is straightforward. The script will obtain the frame that has the least squared difference from the mean and will write that into a cms file which you can use for production run. 
You can also discard initial equilibration data by specifying its length in picoseconds.
Ideally, a statistically rigorous way of detecting eqilibrated region should be used to do this. 

# Requirements
* Desmond installation 
* "$SCHRODINGER" environment variable should be set to desmond installation

Type $SCHRODINGER/run mean_volume_frame.py --help for instructions on how to use this. 