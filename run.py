import sys
import json
import os

sys.path.insert(0, 'src')
from etl import convert_data
from eda import main_eda
from utils import convert_notebook
from tuning import find_metrics
from generate import create_launch_files
from test import test_data


def main(targets):
    print(targets)
    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))
    tuning_config = json.load(open('config/tuning-params.json'))
    generate_config = json.load(open('config/generate-params.json'))
    test_config = json.load(open('config/test-params.json'))

    if 'data' in targets:
        convert_data(**data_config)

    if 'eda' in targets:
        files = []
        for file in os.listdir(eda_config['indir']):
            files.append(os.path.join(eda_config['indir'], file))

        main_eda(files, **eda_config)
        
#         execute notebook / convert to html
        convert_notebook(**eda_config)
    
    if 'tune' in targets:
        find_metrics(**tuning_config)
        
    if 'generate' in targets:
        create_launch_files(**generate_config)

    if 'test' in targets:
        test_data(**test_config)

if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)

