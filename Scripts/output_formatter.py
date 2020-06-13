import sys, os


def get_formatted_array_equal_size(x:list, y:list, channel, x_unit, y_unit):
    rt = []
    rt.append("Time "+str(x_unit)+" , " +str(channel)+str(y_unit))
    lx = len(x)
    ly = len(y)
    if lx > ly:
        diff = lx - ly
        for i in range(0, diff):
            y = y.append("") # ensure equality of array's sizes
    # arrange two lists into one:
    for a in range(0, lx):
        rt.append(str(x[i])+" , "+str(y[i]))
    return rt

def get_formatted_array_equalize(x:list, y:list):
    rt = []
    lx = len(x)
    ly = len(y)
    if lx > ly:
        diff = lx - ly
        for i in range(0, diff):
            y = y.append("") # ensure equality of array's sizes
    # arrange two lists into one:
    for a in range(0, lx):
        rt.append(str(x[i])+" , "+str(y[i]))
    return rt

def get_formatted_lists(x:list, y:list):
    rtt = get_formatted_array_equalize(x,y)
    return rtt
    pass