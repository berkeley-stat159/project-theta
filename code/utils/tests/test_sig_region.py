"""
Test sig_region module the following functions:
    stat_region

Run with::
    **Run from project-theta directory or code directory  with 'make test'

"""
# Loading modules.
from __future__ import absolute_import, division, print_function
import numpy as np
import sys, os


# Append function path
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

# Load graph_functions:
from sig_region import stat_region

def test_stat_region():
    # Test data (3d)
    t_data = np.reshape(np.arange(64), (4,4,4))
    # Looks like this:
    # array([[[ 0,  1,  2,  3],
    #    [ 4,  5,  6,  7],
    #    [ 8,  9, 10, 11],
    #    [12, 13, 14, 15]],

    #   [[16, 17, 18, 19],
    #    [20, 21, 22, 23],
    #    [24, 25, 26, 27],
    #    [28, 29, 30, 31]],

    #   [[32, 33, 34, 35],
    #    [36, 37, 38, 39],
    #    [40, 41, 42, 43],
    #    [44, 45, 46, 47]],

    #   [[48, 49, 50, 51],
    #    [52, 53, 54, 55],
    #    [56, 57, 58, 59],
    #    [60, 61, 62, 63]]])
    sig_lv = 42.5
    # Get [2:4,1:3,1:4] region
    x1 = 2
    x2 = 4
    y1 = 1
    y2 = 3
    z1 = 1
    z2 = 4
    # Corresponds to:
    # array([[[37, 38, 39],
    #    [41, 42, 43]],

    #   [[53, 54, 55],
    #    [57, 58, 59]]])
    
    # So number less than 42.5 are 37, 38, 39, 41, and 42
    t_num = 5
    t_mean = np.mean([37, 38, 39, 41, 42])
    my_num, my_mean = stat_region(x1, x2, y1, y2, z1, z2, sig_lv, t_data)
    
    # Assert
    assert (t_num == my_num)
    assert (t_mean == my_mean)
