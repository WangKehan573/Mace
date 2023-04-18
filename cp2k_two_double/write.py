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

# load model



r = np.load('600K.npz', allow_pickle = True)

E, F, R, Z, Cell = r['E'], r['F'], r['R']

        
  
#lattice = "Lattice=\"%f %f %f %f %f %f %f %f %f\""%(Cell[0],0,Cell[1],0,0,0,Cell[2])


for i in range(2000):
  print(i)
    
  lattice = "Lattice=\"%f %f %f %f %f %f %f %f %f\""%(Cell[i,0],0,0,0,Cell[i,1],0,0,0,Cell[i,2])
 
  
  
  force = F[i]
  energy = E[i]
  numbers= Z
  positions= R[i]
  cell = Cell[i]
  path = 'set/'+str(i)+'.xyz'
  fout = open (path, 'w')
  
  force,positions,energy  = np.array(force), np.array(positions), float(energy)
  
  
  xyz = ""

  
  

  for  i  in range(280):
    



      if int(numbers[i]) == 42:
        token = 'Mo'
      elif int(numbers[i]) == 16 :
        token = 'S'
      else:
        token = 'H'
      
      xyz = xyz+"%s %s %s %s"%(token,positions[i][0],positions[i][1],positions[i][2])+" %s %s %s"%(force[i][0],force[i][1],force[i][2])+'\n'

    
    
  
  fout.write('280'+'\n')
  fout.write("energy="+str(energy)+" ")

  fout.write (lattice+" Properties=species:S:1:pos:R:3:forces:R:3")
  fout.write(' pbc="T T F"\n')

  
  fout.write(xyz)
  xyz = ""
  
  
