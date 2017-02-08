import bpy              # blender python
from pylab import *     # plot values (matplotlib)
import urllib           # download data
import math             # math: pow(a, b), ...
import numpy as np      # advanced math (multi dim arrays)

# TLE class
class TLE:
    # get value from satellite
    def get(value, category, satNr):
        with open('TLE/' + category + '.txt') as data:
            content = data.readlines()

            if value == "name":
                return content[(satNr)*3][0:15]
            elif value == "LineNumber":
                return content[((satNr)*3)+1][0:1]
            elif value == "Classification":
                return content[((satNr)*3)+1][7:8]
            elif value == "LaunchYear":
                return content[((satNr)*3)+1][9:11]
            elif value == "LaunchNumber":
                return content[((satNr)*3)+1][11:14]
            elif value == "LaunchPiece":
                return content[((satNr)*3)+1][14:17]
            elif value == "EpochYear":
                return content[((satNr)*3)+1][18:20]
            elif value == "EpochDayFraction":
                return content[((satNr)*3)+1][20:32]
            elif value == "EpochDay":
                return content[((satNr)*3)+1][20:23]
            elif value == "EpochTime":
                return content[((satNr)*3)+1][24:32]
            elif value == "FirstTimeDerivative":
                return content[((satNr)*3)+1][33:43]
            elif value == "SecondTimeDerivative":
                return content[((satNr)*3)+1][44:52]
            elif value == "BSTARDragTerm":
                return content[((satNr)*3)+1][53:61]
            elif value == "Num0":
                return content[((satNr)*3)+1][62:63]
            elif value == "ElementSetNumber":
                return content[((satNr)*3)+1][64:68]
            elif value == "Checksum1":
                return content[((satNr)*3)+1][68:69]

            elif value == "LineNumber2":
                return content[((satNr)*3)+2][0:1]
            elif value == "Number2":
                return content[((satNr)*3)+2][2:7]
            elif value == "Inclination":
                return content[((satNr)*3)+2][8:16]
            elif value == "RAAN":
                return content[((satNr)*3)+2][17:25]
            elif value == "Eccentricity":
                return content[((satNr)*3)+2][26:33]
            elif value == "ArgumentOfPerigee":
                return content[((satNr)*3)+2][34:42]
            elif value == "MeanAnomaly":
                return content[((satNr)*3)+2][43:51]
            elif value == "MeanMotion":
                return content[((satNr)*3)+2][52:63]
            elif value == "Revloution":
                return content[((satNr)*3)+2][63:68]
            elif value == "Checksum2":
                return content[((satNr)*3)+2][68:69]

    # downlaod specific categeory
    def download(category):
        webx_loc = 'http://celestrak.com/NORAD/elements/' + category + '.txt'
        disk_loc = 'TLE/' + category + '.txt'
        urllib.request.urlretrieve(webx_loc, disk_loc)

    # get number of satellites in specific ategory
    def numOfSat(category):
        with open('TLE/' + category + '.txt') as data:
            content = data.readlines()
            return int(len(content) / 3)

    # print specified category
    def printTLE(category, satNr):
        with open('TLE/' + category + '.txt') as data:
            content = data.readlines()
            print(content[((satNr)*3)+1], end="")
            print(content[((satNr)*3)+2], end="")

# controll
createSatellite = True
category = "dummy"
#TLE.download(category)

# define
globalScale = 8
numOfSat = TLE.numOfSat(category)

# satSize = 0.005
satSize = 5
orbitSubDivs = 128

# create lists:
lia_x = []
lia_y = []
lia_z = []
lia_apogee = []
lia_duration = []

# create "all in one" list
xyz = list( [[], [], []] for _ in range(0, numOfSat))

# defein blender scene
sce = bpy.context.scene

n = TLE.numOfSat(category)

# select all objects
bpy.ops.object.select_all(action='SELECT')
print("selected all")

# delete all objects
bpy.ops.object.delete(use_global=False)
print("deleted all")

