import os
import subprocess
import glob
import pandas as pd


def convert_data(rawdir, posedir):
    for file in os.listdir(rawdir):
        current_db = os.path.join(rawdir, file)
        mv_dir_gt = subprocess.call(["mv", os.path.join(rawdir + '/' + file[:-3] + '_gt.txt'), posedir])
        mv_dir_slam = subprocess.call(["mv", os.path.join(rawdir + '/' + file[:-3] + '_slam.txt'), posedir])
        mv_dir_odom = subprocess.call(["mv", os.path.join(rawdir + '/' + file[:-3] + '_odom.txt'), posedir])
                                     