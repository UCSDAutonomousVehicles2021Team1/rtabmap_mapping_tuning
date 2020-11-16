import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns





def main_eda(files, indir, outdir, **kwargs):
    dfs = []
    for file in files:
        if file.endswith('txt'):
            dfs.append( pd.read_csv(file, header=None, sep=" ").rename(columns={0:'timestamp', 
                   1:'x', 
                   2:'y', 
                   3:'z', 
                   4:'r_x', 
                   5:'r_y', 
                   6:'r_z',
                   7:'r_w'}))
    for df in dfs:
        print(df.head())
    