import numpy as np
import math
import matplotlib.pyplot as plt
import csv
import mpld3

cenmetL = [1410, 1400]
cenmetR = [1500, 1500, 1500]
cenmetNotes = "started with 2 Tips on logger, went at 11:35 am on 2-25-2015"

uplmetL = [1255, 1325, 1282, 1318, 1240, 1255, 1280]
uplmetR = [1280, 1315, 1380, 1380, 1246, 1310]
uplmetNotes= "started with 0 Tips on logger, went at 10:00 am on 2-25-2015"

h15metL = [1360, 1415, 1415, 1415]
h15metR = [1500, 1510, 1510, 1510]
h15metNotes = "started with 0 tips on logger, went at 1 pm on 2-25-2015;  \
did not appear to have been calibrated recently"


Cleft = np.mean(cenmetL)
Cright = np.mean(cenmetR)
Ctot = np.mean(cenmetL + cenmetR)
Cstd = np.std(cenmetL + cenmetR)
Cfactor = Ctot/1420.

print """ Mean Left Side of Snow Lysimeter Bucket at CENMET is %s \n
Mean Right Side of Snow Lysimeter Bucket at CENMET is %s \n
Currently CENMET tips at a mean of %s +- %s \n 
If ideal calibration is 1420 mL per tip, multiply CENMET values by %s \n
Notes: %s \n
""" %(Cleft, Cright, Ctot, Cstd, Cfactor, cenmetNotes)

Uleft = np.mean(uplmetL)
Uright = np.mean(uplmetR)
Utot = np.mean(uplmetL + uplmetR)
Ustd = np.std(uplmetL + uplmetR)
Ufactor = Utot/1420.

print """ Mean Left Side of Snow Lysimeter Bucket at UPLMET is %s \n
Mean Right Side of Snow Lysimeter Bucket at UPLMET is %s \n
Currently UPLMET tips at a mean of %s +- %s \n 
If ideal calibration is 1420 mL per tip, multiply UPLMET values by %s \n
Notes: %s \n
""" %(Uleft, Uright, Utot, Ustd, Ufactor, uplmetNotes)

Hleft = np.mean(h15metL)
Hright = np.mean(h15metR)
Htot = np.mean(h15metL + h15metR)
Hstd = np.std(h15metL + h15metR)
Hfactor = Htot/1420.


print """ Mean Left Side of Snow Lysimeter Bucket at H15MET is %s \n
Mean Right Side of Snow Lysimeter Bucket at H15MET is %s \n
Currently H15MET tips at a mean of %s +- %s \n 
If ideal calibration is 1420 mL per tip, multiply H15MET values by %s \n
Notes: %s \n
""" %(Hleft, Hright, Htot, Hstd, Hfactor, h15metNotes)