# loop all satellites in predefined category
for i in range(0, numOfSat):
# for i in range(0, 2):

    satNr = i
    name = TLE.get("name", category, satNr)
    print("{:#<80}".format("#"))
    print("")
    print(name)
    print("{:<5}{:<1}{:<5}".format(i, "/", TLE.numOfSat(category)))
    print("")

    # get Inclination and convert
    inc_deg = float(TLE.get("Inclination", category, satNr))
    inc_rad = inc_deg / 180.0 * math.pi

    # calculate apogee / perigee
    n0 = float(TLE.get("MeanMotion", category, satNr))
    semimajoraxis = ((6.6228 / pow(n0, 2/3)) * 6371)
    orbitheight = semimajoraxis - 6378

    # define time things
    frames = 86400
    frame_long = 15000
    duration = frames / n0
    frame = (((15000 / duration) - int(15000 / duration)) * duration)

    # get Eccentricity and convert
    e0_a = str(TLE.get("Eccentricity", category, satNr))
    e0 = float("0." + e0_a)

    # define apogee / perigee
    apogee = abs(semimajoraxis * (1 + e0) - 6378)
    perigee = abs(semimajoraxis * (1 - e0) - 6378)

    # get RAAN and convert
    RAAN_deg = float(TLE.get("RAAN", category, satNr))
    RAAN_rad = RAAN_deg * math.pi / 180

    # get AoP and convert
    AoP_deg = float(TLE.get("ArgumentOfPerigee", category, satNr))
    AoP_rad = AoP_deg * math.pi / 180

    # eccentricity test
    a = (apogee + 6378) - (perigee + 6378)
    b = (apogee + 6378) + (perigee + 6378)
    e = a / b

    # get name of sat
    name = str(TLE.get("name", category, satNr))

    # print informations to console
    print("|{:<20}|{:<20}|{:<20}|".format("value", "degrees", "radians"))

    print("+{:-<20}+{:-<20}+{:-<20}+".format("-", "-", "-"))

    print("|{:<20}|{:<20}|{:<20}|".format("inc", inc_deg, inc_rad))
    print("|{:<20}|{:<20}|{:<20}|".format("RAAN", RAAN_deg, RAAN_rad))
    print("|{:<20}|{:<20}|{:<20}|".format("AoP", AoP_deg, AoP_rad))

    print("")

    print("|{:<20}|".format("semimajoraxis"))
    print("+{:-<20}+".format("-"))
    print("|{:<20}|".format(semimajoraxis))

    print("")

    print("|{:<20}|{:<20}|".format("Apogee", "Perigee"))
    print("+{:-<20}+{:-<20}+".format("-", "-"))
    print("|{:<20}|{:<20}|".format(apogee, perigee))

    print("")
    print("TLE:")
    TLE.printTLE(category, satNr)
    print("")

    # add orbit w/ name
    bpy.ops.mesh.primitive_circle_add(radius=1, vertices=orbitSubDivs)
    bpy.context.object.name = name

    # add satellite w/ name
    bpy.ops.mesh.primitive_cube_add(radius=satSize)
    bpy.context.object.name = name + "sat"

    # define orbit / sat
    orbit = bpy.context.scene.objects[name]
    sat = bpy.context.scene.objects[name + "sat"]

    orbitname = name
    satname = name + "sat"

    # convert orbit mesh to curve
    sat.select = False
    orbit.select = True
    bpy.context.scene.objects.active = orbit
    bpy.ops.object.convert(target='CURVE')

    duration = int(86400 / n0)

    # set orbit duration
    bpy.data.curves[name].path_duration = duration
    print("n0 -> " + str(n0))
    print("duration -> " + str(duration))

    # resize orbit
    sat.select = True
    orbit.scale[0] = apogee
    orbit.scale[1] = perigee

    # set sat to follow orbit
    sat.location[1] = perigee

    # make satellite follow orbit
    bpy.context.scene.objects.active = orbit
    bpy.ops.object.parent_set(type='FOLLOW')

    select.orbit = False
    select.sat = True
    bpy.context.scene.objects.active = orbit
    bpy.data.curves[orbitname].path_duration = duration

    # set Argument of Perigee
    orbit.rotation_euler[2] = AoP_rad
    # set inclination
    orbit.rotation_euler[0] = inc_rad
    # set RAAN
    bpy.ops.transform.rotate(value=RAAN_rad, constraint_axis=(False, False, True), constraint_orientation='LOCAL')

    # set orbit as active object
    bpy.context.scene.objects.active = orbit

    # select sat
    sat.select = True

    # get location each x frames (higher -> quicker)
    resolution = 10

    # delete old lists
    del lia_x[:]
    del lia_y[:]
    del lia_z[:]
    del lia_apogee[:]
    del lia_duration[:]

    # get values from sat
    for x in range(0, duration, resolution):
        # set frame
        sce.frame_set(x)

        # clear parent to be able to get values
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        # add location to list
        lia_x.append(sat.location[0])
        xyz[i][0].append(sat.location[0])

        # re-add parent for visualization
        bpy.ops.object.parent_set(type='FOLLOW')

    for y in range(0, duration, resolution):
        # set frame
        sce.frame_set(y)

        # clear parent to be able to get values
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        # add location to list
        lia_y.append(sat.location[1])
        xyz[i][1].append(sat.location[1])

        # re-add parent for visualization
        bpy.ops.object.parent_set(type='FOLLOW')

    for z in range(0, duration, resolution):
        # set frame
        sce.frame_set(z)

        # clear parent to be able to get values
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        # add location to list
        lia_z.append(sat.location[2])
        xyz[i][2].append(sat.location[2])

        # re-add parent for visualization
        bpy.ops.object.parent_set(type='FOLLOW')

    # create duration list
    for i in range(0, int(duration / resolution), 1):
        lia_duration.append(i)

    # print length of list lia_x
    length = len(lia_x)
    print("length -> " + str(length))

    # plot location values
    # plot(lia_x, '-ro')
    # plot(lia_y, '-go')
    # plot(lia_z, '-bo')

