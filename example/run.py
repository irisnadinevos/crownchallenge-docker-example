import json
from pathlib import Path


project_dir = Path(__file__).parent.absolute().parent.absolute()
input_dir = project_dir / 'input'
output_dir = project_dir / 'output crownchallenge/TeamName1_task1'


def do():
    files = list(input_dir.glob('*.nii.gz'))

    for f in files:
        save_json(f.stem / 'result_Lippert.json')


def save_json(filename):

    data = {'Anterior class': 'g', 'Posterior class': 'h'}
    
    with open(output_dir / filename, mode='w', encoding ='utf8') as json_file:
       json.dump(data, json_file, indent=4)
           
    return
