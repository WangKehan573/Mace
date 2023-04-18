

import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)   
        filenumber=len(pathDir)
        rate=1
        picknumber=int(filenumber*rate) 
        sample = random.sample(pathDir, picknumber)  
        print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return

if __name__ == '__main__':
	fileDir = "./for_mace/"    
	tarDir = './trainset/'    
	moveFile(fileDir)

