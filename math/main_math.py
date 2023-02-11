# from math1 import Triplet
# from math1 import Vector
from mymath import *


def create_(tab):
    if tab[0] == 'V':
        var = Vector(int(tab[1]),int(tab[2]),int(tab[3]))
    else:
        var = 3
    return var

if __name__ == '__main__':
    # n1 = Triplet(1,1,1)
    # n2 = Triplet(1,2,3)
    # n3 = Triplet(2,3,4)
    v1 = Triplet('V',1,0,0)
    v2 = Triplet('V',0,1,0)
    v3 = v1.cross(v2)
    v1.show()
    v2.show()
    v3.show()
    # n1.show()
    # n2.show()
    # n3.show()
    #
    