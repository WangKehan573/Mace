from ase import Atoms
import torch
import torchmetrics
import schnetpack as spk
import schnetpack.transform as trn
import pytorch_lightning as pl
import os
import matplotlib.pyplot as plt
import numpy as np
from schnetpack.data import ASEAtomsData,AtomsDataModule
import ase



        
        
  
lattice = "Lattice=\"%f %f %f %f %f %f %f %f %f\""%(15.92720863,0,0,-7.963415974, 13.79347811 ,0,0,0,13.22380977 )
f = np.load('1.npz',allow_pickle = True)

for i in range(1000):
  print(i)

  
  
  
  energy = f['E'][i]#*27.2114
  numbers= f['z']
  positions= f['R'][i]
  path = 'for_mace/'+str(i)+'.xyz'
  fout = open (path, 'w')
  #print(len(numbers))
  positions,energy =  np.array(positions), float(energy)
  force = np.random.randn(73,3)
  force = np.around(force,3)
  xyz = ""

  
  

  for  j  in range(73):
    



      if int(numbers[j]) == 42:
        token = 'Mo'
      elif int(numbers[j]) == 16:
        token = 'S'
      else:
        token = 'H'
      
      xyz = xyz+"%s %s %s %s"%(token,positions[j][0],positions[j][1],positions[j][2])+" %s %s %s"%(force[j][0],force[j][1],force[j][2])+'\n'

    
    
  
  fout.write('73'+'\n')
  fout.write("energy="+str(energy)+" ")

  fout.write (lattice+" Properties=species:S:1:pos:R:3:forces:R:3")
  fout.write(' pbc="T T T"\n')

  
  fout.write(xyz)
  xyz = ""
  
