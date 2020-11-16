import os
import subprocess
import glob
import pandas as pd


def convert_data(rawdir, mapdir, posedir):
    print(glob.glob(rawdir))
#     subprocess.call(["rtabmap-report", "--poses" rtabmap.db])
    print(rawdir, mapdir, posedir)