import os
import spiceypy as spice
from datetime import datetime

#Define our kernels path
kernelsPath = os.path.join(os.path.dirname(os.getcwd()), "kernels")

#Define the path to the leap second kernel
leapSecondsKernelPath = os.path.join(kernelsPath, "naif0012.tls")

#Load the leap second kernel
spice.furnsh(leapSecondsKernelPath)

#Define 'now'
now = str(datetime.now())
print(now)

#Convert it to ET
nowET = spice.str2et(now)
print(nowET)

#Define the path to the solar system ephemeris kernel
solarSystemEpheremisKernelPath = os.path.join(kernelsPath, "de405.bsp")

#Load the kernel
spice.furnsh(solarSystemEpheremisKernelPath)

#Define frames : target=earth, observer=sun
target = "EARTH"
observer = "SUN"
reference = "J2000"

#Get earth positions
earthPositions = spice.spkpos(target, nowET, reference, 'NONE', observer)
print(earthPositions)

#Unload kernels
spice.kclear()
