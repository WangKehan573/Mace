# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:38:49 2023

@author: kehan.wang
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:46:30 2022

@author: kehan.wang
"""


import pandas as pd
import glob
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import os

STRUCTURES_ISIF3 =  ["cp2k_testset"]
def readTxt1(filename,num):
    data = []
    with open(filename,"r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            #print(line)
            line = line.split()
            if len(line) == num:                
                data.append(line)


    return data
 


filename = 'MoS2-pos-1.xyz'
print(filename)

list1 = readTxt1(filename, 4)  #coordinate
list2 = readTxt1(filename, 9)  #energy
print(list2[-1])#,list2)

name = ['element','xu','yu','zu']
table = pd.DataFrame(columns=name,data=list1)
num = int(table.shape[0]/2001)
#print(list(table.columns))
print(table.shape[0]/2001)

R_atom = np.zeros((2000,num,3))
Energy = np.zeros((2000,1))


table = np.array(table)                 
R_table =  table[0:num]

z_atom = []  
for i in range(73):  
    if  list1[i][0] == 'Mo':     
        z_atom.append(42) 
    elif list1[i][0] == 'S':
        z_atom.append(16)
    else:
        z_atom.append(1)








for j in range(1,2001):
        i = int(j - 1)  
        print(i,j)
        R_table = table[(j-1)*num:j*num]     
        
        R_atom[i] = R_table[:,1:]
        Energy[i] = np.array([list2[j-1][-1]])
print(R_atom[-1],Energy[-1]) 
    
    
output_name = '600K.npz'
np.savez(output_name, R = R_atom, E = Energy, z = z_atom)
r = np.load(output_name,allow_pickle=True)  
print(r.files) #
print(len(r["R"])) 
print((r["E"])) 
print((r["z"])) 
