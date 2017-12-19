import argparse
import time
import matplotlib.pyplot
import math

from emwaves import fourspace
from emwaves import grid


if __name__ == '__main__':

    alpha = 1#4*alpha = 32
    H = True
    ds = (alpha/8.0, alpha/8.0, alpha/8.0, alpha/16.0)
    #size = (200, 60)
    size = (200, 100)
    timesteps = 100
    grid_zero = None#grid.grid(size)
    Z = 376.7

    conductor = [int((size[0]/2.0) - 5),
                int((size[0]/2.0) + 5),
                int((size[1]/2.0) - 5),
                int((size[1]/2.0) + 5)]
    
    # m = size[0]*(1.0/4)
    # source = {'xmin': int(m-(size[0]/5.0)),
    #           'xmax': int(m+(size[0]/5.0)),
    #           'ymin': 1,
    #           'ymax': size[1] - 1,
    #           'duration': 5}
  
    m = size[0]*(2.3/4)
    source = {'xmin': 0,
              'xmax': size[0],
              'ymin': int(m-(size[1]/5.0)),
              'ymax': int(m+(size[1]/5.0)),
              'duration': 10 }  


    sim = fourspace.fourspace(grid_zero,
                              timesteps=timesteps,
                              Z=Z,
                              size=size,
                              ds=ds,
                              alpha=alpha,
                              conductor=conductor,
                              source=source)


    for t in range(2, timesteps):
        ##new_grid, one_ahead =  size, ds, one_ahead)
        sim.next_grid(t)
        sim.updateplot(t)

    sim.save_data()
