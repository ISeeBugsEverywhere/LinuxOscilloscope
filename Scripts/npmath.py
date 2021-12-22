#!/usr/bin/python3

import numpy as np
import pyqtgraph
import pyqtgraph.exporters
import os, sys

def do_math_on_arrays(y, expr):
    # y = np.asarray(arr) #
    # ret = None
    if (len(expr) > 0) and ('y' in expr):
        try:
            ret = eval(expr)
            return ret
        except:
            ret = y
            return ret
    else:
        return y
    # return ret

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


def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)
    pass

def prepend_line_at(file_name, text, index = 0):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    idx = 0
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        # write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            if idx == index:
                write_obj.write(text + '\n')
            write_obj.write(line)
            idx = idx + 1
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)
    pass


def make_xy_header(ss_arr, sigs):
    hdr = ''
    for key, val in sigs.items():
        hdr = hdr + str(key)+'_x,'+str(key)+'_y,'
    header = ''
    for i in ss_arr:
        header = header + 'X_x,'+i.eq+','
    return hdr+header
    pass


