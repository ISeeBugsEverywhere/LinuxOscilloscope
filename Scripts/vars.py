from .console_log import ConsoleLog


def console(*args, debug=False):
    """
    Prints an output into console(/tty) with proper formatting
    """
    cc = ""
    for i in args:
        cc = cc + str(i)
    ConsoleLog(cc, level='info', show_caller=True, show_timestamp=False, debug=debug)