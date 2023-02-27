# from Point import * 
from math_lib.Point import *

class Vecteur(Point):

    def __init__(self, x, y, z):
        Triplet.__init__(self, 'V', x, y, z)
    
    def isValidAdd(self, triplet):
        if not (triplet.get_t()=='V'):
            raise ValueError

    def dot(self,triplet):
        if not (triplet.get_t()=='V'):
            raise ValueError

        sum = 0 
        sum += self.get_x() * triplet.get_x()
        sum += self.get_y() * triplet.get_y()
        sum += self.get_z() * triplet.get_z()
        return sum

    def cross(self,triplet): # produit vectoriel
        if not (triplet.get_t()=='V'):
            raise ValueError

        return self.__class__(
            self.get_y() * triplet.get_z() - self.get_z() * triplet.get_y(),
            self.get_z() * triplet.get_x() - self.get_x() * triplet.get_z(),
            self.get_x() * triplet.get_y() - self.get_y() * triplet.get_x()
        )
    
    def len(self):
        sum = 0
        sum += math.pow(self.get_x(), 2)
        sum += math.pow(self.get_y(), 2)
        sum += math.pow(self.get_z(), 2)
        return math.sqrt(sum)
    
    def hat(self):
        l = self.len()
        self.mul(1/l)

    def times(self,triplet):
        raise ValueError