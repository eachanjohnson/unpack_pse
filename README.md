# unpack_pse
Python script for extracting Protein Data Bank (PDB) files from a PyMOL session (PSE) file.

# Requirements
1. UNIX / Linux / MacOS X
2. Python 2.7
3. PyMOL
4. Ability to 'cd' in the Terminal

# How to use
1. Put the unpack_pse.py file in the directory containing the PSE files you want to unpack (the working directory), or in your $PATH.
2. In the Terminal, cd to the working directory, and do "python unpack_pse.py".
3. The script will create a new directory for each PSE containing the PDB files corresponding to the objects in that PSE.
