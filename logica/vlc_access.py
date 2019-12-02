import os


def vlcAccess(vlcpath, randomplaylist):

    try:
        os.system('/snap/bin/vlc')
    except OSError:
        print('System cannot find the specified path')
    else:
        pass

    return os.popen(vlcpath + randomplaylist)


