# UC Berkeley Stat 159/259 Fall 2015
## Project-Theta

[![Build Status](https://travis-ci.org/berkeley-stat159/project-theta.svg?branch=master)](https://travis-ci.org/berkeley-stat159/project-theta?branch=master)
[![Coverage Status](https://coveralls.io/repos/berkeley-stat159/project-theta/badge.svg?branch=master)](https://coveralls.io/r/berkeley-stat159/project-theta?branch=master)

_**Group members:**_ Siyao Chang ([`changsiyao`](https://github.com/changsiyao)) , Boying Gong ([`boyinggong`](https://github.com/boyinggong)), Benjamin Hsieh ([`BenjaminHsieh`](https://github.com/BenjaminHsieh)), Brian Qiu ([`brianqiu`](https://github.com/brianqiu)), Jiang Zhu ([`pigriver123`](https://github.com/pigriver123))

_**Topic:**_ [The Neural Basis of Loss Aversion in Decision Making Under Risk] (https://openfmri.org/dataset/ds000005/)
[SOME SUMMARY OF PAPER]

## Instructions

- `make all` will generate everything related to the analyses. It will pull in and validate data inside the data directory, create images saved inside the results directory, move relevant images to the paper/figures subdirectory, and generate the final report report.pdf inside the paper directory. The process can take a very long time as the data is over 16 GB and the analyses take a while as well. To save time one can view the final report without running this command by going to the paper directory and running make all from there since the needed figures are already preloaded there. 
- `make clean` will delete extraneous files created by our scripts
- `make coverage` will check the coverage of our data, code directories 
- `make test` will run the tests in our code/utils/tests and code/data/tests directory
- `make verbose` is the verbose version of 'make test'


## Directories

- `code` contains the functions and scripts for analysis and graphing
- `data` holds the relevant datasets that are pulled in and validated either through make commands there or make all here.
- `paper` contains the final report, report.pdf, once the appropriate make commands are run, either here or in paper. It also has the relevant figures for the paper
- `requirements.txt` is the a text file listing the required package versions 
- `tools` contains the material related to travis ci
