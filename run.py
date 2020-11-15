import sys
import json

sys.path.insert(0, 'src')
from etl import convert_data
# from eda import generate_stats
# from utils import convert_notebook



def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))
    tuning_config = json.load(open('config/tuning-params.json'))
    generate_config = json.load(open('config/generate-params.json'))

    if 'data' in targets:
        convert_data(**data_config)

#     if 'eda' in targets:

#         try:
#             data
#         except NameError:
#             data = pd.read_csv(data_config['data_fp'])

#         generate_stats(data, **eda_config)
        
#         # execute notebook / convert to html
#         convert_notebook(**eda_config)


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)