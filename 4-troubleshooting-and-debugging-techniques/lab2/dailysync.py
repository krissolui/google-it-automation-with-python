#!/usr/bin/env python3

import os
import subprocess
from multiprocessing import Pool

home = os.path.expanduser("~")
src = home + "/data/prod/"
dest = home + "/data/prod_backup/"

def backup(name):
    subprocess.call(["rsync", "-arq", name, name.replace(src, dest)])

subdirectories = [f.path for f in os.scandir(src) if f.is_dir()]
pool = Pool(len(subdirectories))
pool.map(backup, subdirectories)
