# import packages
# opensees packages
import openseespy.opensees as ops
import opsvis as ovs
#other packages
import matplotlib.pyplot as plt

#helper functions
from modelUnits import *
from modelFunctions import *
from buildFiberSection import *


# remove older active model
ops.wipe()
ops.model('BasicBuilder', '-ndm', 2, '-ndf', 3) #defines model geometry and DOF per node


#call getmodel function and build the buiding
getModel(buildingID=10, NBay=1, NStory=3, LBeam=4, LCol=4, sectionType='RCFiber', startCoor=(0,0))



# must run gravity analyisis to incorporate dead load effects
runGravityAnalysis(100)
ovs.plot_defo()
plt.show()

setRayleighDamping()

# define earthquake data files
lomaPrietaEq2 = "data/0493a.smc"
lomaPrietaEq = "data/A10000.dat"
casi68Eq = "data/BM68elc.dat"
elcentro = "data/elcentro.txt"

#load data
gmDatacasi68Eq = np.loadtxt(casi68Eq).ravel()

#run analysis
runGroundMotionAnalysis(gmDatacasi68Eq, GM_fact=9.81, dt=0.01)


#you can plot every things