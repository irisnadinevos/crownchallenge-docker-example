# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import random
import string
from pathlib import Path

import SimpleITK as sitk

project_dir = Path('__file__').parent.absolute().parent.absolute()
input_dir = project_dir / 'input'
output_dir = project_dir / 'output crownchallenge/TeamName1_task1'


def random_classification(image):
    output_anterior = random.choice(string.ascii_letters)
    output_posterior = random.choice(string.ascii_letters)

    return output_anterior, output_posterior


def save_json(save_name, output_anterior, output_posterior):
    output_dict = {'Anterior class': output_anterior, 'Posterior class': output_posterior}

    with open(save_name, mode='w', encoding ='utf8') as json_file:
        json.dump(output_dict, json_file, indent=4)


def main():
    image = sitk.ReadImage(input_dir / '3D_TOF_MRA.nii.gz')
    output_ant, output_pos = random_classification(image)
    save_json(output_dir / 'result_Lippert.json', output_ant, output_pos)


if __name__ == '__main__':
    main()
