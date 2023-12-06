#
# libraries
#
# system
import os, sys, fileinput
import numpy
# graphics
import seaborn as sns
import matplotlib.pyplot as plt

#
# functions
#

def readOFTwoColumn(dataFile):
    """ 
    read OF two columns files
    """
    
    # Init
    col0 = []
    col1 = []
    
    # Read File
    for line in fileinput.input(dataFile):
        words = line.split()
        if words[0][0] != '#':
            col0.append(float(words[0]))
            col1.append(float(words[1]))
    #
    return col0,col1
    
    


#
# main program
#
sns.set()  # for nice plots : seaborn setup
dataFile       = './postProcessing/surfaceFieldValue-free.dat'
dataFileRockV1 = './postProcessing/surfaceFieldValue-free.dat'

#
time, force       = readOFTwoColumn(dataFile)
timeRV1, forceRV1 = readOFTwoColumn(dataFileRockV1)
#
forceMax     = max(force)
timeForceMax = time[numpy.argmax(force)]

print('Force max [N]:',forceMax)
print('Time force max [s]:',timeForceMax)



#
plt.figure(0)
plt.plot(time, force,linewidth=3,label='free')
plt.plot(timeRV1, forceRV1,linewidth=3,label='rock V1')
plt.xlabel('time [s]',fontsize=14)
plt.ylabel('force [N]',fontsize=14)
plt.title('Water impact force',fontsize=18)
plt.legend(loc='upper right')
plt.tight_layout()
figFile='waterImpactForce.pdf'
plt.savefig(figFile)
plt.show()









