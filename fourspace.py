import matplotlib.pyplot
import numpy
import h5py
import math

from emwaves import objects
from emwaves import grid

"""This is the whole simulation object (all of time, all grids) """

class fourspace(object):

    def __init__(self, grid_zero, timesteps, Z, size, ds, alpha, conductor=[], source={}):
        self.FIELDS = ['Ez', 'Hy', 'Hx']
        self.size = size
        self.dt = ds[0]
        self.dx = ds[1]
        self.dy = ds[2]
        self.dz = ds[3]
        self.alpha = alpha
        self.Z = Z
        if conductor:
            #min and max for x and y coords of conductor
            self.conductor = objects.conductor(conductor[0], conductor[1], conductor[2], conductor[3])
        else:
            self.conductor = None
        if source:
            self.source = objects.source(size, self.alpha, self.dx, self.dt, **source)
        else:
            source = None

        #or make grid_zero here
        if grid_zero is None:
            self.grids = [self.initialize_grid(t) for t in range(3)]
        else:
            self.grids = [grid_zero, grid_zero, grid_zero]
        self.timesteps = timesteps

        #make figure for plotting
        self.f1 = matplotlib.pyplot.figure()
        self.graph1 = self.f1.add_subplot(111)
        self.Ezplot = self.graph1.imshow(self.grids[0].lattice['Ez'])
        self.bar1 = matplotlib.pyplot.colorbar(self.Ezplot)
        
        self.f2 = matplotlib.pyplot.figure()
        self.graph2 = self.f2.add_subplot(111)#321, sharex=self.graph1)
        self.Hyplot = self.graph2.imshow(self.grids[0].lattice['Hy'])
        self.bar2 = matplotlib.pyplot.colorbar(self.Hyplot)
        
        self.f3 = matplotlib.pyplot.figure()
        self.graph3 = self.f3.add_subplot(111)#331, sharex=self.graph1)
        self.Hxplot = self.graph3.imshow(self.grids[0].lattice['Hx'])
        self.bar3 = matplotlib.pyplot.colorbar(self.Hxplot)
        

        matplotlib.pyplot.show(block=False)

    def initialize_grid(self, t):
        this_grid = grid.grid(self.size)

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                x = (i, j)
                for field in self.FIELDS:
                    if self.source.space(x, t, field):
                        this_grid.lattice[x][field] = self.source.assign_field(field, self.Z, x, t, self.alpha)
                    else:
                        this_grid.lattice[x][field] = 0
        return this_grid

    def save_data(self):
        data = numpy.ndarray((len(self.grids), self.size[0], self.size[1]), dtype=\
                                    self.grids[0].lattice.dtype)

        for i in range(len(self.grids)):
            data[i] = self.grids[i].lattice[:][:][:]

        h5f = h5py.File('data.h5', 'w')
        h5f.create_dataset('fourspace', data=data)
        h5f.close()



    def objectspace(self, x, t, field):
        #complicated way of checking if the
        if self.conductor is None and self.source is None:
            #no object to be inside of
            return False
        elif self.conductor and self.source:
            if x in self.conductor.space or self.source.space(x, t, field):
                #location is inside the object
                return True
            else:
                return False
        elif self.conductor:
            if x in self.conductor.space:
                return True
            else:
                return False
        elif self.source:
            if self.source.space(x, t):
                return True
            else:
                return False
        else:
            return False


    def updateplot(self, t):
        #change data in plots
        self.Ezplot.set_array(self.grids[t].lattice['Ez'])
        self.Hyplot.set_array(self.grids[t].lattice['Hy'])
        self.Hxplot.set_array(self.grids[t].lattice['Hx'])
        #re-draw the scales
        self.bar1.draw_all()
        self.bar2.draw_all()
        self.bar3.draw_all()
        #Refresh the appearence of the plots
        self.f1.canvas.draw()
        self.f2.canvas.draw()
        self.f3.canvas.draw()
        print(t)


    def next_grid(self, t):
        #add another time step to the set of grids
        self.grids.append(grid.grid(self.size))
        #iterate over whole grid
        for i in range(-1, self.size[0]):
            for j in range(-1, self.size[1]):
                self.evolveTM(t, i, j)


    def evolveTM_NEW(self, t, i, j):
        #repeat for H fields
        Hx = (4*(
            self.get_val(t-.5, (i, j+.5), 'Hx') \
            - (1.0/self.Z)*(self.dt/self.dx)*(self.get_val(t, (i, j+1), 'Ez') -\
            self.get_val(t, (i, j), 'Ez'))
            ) \
            - 2*self.get_val(t+1, (i, j), 'Hx') \
            - self.get_val(t, (i, j), 'Hx'))

        
        self.assign_val(t+1, (i, j+1), 'Hx', value=Hx)


        Hy = (4*(
            self.get_val(t-.5, (i+.5, j), 'Hy') \
            + (1.0/self.Z)*(self.dt/self.dx)*(self.get_val(t, (i+1, j), 'Ez') - self.get_val(t, (i, j), 'Ez'))
            ) \
            - 2*self.get_val(t+1, (i, j), 'Hy') \
            - self.get_val(t, (i, j), 'Hy'))

        self.assign_val(t+1, (i+1, j), 'Hy', value=Hy)

        #calculate the new field value
        Ez = (
            self.get_val(t, (i, j), 'Ez') \
            + (self.Z)*(self.dt/self.dx)*(self.get_val(t+.5, (i+.5, j), 'Hy') -\
            self.get_val(t+.5, (i-.5, j), 'Hy'))  \
            - (self.Z)*(self.dt/self.dy)*(self.get_val(t+.5, (i, j+.5), 'Hx') -\
            self.get_val(t+.5, (i, j-.5), 'Hx'))
            )
        #store the field value in the array of data
        self.assign_val(t+1, (i, j), 'Ez', value=Ez)


    def get_val(self, t=1, x=(0,0), field='Ex'):
        """
        #if there is half time step and half position step
        if (not (int(t) == t)) and (False in [int(i) == i for i in x]):
            pos_index = 0 if int(x[0]) != x[0] else 1
            x1 = [int(math.floor(x[i])) if i == pos_index else x[i] for i in range(len(x))]
            x2 = [int(math.ceil(x[i])) if i == pos_index else x[i] for i in range(len(x))]

            return (1/4.0)*(self.extract_val(int(math.floor(t)), x1, field) + self.extract_val(int(math.ceil(t)), x1, field) \
                          + self.extract_val(int(math.floor(t)), x2, field) + self.extract_val(int(math.ceil(t)), x2, field))

        #if there is only a time half step
        elif not (int(t) == t):
            return self.extract_val(int(math.floor(t)), x, field) + self.extract_val(int(math.ceil(t)), x, field) 
        #if there is only a half position step
        elif False in [int(i) == i for i in x]:
            pos_index = 0 if int(x[0]) != x[0] else 1
            x1 = [int(math.floor(x[i])) if i == pos_index else x[i] for i in range(len(x))]
            x2 = [int(math.ceil(x[i])) if i == pos_index else x[i] for i in range(len(x))]

            return (1/2.0)*(self.extract_val(t, x1, field) + self.extract_val(t, x1, field))

        else:
        """
        return self.extract_val(t, x, field)

    def extract_val(self, t, x, field):
        #if it is outside of the grid or in a conductor it will return zero
        if any([x[index] < 0 or x[index] > self.size[index]-1 \
                        for index in range(len(x))]) or x in self.conductor.space:
            return 0
        else:
            val = self.grids[t].lattice[x[0]][x[1]][field]
            return  val


    def assign_val(self, t, x, field, value):
        #check if the location is inside a conductor, the initial conditions, or outisde the grid
        if any([x[index] < 0 or x[index] > self.size[index]-1 \
                        for index in range(len(x))]) or self.objectspace(x, t, field):
            if x in self.conductor.space:
                #inside the conductor, assing 0
                self.grids[t].lattice[x][field] = 0
            elif self.source.space(x, t, field):
                self.grids[t].lattice[x][field] = self.source.assign_field(field, self.Z, x, t, self.alpha)
            else:
                #outside fo the grid, dont assign a value
                pass
        else:
            if not (t < 0 or t > self.timesteps+2):
                #if a normal point, assign the value
                self.grids[t].lattice[x][field] = value
            else:
                raise ValueError("Tried to access time that is out of bounds.")



    def evolveTM(self, t, i, j):
        Hx = (
            self.get_val(t, (i, j+1), 'Hx') \
            - (1.0/self.Z)*(self.dt/self.dx)*(self.get_val(t, (i, j+1), 'Ez') -\
            self.get_val(t, (i, j), 'Ez'))
            )

        self.assign_val(t+1, (i, j+1), 'Hx', value=Hx)

        Hy = (
            self.get_val(t, (i+1, j), 'Hy') \
            + (1.0/self.Z)*(self.dt/self.dx)*(self.get_val(t, (i+1, j), 'Ez') - self.get_val(t, (i, j), 'Ez'))
            )

        self.assign_val(t+1, (i+1, j), 'Hy', value=Hy)

        #calculate the new field value
        Ez = (
            self.get_val(t, (i, j), 'Ez') \
            + (self.Z)*(self.dt/self.dx)*(self.get_val(t+1, (i+1, j), 'Hy') -\
            self.get_val(t+1, (i, j), 'Hy'))  \
            - (self.Z)*(self.dt/self.dy)*(self.get_val(t+1, (i, j+1), 'Hx') -\
            self.get_val(t+1, (i, j), 'Hx'))
            )
        
        #store the field value in the array of data
        self.assign_val(t+1, (i, j), 'Ez', value=Ez)