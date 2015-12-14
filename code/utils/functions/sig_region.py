"""
    This is a utility function for finding significant p-values in a 3-d brain
    region. Used in genearating scatterplot of correspondence between h
"""
from __future__ import division, print_function
import numpy as np


def stat_region(x1, x2, y1, y2, z1, z2, sig_lv, pgainloss_tst):
    """
    Calculates the number of and mean of all the significant p-values in a 3-d
    brain region of p-values. 
    
    Parameters:
    -----------
    x1, x2: Range of volume x-coordinates (low, high)
    y1, y2: Range of volume y-coordinates (low, high)
    z1, z2: Range of volume z-coordinates (low, high)
    sig_lv: p-value significant cutoff, double
    pgainloss_tst: 3-d array of gain_loss p-value  
    
    Returns:
    --------
    - Number of significant coordinate p-values, double
    - Mean significant p-value of region, double
    
    """
    cordn2d = np.array(np.where(pgainloss_tst[x1:x2, y1:y2, z1:z2] <= sig_lv)).transpose()
    cordn2d[:, 0] = cordn2d[:, 0] + x1
    cordn2d[:, 1] = cordn2d[:, 1] + y1
    cordn2d[:, 2] = cordn2d[:, 2] + z1
    meansig = np.empty(cordn2d.shape[0])
    # Find significant p-values
    for i in np.arange(cordn2d.shape[0]):
        meansig[i] = pgainloss_tst[cordn2d[i, 0], cordn2d[i, 1], cordn2d[i, 2]]
    return cordn2d.shape[0], np.mean(meansig)
