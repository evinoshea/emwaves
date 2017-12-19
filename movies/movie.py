import h5py
import time
import matplotlib.pyplot
import numpy
from sys import argv


if __name__ == '__main__':

    dfile = argv[1]
    field = argv[2]

    h5f = h5py.File(dfile,'r')
    data = h5f['fourspace'][:]
    h5f.close()



    if field == 'Ez':
        f = matplotlib.pyplot.figure()
        graph1 =  f.add_subplot(111)
        Ezplot =  graph1.imshow(data[0]['Ez'])
        bar1 = matplotlib.pyplot.colorbar(Ezplot)
        f.show()
    elif field == 'Hy':
        f = matplotlib.pyplot.figure()
        graph1 =  f.add_subplot(111)
        Hyplot =  graph1.imshow(data[0]['Hy'])
        bar1 = matplotlib.pyplot.colorbar(Hyplot)
        f.show()
    elif field == 'Hx':
        f = matplotlib.pyplot.figure()
        graph1 =  f.add_subplot(111)
        Hxplot =  graph1.imshow(data[0]['Hx'])
        bar1 = matplotlib.pyplot.colorbar(Hxplot)
        f.show()
    

    for i in range(1, len(data)):
        if field == 'Ez':
            Ezplot.set_array(data[i]['Ez'])
        elif field == 'Hy':
            Hyplot.set_array(data[i]['Hy'])
        elif field == 'Hx':
            Hxplot.set_array(data[i]['Hx'])



        bar1.draw_all()
        #matplotlib.pyplot.colorbar(f)
        
        f.canvas.draw()
        time.sleep(.1)




    """
    f = matplotlib.pyplot.figure()
    graph1 =  f.add_subplot(311)
    Ezplot =  graph1.imshow(data[0]['Ez'])
    bar1 = matplotlib.pyplot.colorbar( Ezplot)

    graph2 =  f.add_subplot(312, sharex= graph1)
    Hyplot =  graph2.imshow(data[0]['Hy'])
    bar2 = matplotlib.pyplot.colorbar( Hyplot)

    graph3 =  f.add_subplot(313, sharex= graph1)
    Hxplot =  graph3.imshow(data[0]['Hx'])
    bar3 = matplotlib.pyplot.colorbar( Hxplot)

    matplotlib.pyplot.show(block=False)
    for i in range(1, len(data)):
        Ezplot.set_array( data[i]['Ez'])
        Hyplot.set_array( data[i]['Hy'])
        Hxplot.set_array( data[i]['Hx'])

        bar1.draw_all()
        bar2.draw_all()
        bar3.draw_all()

        #matplotlib.pyplot.colorbar( f.)
        f.canvas.draw()

        #PLOT data['data'][i]
        time.sleep(1)
    """
