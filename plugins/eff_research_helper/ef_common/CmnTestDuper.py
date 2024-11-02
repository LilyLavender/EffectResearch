# ChatGPT-made program to duplicate found P_CmnTest folders from P_CmnTest1-12

import os
import shutil

current_dir = os.getcwd()

folder_name = None
for i in range(1, 13):
    possible_folder = f'P_CmnTest{i}'
    if os.path.exists(os.path.join(current_dir, possible_folder)):
        folder_name = possible_folder
        break

if not folder_name and os.path.exists(os.path.join(current_dir, 'P_CmnTest')):
    folder_name = 'P_CmnTest'

if folder_name:
    for i in range(1, 13): 
        new_folder_name = f'P_CmnTest{i}'
        new_folder_path = os.path.join(current_dir, new_folder_name)

        if not os.path.exists(new_folder_path):
            shutil.copytree(os.path.join(current_dir, folder_name), new_folder_path)
            print(f'Created: {new_folder_name}')

    if folder_name == 'P_CmnTest' and os.path.exists(os.path.join(current_dir, 'P_CmnTest')):
        shutil.rmtree(os.path.join(current_dir, 'P_CmnTest'))
        print('Deleted: P_CmnTest')
else:
    print('No P_CmnTest or P_CmnTest1 to P_CmnTest12 folder found in the current directory.')
