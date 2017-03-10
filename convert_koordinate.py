# import
import math
import numpy as np
import matplotlib.pyplot as plt

# pol[x, y, z]
x = 1
y = 2
z = 3
pol = [x, y, z]

# define r, theta, phi
r = 0
theta = 0
phi = 0
kart = [0, 0, 0]

def poltokart(pol):
    # split up list
    x = pol[0]
    y = pol[1]
    z = pol[2]

    # radius
    r = np.sqrt(np.power(x, 2) + np.power(y, 2) + np.power(z, 2))

    # theta
    a = np.sqrt(x^2 + y^2 + z^2)
    b = ((z) / a)
    b = b * math.pi / 180
    theta = np.arccos(b)

    # phi
    if x > 0:
        phi = np.arctan(y/x)
    elif x == 0:
        phi = np.sign(y)*(math.pi/2)
    elif x < 0 and y >= 0:
        phi = np.arctan(y/x) + math.pi
    elif x < 0 and y < 0:
        phi = np.arctan(y/x) - math.pi

    # write to cartesian list
    kart[0] = r
    kart[1] = theta
    kart[2] = phi

# run
poltokart(pol)

print("{:<15}{:<60}".format("polar:", str(pol) ))
print("{:<15}{:<60}".format("cartesian:", str(kart) ))
