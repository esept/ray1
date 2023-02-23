from Couleur import *

class Point(Couleur):

    def __init__(self, x, y, z):
        Triplet.__init__(self, 'P', x, y, z)

    def isValidAdd(self, triplet):
        if not (triplet.get_t()=='V'):
            raise ValueError

    def sub(self, triplet): 
        # triplet doit être un point (ou V lorsqu'il faut sub avec un autre V) !
        if not ((self.get_t()=='P' and triplet.get_t()=='P') or (self.get_t()=='V' and triplet.get_t()=='V')):
            raise ValueError
        
        n_x = self.get_x() - triplet.get_x()
        n_y = self.get_y() - triplet.get_y()
        n_z = self.get_z() - triplet.get_z()

        if (self.get_t()=='P' and triplet.get_t()=='P'):
            return Triplet('V',n_x,n_y,n_z)
        return self.__class__(n_x,n_y,n_z)