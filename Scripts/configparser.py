import configparser

file = "Config/config.cfg"

cp = configparser.ConfigParser()

def get_last_path():
    cp.read(file)
    section = "SAVEPATH"
    path = cp[section]["path"]
    return path
    pass

def get_last_ips():
    """
    Gets last used ip's, ina array (list)
    :return:
    """
    cp.read(file)
    section = "SAVEPATH"
    ips = cp[section]["ips"]
    return ips.split(',')
    pass

def set_last_ips(ips):
    section = "SAVEPATH"
    cp[section]["ips"] = ips
    # cp[section]["ip"] = ip
    with open(file, 'w') as cfg:
        cp.write(cfg)

def save_last_path(path):
    section = "SAVEPATH"
    cp[section]["path"] = path
    # cp[section]["ip"] = ip
    with open(file, 'w') as cfg:
        cp.write(cfg)