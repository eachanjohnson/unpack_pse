#!/usr/bin/env python

import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI

import sys, time, os, subprocess
import pymol

pymol.finish_launching()

# Get list of pse files in the directory
files = [file for file in subprocess.check_output(['ls']).split('\n') if file[-4:] == '.pse']

for file in files:

	# Make a new directory for each pse file's pdbs
	subprocess.call(['mkdir', file.split('.pse')[0]])

	# Clear pymol
	pymol.cmd.reinitialize()
	time.sleep(0.5)

	# Load the file in pymol
	pymol.cmd.load(file)

	# Get the list of objects
	objects = pymol.cmd.get_names('all')

	# Save each one as pdb
	for object in objects:
		pymol.cmd.save('./{}/{}.pdb'.format(file.split('.pse')[0], object), '{}'.format(object))

pymol.cmd.quit()

quit()
