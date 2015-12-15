from __future__ import division
import nibabel as nib
import numpy as np
import json
import sys

# Path to function
pathtofunction = '../utils/functions'
# Append path to sys
sys.path.append(pathtofunction)

from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getRegressor, deleteOutliers
from lme_functions import calcBetaLme, calcSigProp, calcAnov, anovStat

#this script produces the values and anova for a linear mixed effects model in txt files

n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)

pathtofolder = '../../data/'

dvars_out = json.load(open("../../results/texts/dvarsOutliers.txt"))
fd_out = json.load(open("../../results/texts/fdOutliers.txt"))

sig_gain_prop = np.empty(16)
sig_loss_prop = np.empty(16)
anov_prop = np.empty(16)
for i in range(1,17):
    # first three dimension for data shape is 64, 64, 34.
    # create array to store the combined dataset of three runs
    data_full = np.empty([64, 64, 34, 0])
    gain_full = np.empty([0,])
    loss_full = np.empty([0,])
    linear_full = np.empty([0,])
    quad_full = np.empty([0,])
    run_count = np.zeros(3)
    for j in range(1,4):
        direct='ds005/sub0'+str(i).zfill(2)+'/BOLD/task001_run00'+`j`+'/'
        boldname = pathtofolder + direct+'bold.nii.gz'
        img=nib.load(boldname)
        data=img.get_data()
        run = j
        behav_cond = pathtofolder + 'ds005/sub0'+str(i).zfill(2)+'/behav/task001_run00'+`j`+'/behavdata.txt'
        task_cond1 = pathtofolder + 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond001.txt'
        task_cond2 = pathtofolder + 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond002.txt'
        task_cond3 = pathtofolder + 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond003.txt'
        task_cond4 = pathtofolder + 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond004.txt'
        parameters = merge_cond(behav_cond, task_cond1, task_cond2, task_cond3, task_cond4)
        neural_prediction = events2neural_extend(parameters,TR, n_vols)
        gain, loss, linear_dr, quad_dr = getRegressor(TR, n_vols, hrf_at_trs, neural_prediction)
        data, gain, loss, linear_dr, quad_dr = deleteOutliers(data, gain, loss, i, run, dvars_out, fd_out, linear_dr, quad_dr)
        run_count[j-1] = data.shape[3]     ## dummy variable indicating the groups
        data_full = np.concatenate((data_full,data),axis=3)
        gain_full = np.concatenate((gain_full,gain),axis=0)
        loss_full = np.concatenate((loss_full,loss),axis=0)
        linear_full = np.concatenate((linear_full,linear_dr),axis=0)
        quad_full = np.concatenate((quad_full,quad_dr),axis=0)
        
    run_group = np.concatenate((np.repeat(1, run_count[0]), 
                                np.repeat(2, run_count[1]), np.repeat(3, run_count[2])), axis=0)
    thrshd = 400 ## set a threshold to idenfity the voxels inside the brain
    print "calculating parameters of subject "+str(i)
    beta = calcBetaLme(data_full, gain_full, loss_full, linear_full, quad_full, run_group, thrshd)
    sig_level = 0.05
    sig_gain_prop[i-1], sig_loss_prop[i-1] = calcSigProp(beta, sig_level)
    write='../../results/texts/sub0'+str(i).zfill(2)+'_lme_beta.txt'
    np.savetxt(write, beta)
    anov_test = calcAnov(data_full, run_group, thrshd)
    anov_prop[i-1] = anovStat(anov_test)

write='../../results/texts/lme_sig_gain_prop.txt'
np.savetxt(write,  sig_gain_prop)
write='../../results/texts/lme_sig_loss_prop.txt'
np.savetxt(write,  sig_loss_prop)
write='../../results/texts/anova_prop.txt'
np.savetxt(write,  anov_prop)

