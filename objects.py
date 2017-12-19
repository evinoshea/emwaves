import numpy
import math

class conductor(object):

    def __init__(self, xmin=None, xmax=None, ymin=None, ymax=None):
        #print(xmin, xmax, ymin, ymax)
        self.space = [(i, j) for i in range(xmin, xmax) for j in range(ymin, ymax)]
        #print(self.space)


class source(object):

    def __init__(self, size, alpha, dx, dt, xmin, xmax, ymin, ymax, duration):
        self.alpha = alpha
        self.offset = ((ymax + ymin) / 2.0)
        self.size = size #of whole grid
        self.dx = dx
        self.dt = dt
        self.ontime = self.dt*1
        self.therange = range( duration)
        if None in [xmin, xmax, ymin, ymax]:
            self.location = []
        else:
            self.location = [(i , j) for i in range(xmin, xmax) \
                                for j in range(ymax, ymin)]


    def space(self, x, t, field):
        if x[0] < self.size[0] and x[1] < self.size[1]:
            if field in ['Ez', 'Hy']:
                if int(self.calc_in(x[0], t)) in self.therange and t < 3 and x[1] in range(20,self.size[1]-20):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def assign_field(self, field, Z, x, t, alpha):
        data = numpy.zeros(shape=self.size, dtype=numpy.float32())
        if field == 'Ez':
            factor = 1
            i = x[0] 
        else:
            t = t - 0.5
            i = x[0] - 0.5
            factor = 1.0/Z


        # for i in range(self.size[0]):
        #     for j in range(self.size[1]):
        if int(self.calc_in(x[0], t)) in self.therange and t < 3 and x[1] in range(20,self.size[1]-20):
            data = factor*5.0*math.sin((self.calc_in(i, t)/(8))*(3.1415) )
        else:
            data = 0
        return data

    def calc_in(self, i, t):
        return i-self.offset+t*self.ontime