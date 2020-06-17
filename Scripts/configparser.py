import configparser

file = "Config/config.cfg"

cp = configparser.ConfigParser()

def get_last_path():
    cp.read(file)
    section = "SAVEPATH"
    path = cp[section]["path"]
    return path
    pass

def save_last_path(path):
    section = "SAVEPATH"
    cp[section]["path"] = path
    # cp[section]["ip"] = ip
    with open(file, 'w') as cfg:
        cp.write(cfg)