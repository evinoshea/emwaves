import matplotlib.pyplot
import Finite_Diffs
import numpy



if __name__ == '__main__':


    Z = 376.7
    Ez = [[[ (2.71**(-((j-20)**2)/100))*10 if (n in [0, 1] and j != 0 and i != 0) else 0 for i in range(60)] for j in range(60)] for n in range(600)]
    Hy = [[[ (1/Z)*(2.71**(-((j-20)**2)/100))*10 if (n in [0, 1] and j != 0 and i != 0) else 0 for i in range(60)] for j in range(60)] for n in range(600)]
    Hz = [[[0 for i in range(60)] for j in range(60)] for n in range(600)] #if (j > 35 and j < 45) else 0
    Ex = [[[0 for i in range(60)] for j in range(60)] for n in range(600)] #if (j > 35 and j < 45) else 0
    Ey = [[[0 for i in range(60)] for j in range(60)] for n in range(600)] #if (j > 35 and j < 45) else 0
    Hx = [[[0 for i in range(60)] for j in range(60)] for n in range(600)] #if (j > 35 and j < 45) else 0

    # heatmap = matplotlib.pyplot.imshow(Hy[0], cmap='hot', interpolation='nearest')
    # matplotlib.pyplot.colorbar(heatmap)
    # matplotlib.pyplot.show()
    #x = numpy.ndarray(shape=(60, 60, 60), data=Hz, dtype=numpy.float32)

    # print(x[0][:][0])
    # print('#############')
    # print([Hz[1][x][0] for x in range(60)])

    print('x')
    print_steps = range(0, 600, 2)#[5, 10, 40, 59]
    dx = 1/1000.0
    dy = 1/1000.0
    dz = 1/1000.0
    dtau = 1/2000.0

    #print(dtau)

    x = Finite_Diffs.Finite_Differences(print_steps,
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
                        Z)

    for n in range(1, 597):
        x.calc(n)
