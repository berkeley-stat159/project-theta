## Code Overview

The code folder contains two subdirectories. Utils contains our functions for 
analysis, our functions for graphing, and our tests. Scripts contains the 
scripts that utilize these functions. 

## Data Analysis

**KEY STEP** If you have not already done so, please first create the local 
results directory by nagivating to `project-theta` and running `make resultfolder` 

The following make commands perform an exhaustive analysis for all subjects. 
For those strictly interested in our paper results figures, also run `make 
paperfig` to update the figures used in paper.

- `make all`: Performs all data analysis, generating the intermediate text file
saves and all figures (exhaustive) accross all subjects. **WARNING** Due to large
data size and exhaustive analysis of the mixed effects model, this may more than 
a 1 day. Please run with caution! For updating individual analysis. We recommend 
nagivating to `project-theta/code/scripts` and running the respective make 
commands. 

- `make paperfig`: Moves any (updated) figures strictly related to paper 
results to `project-theta/paper/figures` for inclusion in final paper/slides. 

Other utility make commands include: `clean`, `test`, `verbose` and `coverage`:

- `make test`: Runs function tests in utils/tests on functions that are 
associated with analyzing the data (in utils/functions).
- `make verbose`: Verbose version of `make test`.
- `make clean`: Cleans for temporary files generate by script runs or test runs.
- `make coverage`: Generates a coverage report of functions used in analysis.

# Additional Documentation

Additional documentation and information on the subdirectories can 
be found in their respective READMEs. 

- `scripts`: Script to run analysis. 
- `utils/functions`: User-defined functions used in analysis 
- `utils/graphing`: User-defined graphing functions used in analysis. 
- `utils/tests`: Test files for the user-defined functions. 

## Note on Saved Results:

The exhaustive results, including all figures and intermediate results files, 
are saved in a local, untracked directory `project-theta/results` initailized 
by running the make command `make resultfolder` from `project-theta` directory. 
All paper figures are saved in `project-theta/paper/figures`, which also caches the 
figures required slides. These figures can be updated by running `make paperfig`.
