# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:22:12 2024

@author: nilah
"""
import os

base_dir = '/data/nnair/datasetbias/mobiact/prepros/'

def create_folder():
    for i in range(1,38):
        folder = 'exp' + str(i)
        path = os.path.join(base_dir, folder)
        try:
            os.mkdir(path)
        except OSError as error:  
            print(error)
        path2 = os.path.join(path, 'sequences_train')
        try:
            os.mkdir(path2)
        except OSError as error:  
            print(error)
        path3 = os.path.join(path, 'sequences_test')
        try:
            os.mkdir(path3)
        except OSError as error:  
            print(error)
        path4 = os.path.join(path, 'sequences_val')
        try:
            os.mkdir(path4)
        except OSError as error:  
            print(error)
    return 
        
        
if __name__ == '__main__':
    create_folder()
    print('done')