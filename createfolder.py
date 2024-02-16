# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:22:12 2024

@author: nilah
"""

import os

base_dir = '/data/nnair/datasetbias/sisfall/prepros/'

def create_folder():
    for i in range(1,34):
        folder = 'exp' + str(i)
        path = os.path.join(base_dir, folder)
        os.makedir(path)
        path2 = os.path.join(path, 'sequences_train')
        os.makedir(path2)
        path3 = os.path.join(path, 'sequences_test')
        os.makedir(path3)
        path4 = os.path.join(path, 'sequences_val')
        os.makedir(path4)
    return 
        
        
if __name__ == '__main__':
    create_folder()
    print('done')