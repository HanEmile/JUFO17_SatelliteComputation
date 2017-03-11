# import
import numpy as np
import matplotlib.pyplot as plt

# define r, theta, phi
r = 0
theta = 0
phi = 0
cart = [r, theta, phi]

def poltocart(pol):
    print(pol)

    x = pol[0]
    y = pol[1]
    z = pol[2]

    # radius
    r = np.sqrt(np.power(x, 2) + np.power(y, 2) + np.power(z, 2))

    # theta
    theta = np.arccos( z / r )

    # phi
    if x > 0:
        phi = np.arctan(y/x)
    elif x == 0:
        phi = np.sign(y)*(np.pi/2)
    elif x < 0 and y >= 0:
        phi = np.arctan(y/x) + math.pi
    elif x < 0 and y < 0:
        phi = np.arctan(y/x) - math.pi

    # write to cartesian list
    cart[0] = r
    cart[1] = theta
    cart[2] = phi

    return cart

poltocart([4, 3, 5])
