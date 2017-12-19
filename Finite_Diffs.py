import numpy
import matplotlib.pyplot


class Finite_Differences(object):

    def __init__(self,
                print_steps,
                dx,
                dy,
                dz,
                dtau,
                Hz,
                Ex,
                Ey,
                Hx,
                Hy,
                Ez,
                Z):

        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.dtau = dtau
        self.print_steps = print_steps
        self.Z = Z
        self.Hz = Hz
        self.Ex = Ex
        self.Ey = Ey
        self.Hx = Hx
        self.Hy = Hy
        self.Ez = Ez

        
        # location = [0, 0, 0]
        #
        # def mu(self, i, j):
        #
        #         return 90
        #     else:
        #         return
        #
        # def epsilon(self):
        #     if whatever:
        #         return
        #
        #     def xyz(self):
        #         return self.x, self.y, self.z

    def plotit(self, n):
        #matplotlib.pyplot.subplot(1, 2, 1)
        #self.graph1.title("Ez")

        self.Ezplot.set_array(self.Ez[n])

        self.Hyplot.set_array(self.Hy[n])

        self.bar1.draw_all()
        self.bar2.draw_all()
        #matplotlib.pyplot.colorbar(self.f.)
        self.f.canvas.draw()



    def calc(self, n):
        if n in self.print_steps:
            # plotit(self.Hz, n)
            # plotit(self.Ex, n)
            #print(n)
            self.plotit(n)
            # plotit(self.Hx, n)
            # plotit(self.Hy, n)
            # plotit(self.Ez, n)
        for i in range(1, 60):
            for j in range(1, 60):
                #print(i, j, n)
                #TE waves
                if i == 1 and j == 1:
                    print(i, j, n)
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])

                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif i > 58 and j > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(-1*self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(-1*self.Hx[n+1][i][j-1])
                elif i == 58 and j > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(-1*self.Hx[n+1][i][j-1])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*( -1*self.Hz[n+1][i+1][j-1])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ez[n][i][j])
                elif i == 58 and j == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ez[n][i][j])
                elif i > 58 and j == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(-1*self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(-1*self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(-1*self.Ez[n][i][j])
                elif i == 1 and j > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(-1*self.Hx[n+1][i][j-1])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(-1*self.Hz[n+1][i+1][j-1])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif i == 1 and j == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*( -1*self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = -1*(self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*( -1*self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif i == 1:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif j == 1 and i > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(-1*self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(-1*self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                elif j == 1 and i == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ez[n][i][j])
                elif j == 1:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif i > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(-1*self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(-1*self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                elif i == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(-1*self.Ez[n][i][j])
                elif j == 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(-1*self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(-1*self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                elif j > 58:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(-1*self.Hx[n+1][i][j-1])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(-1*self.Hz[n+1][i+1][j-1])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
                else:
                    self.Ez[n+2][i][j] = self.Ez[n][i][j] + (self.Z)*(self.dtau/self.dx)*(self.Hy[n+1][i+1][j] - self.Hy[n+1][i-1][j]) \
                                                          - (self.Z)*(self.dtau/self.dy)*(self.Hx[n+1][i][j+1] - self.Hx[n+1][i][j-1])
                    self.Hz[n+1][i+1][j+1] = self.Hz[n-1][i+1][j+1] - (1/self.Z)*(self.dtau/self.dx)*(self.Ey[n][i+2][j+1] - self.Ey[n][i][j+1]) \
                                                          + (1/self.Z)*(self.dtau/self.dy)*(self.Ex[n][i+1][j+2] - self.Ey[n][i+1][j])
                    self.Ex[n+2][i+1][j] = self.Ex[n][i+1][j] - (self.Z)*(self.dy/self.dtau)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i+1][j-1])
                    self.Ey[n+2][i][j+1] = - (self.Z)*(self.dtau/self.dx)*(self.Hz[n+1][i+1][j+1] - self.Hz[n+1][i-1][j+1])
                    self.Hx[n+1][i][j+1] = self.Hx[n-1][i][j+1] - (1/self.Z)*(self.dtau/self.dy)*(self.Ez[n][i][j+2] - self.Ez[n][i][j])
                    self.Hy[n+1][i+1][j] = self.Hy[n-1][i+1][j] + (1/self.Z)*(self.dtau/self.dx)*(self.Ez[n][i+2][j] - self.Ez[n][i][j])
