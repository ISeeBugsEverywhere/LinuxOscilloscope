def console(*args):
    """
    Prints an output into console(/tty)
    """
    a = args
    cc = ""
    for i in a:
        cc = cc + str(i)
    print(cc+"\n")