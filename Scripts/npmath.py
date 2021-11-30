#!/usr/bin/python3

import numpy as np
import pyqtgraph
import pyqtgraph.exporters
import os, sys

def do_math_on_arrays(y, expr):
    # y = np.asarray(arr) #
    ret = eval(expr)
    return ret

def get_eq_mode(s):
    if len(s) > 0:
        return True
    else:
        return False


def get_mod_array(np_x,np_y, zero, equation):
    """

    :param np_x: np array
    :param np_y: np array
    :param zero: True, False
    :param equation: string
    :return:
    """
    if zero and equation:
        idxs = np_x < 0.0
        npay = np_y[idxs]
        av = np.average(npay[:int(0.9 * len(npay))])
        yy = do_math_on_arrays((np_y-av), equation)
        return np_x, yy
    elif zero:
        idxs = np_x < 0.0
        npay = np_y[idxs]
        av = np.average(npay[:int(0.9 * len(npay))])
        return np_x, np_y-av
    elif equation:
        yy = do_math_on_arrays(np_y, equation)
        return np_x, yy
    else:
        return np_x, np_y


