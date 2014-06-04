__author__ = 'vincent'

import os
import hashlib

SHOOTERURL = "http://shooter.cn/api/subapi.php"


def get_API_URL():
    return SHOOTERURL


def get_shooter_hash(filepath):
    ret = ''
    try:
        file = open(filepath, "rb")
        fLength = os.stat(filepath).st_size

        for i in (4096, int(fLength / 3) * 2, int(fLength / 3), fLength - 8192):
            file.seek(i, 0)
            bBuf = file.read(4096)
            if i != 4096:
                ret += ";"
            ret = ret + hashlib.md5(bBuf).hexdigest()

    except IOError:
        print "Can not read file" + filepath
    except StandardError:
        print "StandardError"
    finally:
        file.close()
    return ret


