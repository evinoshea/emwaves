

class conductor(object):

    def __init__(xmin, xmax, ymin, ymax):
        self.space = [(i , j) for i in range(xmin, xmax) \
                                for j in range(ymax, ymin)]


class source(object):

    def __init__(xmin, xmax, ymin, ymax, duration):



    def assign_field(field):

    def infunction():
        # if int(x[0]-50*alpha) in range(0, int(8*alpha)):
        #     return 5.0* math.sin(((dx*x[0]-50*alpha)/(8*alpha))*(3.1415) )
        # else:
        #     return .05
        H = False
        m = size[0]*(1.0/4)
        if x[0] in range(int(m-(size[0]/5.0)), int(m+(size[0]/5.0))):
            return (5.0/5 )* math.cos( ((x[0]-m)/(size[0]/10.0))*(3.1415*2))
        else:
            return 0.0
