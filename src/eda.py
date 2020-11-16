import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np




def main_eda(files, indir, outdir, **kwargs):
    dfs = []
    for file in files:
        if file.endswith('txt'):
            print(file)
            dfs.append( pd.read_csv(file, header=None, sep=" ").rename(columns={0:'timestamp', 
                   1:'x', 
                   2:'y', 
                   3:'z', 
                   4:'r_x', 
                   5:'r_y', 
                   6:'r_z',
                   7:'r_w'}))
    plot_timestamp(dfs[2], dfs[1], dfs[0])
    plot_xy(dfs[2], dfs[1], dfs[0])
    plot_z(dfs[2], dfs[1], dfs[0])
    plot_r_x(dfs[2], dfs[1], dfs[0])
    plot_r_y(dfs[2], dfs[1], dfs[0])
    plot_r_w(dfs[2], dfs[1], dfs[0])
    plot_r_z_gt(dfs[2])
    plot_r_z_odom(dfs[1])
    plot_r_z_slam(dfs[0])

def plot_timestamp(gt, odom, slam):
    plt.plot(gt['timestamp'].values)
    plt.plot(odom['timestamp'].values)
    plt.plot(slam['timestamp'].values)
    plt.legend(['Ground Truth', 'Odometry', 'SLAM'])
    plt.title("Overlap in timestamps")
    plt.savefig('./results/timestamp.png')
    plt.close()
    
def plot_xy(gt, odom, slam):
    fig, ax = plt.subplots(1, 3, sharex = True, sharey = True)
    ax[0].plot(gt['x'].values, gt['y'].values)
    ax[0].set_title('Ground Truth')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[1].plot(odom['x'].values, odom['y'].values)
    ax[1].set_title('Odometry Path')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')
    ax[2].plot(slam['x'].values, slam['y'].values)
    ax[2].set_title('SLAM Path')
    ax[2].set_xlabel('x')
    ax[2].set_ylabel('y')
    fig.suptitle("X and Y in each path")
    fig.savefig('./results/xy.png')
    plt.close()
    
def plot_z(gt, odom, slam):
    plt.plot(gt['z'].values)
    plt.plot(odom['z'].values)
    plt.plot(slam['z'].values)
    plt.title("Similarity in elavation")
    plt.legend(['Ground Truth', 'Odometry', 'SLAM'])
    avgs = [ np.mean(gt['z'].values), np.mean(odom['z'].values), np.mean(slam['z'].values)]
    df = pd.DataFrame(avgs, columns = ['Average Value of Z'], index = ['Ground Truth', 'Odometry', 'SLAM'])
    plt.savefig('./results/z.png')
    plt.close()
    df.to_csv('./results/z.csv', header=True, index=True)
    
def plot_r_x(gt, odom, slam):
    plt.plot(gt['r_x'].values)
    plt.plot(odom['r_x'].values)
    plt.plot(slam['r_x'].values)
    plt.title("Similarity in pitch")
    plt.legend(['Ground Truth', 'Odometry', 'SLAM'])
    avgs = [ np.mean(gt['r_x'].values), np.mean(odom['r_x'].values), np.mean(slam['r_x'].values)]
    df = pd.DataFrame(avgs, columns = ['Average Value of Rotations X'], index = ['Ground Truth', 'Odometry', 'SLAM'])
    plt.savefig('./results/rx.png')
    plt.close()
    df.to_csv('./results/rx.csv', header=True, index=True)
    
def plot_r_y(gt, odom, slam):
    plt.plot(gt['r_y'].values)
    plt.plot(odom['r_y'].values)
    plt.plot(slam['r_y'].values)
    plt.title("Similarity in yaw")
    plt.legend(['Ground Truth', 'Odometry', 'SLAM'])
    avgs = [ np.mean(gt['r_y'].values), np.mean(odom['r_y'].values), np.mean(slam['r_y'].values)]
    df = pd.DataFrame(avgs, columns = ['Average Value of Rotations Y'], index = ['Ground Truth', 'Odometry', 'SLAM'])
    plt.savefig('./results/ry.png')
    plt.close()
    df.to_csv('./results/ry.csv', header=True, index=True)
    
def plot_r_w(gt, odom, slam):
    plt.plot(gt['r_w'].values)
    plt.plot(odom['r_w'].values)
    plt.plot(slam['r_w'].values)
    plt.title("Similarity in angle of wheel")
    plt.legend(['Ground Truth', 'Odometry', 'SLAM'])
    avgs = [ np.mean(gt['r_w'].values), np.mean(odom['r_w'].values), np.mean(slam['r_w'].values)]
    df = pd.DataFrame(avgs, columns = ['Average Value of Rotations X'], index = ['Ground Truth', 'Odometry', 'SLAM'])
    plt.savefig('./results/rw.png')
    plt.close()
    df.to_csv('./results/rw.csv', header=True, index=True)
    
def plot_r_z_gt(gt):
    plt.plot(gt['y'].values[:15])
    plt.title("Change in direction")
    plt.plot(6, 0,'o')
    plt.savefig('./results/rz_gt.png')
    plt.close()
    
def plot_r_z_odom(odom):
    plt.plot(odom['y'].values[:15])
    plt.title("Change in direction")
    plt.plot(6, 0,'o')
    plt.savefig('./results/rz_odom.png')
    plt.close()

def plot_r_z_slam(slam):
    plt.plot(slam['y'].values[:15])
    plt.title("Change in direction")
    plt.plot(6, 0,'o')
    plt.savefig('./results/rz_slam.png')
    plt.close()
  