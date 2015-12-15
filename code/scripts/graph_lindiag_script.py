import nibabel as nib
import numpy as np
import json
import sys
import os

# Path to function
pathtofunction = '../utils/functions'
pathtofunction2='../utils/graphing'
# Append path to sys
sys.path.append(pathtofunction)
sys.path.append(pathtofunction2)

from graph_lindiagnostics import qqplot, res_var
from behavtask_tr import events2neural_extend, merge_cond
from regression_functions import hrf, getRegressor, calcBeta, calcMRSS, deleteOutliers
from smooth_gaussian import fwhm2sigma, smooth_spatial

# This first part is same as regression_script, except path changes
#------------------------------------------------------------------------------#
n_vols=240
TR=2
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)

os.chdir("../../data")

dvars_out = json.load(open("../results/texts/dvarsOutliers.txt"))
fd_out = json.load(open("../results/texts/fdOutliers.txt"))

# Threshold cutoff from histogram observation
threshold = 400

for i in range(2,3):
    # first three dimension for data shape is 64, 64, 34.
    # create array to store the combined dataset of three runs
    data_full = np.empty([64, 64, 34, 0])
    gain_full = np.empty([0,])
    loss_full = np.empty([0,])
    linear_full = np.empty([0,])
    quad_full = np.empty([0,])
    for j in range(1,4):
        direct='ds005/sub0'+str(i).zfill(2)+'/BOLD/task001_run00'+`j`+'/'
        boldname = direct+'bold.nii.gz'
        img=nib.load(boldname)
        data=img.get_data().astype(float)
        data=smooth_spatial(data)
        run = j
        behav_cond = 'ds005/sub0'+str(i).zfill(2)+'/behav/task001_run00'+`j`+'/behavdata.txt'
        task_cond1 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond001.txt'
        task_cond2 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond002.txt'
        task_cond3 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond003.txt'
        task_cond4 = 'ds005/sub0'+str(i).zfill(2)+'/model/model001/onsets/task001_run00'+`j`+'/cond004.txt'
        parameters = merge_cond(behav_cond, task_cond1, task_cond2, task_cond3, task_cond4)
        neural_prediction = events2neural_extend(parameters,TR, n_vols)
        gain, loss, linear_dr, quad_dr = getRegressor(TR, n_vols, hrf_at_trs, neural_prediction, standard = False)
        data, gain, loss, linear_dr, quad_dr = deleteOutliers(data, gain, loss, i, run, dvars_out, fd_out, linear_dr, quad_dr)
        data_full = np.concatenate((data_full,data),axis=3)
        gain_full = np.concatenate((gain_full,gain),axis=0)
        loss_full = np.concatenate((loss_full,loss),axis=0)
        linear_full = np.concatenate((linear_full,linear_dr),axis=0)
        quad_full = np.concatenate((quad_full,quad_dr),axis=0)
    d_shape = data_full.shape[:3]
    mea=calcMRSS(data_full, gain_full, loss_full, linear_full, quad_full, threshold)
    X, Y, beta=calcBeta(data_full, gain_full, loss_full, linear_full, quad_full, threshold)
#------------------------------------------------------------------------------#
    # Take the 40,000 voxel
    fitted = X.dot(beta[:,40000])
    residuals = Y[:,40000] - fitted
    qqplot(residuals, saveit=True)
    res_var(fitted, residuals, name = 'fitted', saveit=True)
 
   # possibly transform data: 
    X_log, Y_log, beta_log=calcBeta(np.log(data_full+1), gain_full, loss_full, linear_full, quad_full)
    residuals_log = Y_log[:,40000] - X_log.dot(beta_log[:,40000])
    qqplot(residuals_log, saveit=True)
    res_var(X_log.dot(beta_log[:,40000]), residuals_log, name = 'fitted_log',  saveit=True)  
    vox_pos = np.unravel_index(40000, d_shape)
    print("Voxel used: " + str(vox_pos))
    
