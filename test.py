# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:50:56 2024

@author: nilah
"""

def test():
    '''
    SUBJECT= ['SA01', 'SA02', 'SA03', 'SA04', 'SA05', 'SA06', 'SA07', 'SA08', 'SA09', 'SA10', 'SA11', 'SA12', 
               'SA13', 'SA14', 'SA15', 'SA16', 'SA17', 'SA18', 'SA19', 'SA20', 'SA21', 'SA22', 'SA23', 'SE01', 'SE02',
               'SE03', 'SE04', 'SE05', 'SE06', 'SE07', 'SE08', 'SE09', 'SE10', 'SE11', 'SE12', 'SE13', 'SE14', 'SE15']
    train_ids= ['SA01','SA06', 'SA09', 'SA22']
    test_ids=[]
    for i in SUBJECT:
        if i not in train_ids:
            test_ids.append(i)
    print(test_ids)
    '''
    sub_list= {'SA01':1, 'SA02':2, 'SA03':3, 'SA04':4, 'SA05':5, 'SA06':6, 'SA07':7, 'SA08':8, 'SA09':9, 'SA10':10, 'SA11':11, 'SA12':12, 
               'SA13':13, 'SA14':14, 'SA15':15, 'SA16':16, 'SA17':17, 'SA18':18, 'SA19':19, 'SA20':20, 'SA21':21, 'SA22':22, 'SA23':23, 'SE01':24, 'SE02':25,
               'SE03':26, 'SE04':27, 'SE05':28, 'SE06':29, 'SE07':30, 'SE08':31, 'SE09':32, 'SE10':33, 'SE11':34, 'SE12':35, 'SE13':36, 'SE14':37, 'SE15':38}
    
    train_ids=[]
    for i in [24,28,29,30,32,35,36,37]:
        x = [sub_list for sub_list, v in sub_list.items() if v == i][0]
        train_ids.append(x)
    print(train_ids)
    
    
    
    return

if __name__ == "__main__":
    test()
    print('done')