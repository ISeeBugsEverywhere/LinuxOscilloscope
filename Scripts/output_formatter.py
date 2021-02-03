import sys, os


def get_formatted_array_equalize(x:list, y:list):
    """
    returns an array (list) made from two passed lists.
    If x and y lists are in different size, y list will be extended by empty
    spaces until y reaches equal size to x.

    :param x: list
    :param y: list
    :return: list rt (list x + list y)
    """
    rt = []
    lx = len(x)
    ly = len(y)
    if lx > ly:
        diff = lx - ly
        for i in range(0, diff):
            y = y.append("") # ensure equality of array's sizes
    # compact two lists into one:
    for i in range(0, lx):
        rt.append(str(x[i])+" , "+str(y[i])+" , ")
    return rt


def get_oo_dict(_dict:dict):
    _arr = []
    for key, value in _dict.items():
        xy = get_formatted_array_equalize(value[0], value[1])
        _comments = ["%TIME% , %COM"+str(key)+"% , "]
        _f_line = ["Time "+str(value[2])+" , "+ str(key)+" , "]
        _f_line.extend(_comments)
        _f_line.extend(xy)
        _arr.append(_f_line)
    return _arr
    pass

def get_oo_jj(_array:list):
    """
    TODO: not finished
    :param _array:
    :return:
    """
    _l = len(_array) # how many arrays inside?
    _l_array = []
    _oo = []
    for i in range(0, _l):
        _l_array.append(len(_array[i]))
    mx = max(_l_array)
    for i in range(0, mx):
        _string = ""
        for m in range(0, _l):
            _string = _string + str((_array[m][i]))
        _oo.append(_string)
    return _oo

def get_o_d(_d:dict):
    _a = get_oo_dict(_d)
    _o = get_oo_jj(_a)
    return _o