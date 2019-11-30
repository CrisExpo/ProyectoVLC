import os


def vlcAccess(vlcPath, list):
    try:
        f = exec(vlcPath)
    except OSError:
        print('System cannot find the specified path')
    else:
        pass

    return os.popen(vlcPath + " " + list)