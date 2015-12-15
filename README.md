# UC Berkeley Stat 159/259 Fall 2015
## Project-Theta

[![Build Status](https://travis-ci.org/berkeley-stat159/project-theta.svg?branch=master)](https://travis-ci.org/berkeley-stat159/project-theta?branch=master)
[![Coverage Status](https://coveralls.io/repos/berkeley-stat159/project-theta/badge.svg?branch=master)](https://coveralls.io/r/berkeley-stat159/project-theta?branch=master)

_**Group members:**_ Siyao Chang ([`changsiyao`](https://github.com/changsiyao)), 
Boying Gong ([`boyinggong`](https://github.com/boyinggong)), 
Benjamin Hsieh ([`BenjaminHsieh`](https://github.com/BenjaminHsieh)), 
Brian Qiu ([`brianqiu`](https://github.com/brianqiu)), 
Jiang Zhu ([`pigriver123`](https://github.com/pigriver123))

_**Topic:**_ [The Neural Basis of Loss Aversion in Decision Making Under Risk]
(https://openfmri.org/dataset/ds000005/)

The original Science paper found 
[here](https://www.sciencemag.org/content/315/5811/515.abstract) was written by 
Sabrina M. Tom, Craig R. Fox, Christopher Trepel, and Russell A. Poldrack at 
UCLA. The main aim is to identify regions of brain related to loss aversion in 
decision making (in this case a gambling task of 50/50 chance of gaining/lossing
money) and investigate the behavorial and neural correlates of loss aversion. 
In our project we aim to recreate a subset of the paper results with the goal 
of of checking model assumptions, creating analysis pipelines of fMRI research, 
and comparing results with Tom's (et al) paper. Please see paper report in 
`project-theta/paper` for further discussion.  

## Instructions

To generate paper please navigate to `paper` directory and `make all`. 
Follow the instructions below to reproduce/update analyses figures.

### Steps to run all analyses:
 
__Note__: These steps, in particular `make all`, can take dozens of hours due 
to the size and nature of the analyses. We do not recommend running it but 
instead follow the instructions below __Alternate Steps__ for specific desired 
results. 

- `make resultfolder` will generate the results folder `project-theta/results`
to save all analysis output and figures generated from running scripts. Please 
note that this folder will be git ignored (exist on local repository). *If 
one decides to `make all` or run any analyses in `scripts`,  
run this command beforehand.* 
- `make all` will generate everything related to the analyses. It will pull in 
and validate data inside the data directory, create images saved inside the 
results directory, move relevant images to the paper/figures subdirectory, and 
generate the final report report.pdf inside the paper directory. The process 
can take a VERY long time as the data is over 16 GB and the analyses take quite 
a while as well. To save time one can view the final report without running 
this command by going to the paper directory and running make all from there 
since the needed figures are already preloaded there. 

### Alternate steps for analyses:

- First, `make data` to download, unzip, and validate data, saving datasets 
to the data directory. *Note: Run time around 30 minutes*.
- Second, `make resultfolder` to initialize analyses output directory.  
- Navigate to `code/scripts` and run the specific desired analysis.
- Navigate to `code` directory and `make paperfig` to update paper 
figures
- Navigate to `paper` directory and `make all` to generate paper. 

### Other Utility Commands:

- `make clean` will delete extraneous files created by our scripts
- `make coverage` will check the coverage of our data, code directories 
- `make test` will run the tests in our `code/utils/tests` and `code/data/tests` 
directory
- `make verbose` is the verbose version of 'make test'

## Directories

- `code` contains the functions and scripts for analysis and graphing
- `data` holds the relevant datasets that are pulled in and validated either 
through make commands there or make all here.
- `paper` contains the final report, report.pdf, once the appropriate make 
commands are run, either here or in paper. It also has the relevant figures for 
the paper.
- `slides` contain our presentation slides used in class (Stat 159/259).
- `requirements.txt` is the a text file listing the required package versions. 
- `tools` contains the material related to travis ci.

## Acknowledgments

Many thanks to Jarrod Millman, Matthew Brett, J-B Poline, and Ross Barnowski 
for their advice and efforts that made this project possible. 