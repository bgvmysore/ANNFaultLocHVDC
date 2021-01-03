from os import walk
import numpy as np

numpdatdir = './uploads/'

cleandatadir = './cleaned_data/faults_current_only/'

allFiles = [f for _, _1, f in walk(cleandatadir) ]
allFiles = allFiles[0]

tdata = []
for fn in allFiles:
    tmp = np.loadtxt(cleandatadir+fn)
    y = float( fn[2:-5] )
    tdata += [[tmp, y]]
    
tdata = np.array(tdata,dtype=object)

savedataname = 'numpydata'
np.save(numpdatdir+savedataname, tdata)