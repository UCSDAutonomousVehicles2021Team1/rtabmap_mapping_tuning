import os
import subprocess
import glob
import numpy as np

def move_data(rawdir, posedir):
	"""
	>>> posedir = "data/poses/"
	>>> os.path.isfile(posedir+'param1_gt.txt')
	True
	>>> os.path.isfile(posedir+'param2_gt.txt')
	True
	>>> os.path.isfile(posedir+'param1_slam.txt')
	True
	>>> os.path.isfile(posedir+'param1_odom.txt')
	True
	"""
	for file in set(np.apply_along_axis(lambda x: x[0][:x[0].find('_')], 0, np.array([os.listdir(rawdir)]))):
		os.makedirs(posedir, exist_ok = True)
		mv_dir_gt = subprocess.call(["cp", os.path.join(rawdir + '/' + file + '_gt.txt'), posedir])
		mv_dir_slam = subprocess.call(["cp", os.path.join(rawdir + '/' + file + '_slam.txt'), posedir])
		mv_dir_odom = subprocess.call(["cp", os.path.join(rawdir + '/' + file + '_odom.txt'), posedir])
		mv_dir_yaml = subprocess.call(["cp", os.path.join(rawdir + '/' + file + '.yaml'), posedir])
