# SatelliteComputation

**Blender Required !!!**
## Required Packages
- bpy
- pylab(matplotlib)
- urllib
- math
- numpy

## Running

    blender --python main.py

If you don't want to start blender and only want to get the raw data
(console + matplotlib) start like this:

    blender --python main.py --background

## code:
Download data from a specific category:

     TLE.download(category)

     example:
     TLE.download("iridium")

Get number of satellites in category:

     TLE.numOfSat(category)

     example:
     TLE.numOfSat("noaa")

Print specific TLE:

     TLE.printTLE(category, satNr)

     example:

Get value from sat in category:

     TLE.get(value, category, satNr)

     example:
     TLE.get("inclination", "argos", 3)

xyz list:

    xyz[satNr][x/y/z][time]
