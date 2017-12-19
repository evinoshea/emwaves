
import numpy


class grid(object):

    def __init__(self, size=(100, 100)):
        #make array of cells
        dt = [(fieldname, numpy.float32()) for fieldname in ['Ez', 'Hx', 'Hy']] #'Hz', 'Ex', 'Ey']]
        self.lattice = numpy.zeros(shape=size, dtype=numpy.dtype(dt))
