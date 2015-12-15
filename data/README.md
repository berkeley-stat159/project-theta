## Download/Validate Data

The ds005 dataset, filtered ds005 dataset, and mni templates are stored here. 
THE COMMANDS SHOULD BE DONE IN THIS ORDER to be successfully validated.
The makefile is written such that:
 
- `make data` will download all the appropriate ds005 data, *The Neural Basis 
of Loss Aversion in Decision Making Under Risk*. WARNING: The combined size
will be a total of 16.7 GB, so can take ~30 minutes to download, please plan 
accordingly. 
- `make unzip` will unzip, remove, and rename certain files
- `make validate` will run data.py to check the hashes of each downloaded file 
with a master hashlist included, ensuring all downloaded data is correct  

## Testing

- `make test` will run nosetest on the checking hashes function in data.py
- `make coverage` will generate a coverage report on validating function

## Overview

The ds005 folder contains subfolders for each subject, the most relevant of 
which are:

- BOLD: raw data of fMRI scans for each of the subjects three runs, as well as d
isplacement/variance data 
- behav: file for each run that contains the onsets, potential gains, potential 
losses, and response of each trial
- model: filtered, processed data of fMRI scans for each of the subjects three 
runs, and the onsets files. We thank the NiPy berkeley project for this 
processed data.

The templates folder contains the MNI templates  
