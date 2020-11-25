from os import listdir
from os.path import isfile, join
import os
import pandas as pd

def test_data(datadir, outdir):
    report = open(r'test_report.txt', 'w+')
    for file in os.listdir(datadir):
        current = os.path.join(datadir, file)
        if current.endswith('db'):
            report.write('RTABMAP DB File Found!\n')
            
        else:
            report.write('RTABMAP DB NOT File Found!\n')

        report.write('\n')
        if current.endswith('txt'):
            df = pd.read_csv(current, sep=' ', header=None)
            report.write('Checking: ' + current + '\n')
            report.write('\n')

            report.write('Checking Number of Columns\n')
            report.write(('Number of Required Columns Needed: 8\n'))
            report.write('Number of Columns Found:'+ str(len(df.columns)) + '\n')
            report.write('\n')
            if len(df.columns) != 8:
                report.write('ERROR\n')
                report.write(current + ' seems to be corrupted and is missing column(s).\n')
            report.write('\n')

            report.write('Checking Column Types...\n')
            counter = 0
            error = 0
            for i in df.dtypes:
                if type(i) == float:
                    counter += 1
                else:
                    error = counter
            if counter == 8:
                report.write('All Columns are the correct types.\n')
            else:
                report.write('ERROR\n')
                report.write('Column ' + str(error) + ' is the wrong type!\n')
            report.write('\n')

    report.close()