print("{:#<80}".format("#"))

# create array filled with zeros
array = np.zeros((numOfSat + 3, numOfSat + 3))
# array = np.zeros((10, 10))

# define
t = 1
satNr = 1

for t in range(0, 10, 1):

    print(xyz[satNr][0][t])
    print(xyz[satNr][1][t])
    print(xyz[satNr][2][t])
    print(numOfSat)

    # horizontal define:
    y = 0
    # for x in range(3, 10, 1):
    for x in range(3, numOfSat + 3, 1):
        array[y+0, x] = round(xyz[x-3][0][t], 1)
        array[y+1, x] = round(xyz[x-3][1][t], 1)
        array[y+2, x] = round(xyz[x-3][2][t], 1)

    print("")
    print(array)
    print("")

    # vertical define:
    x = 0
    # for y in range(3, 10, 1):
    for y in range(3, numOfSat + 3, 1):
        array[y, x+0] = round(xyz[y-3][0][t], 1)
        array[y, x+1] = round(xyz[y-3][1][t], 1)
        array[y, x+2] = round(xyz[y-3][2][t], 1)

    print(array)
    print("")

    for x in range(3, numOfSat + 3, 1):
        for y in range(3, numOfSat + 3, 1):
    # for x in range(3, numOfSa, 1):
        # for y in range(3, numOfSat, 1):
            # print("{:-<10}".format("-"))
            # print(x, y)
            # print("")
            a = array[0, x]
            b = array[1, x]
            c = array[2, x]
            # print("{:<20}{:<20}{:<20}".format(a, b, c))

            d = array[y, 0]
            e = array[y, 1]
            f = array[y, 2]
            # print("{:<20}{:<20}{:<20}".format(d, e, f))

            g = pow(abs(a - d), 2)
            h = pow(abs(b - e), 2)
            i = pow(abs(c - f), 2)
            # print("{:<20}{:<20}{:<20}".format(g, h, i))

            # j = math.sqrt(g)
            # k = math.sqrt(h)
            # l = math.sqrt(i)
            # print("{:<20}{:<20}{:<20}".format(j, k, l))
            #
            # m = j + k + l
            m = round(math.sqrt(g + h + i), 1)
            # print(m)
            array[x, y] = m

    print("")
    print(array)

for i in range(0, int(numOfSat)):
    plot(xyz[i][0], '-ro')
    plot(xyz[i][1], '-go')
    plot(xyz[i][2], '-bo')
    # plot(abc, '-ko')

for x in range(3, numOfSat, 1):
    for y in range(3, numOfSat, 1):
        if array[x, y] <= 1 and array[x, y] > 0 :
            print(array[x, y])

# select all and resize
bpy.ops.object.select_all(action='SELECT')
bpy.ops.transform.resize(value=(globalScale, globalScale, globalScale))

# show plot
grid(True)
savefig("run.png")
title("resolution: " + str(resolution))
xlabel("Nr. of Value (Value * resolution to get Frame Time)")
ylabel("location in km")
xlim(0, duration / resolution)
ylim(-apogee - 100, apogee + 100)
show()

sce.frame_set(0)
