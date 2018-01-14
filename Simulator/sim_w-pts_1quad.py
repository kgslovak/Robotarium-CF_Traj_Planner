#!/usr/bin/env python

import numpy as np

from util.interpolation import *
from util.vizualization import *



if __name__ == "__main__":
### SIMULATION SETUP: #########################################################

    # Set number of agents and spline polynomial-degree
    N = 1
    deg = 8

    # Store waypoints as entries in a dictionary for each agent
    p0 = dict()

    # Waypoint format:
    #                [[    x,    y,    z],
    #                 [ roll, ptch,  yaw],
    #                 [   xd,   yd,   zd],
    #                 [   rd,   pd,   yd]]

    p0[0] = np.array([[ -1.0, -1.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    p0[1] = np.array([[ -1.0, -1.0, -0.8],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    p0[2] = np.array([[  0.5,  1.0, -1.2],
                      [ -0.2,  0.2, -0.1],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    p0[3] = np.array([[ -0.6,  1.0, -1.0],
                      [  0.2, -0.8,  0.1],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    p0[4] = np.array([[  1.5, -1.0, -0.6],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    p0[5] = np.array([[  1.5, -1.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0],
                      [  0.0,  0.0,  0.0]])

    # Set time duration between points and simulation's time step size
    T = np.array([1, 2, 2, 2, 1, 2])
    dt = 0.02


### SIMULATION VISUALIZATION: #################################################
    
    # Setup figure and axes
    fig = plt.figure()
    ax  = fig.gca(projection = '3d')
    ax.set_aspect('equal')
    ax.invert_zaxis()

    # Create bounding cube with equal aspect ratio (defined by corners)
    max_range = 3
    Xb = 0.5*max_range*np.mgrid[-1:1:2j,-1:1:2j,-1:1:2j][0].flatten()
    Yb = 0.5*max_range*np.mgrid[-1:1:2j,-1:1:2j,-1:1:2j][1].flatten() 
    Zb = 0.5*max_range*np.mgrid[-1:1:2j,-1:1:2j,-1:1:2j][2].flatten() - 1
    for xb, yb, zb in zip(Xb, Yb, Zb):
       ax.plot([xb], [yb], [zb], 'w')
    plt.pause(.001)

    # Initialize plotting handles
    CF_Coord = Coord3D(ax, p0[0][0,:])

    # Visualize flight path
    for i in range(len(p0)):
	# Reset "initial time" when starting a new trajectory segment
        t = 0
	# Set index for "next point" (loops back to initial position)
        j = i+1
        if (j==len(p0)):
            j = 0
	# Obtain interpolation coeff for current trajectory segment
        coeff = Interp(p0[i], p0[j], T[i], deg) 
        while (t<T[i]):
           t += dt
           curr_pt = ExtractVal(coeff, t, T[i])
           roll, pitch, yaw = Invert_diff_flat_output(curr_pt)
	   CF_Coord.update(curr_pt[0,:], roll, pitch, yaw)
           plt.pause(.001)           
    plt.show()



