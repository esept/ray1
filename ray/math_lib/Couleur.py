from Triplet import Triplet

class Couleur(Triplet):

    def __init__(self, x, y, z):
        Triplet.__init__(self, 'C', x, y, z)

    def isValidAdd(self, triplet):
        if not (triplet.get_t()=='C'):
            raise ValueError

    def add(self, triplet):
        self.isValidAdd(triplet)

        n_x = self.get_x() + triplet.get_x()
        n_y = self.get_y() + triplet.get_y()
        n_z = self.get_z() + triplet.get_z()
        return self.__class__(n_x, n_y, n_z)

    def times(self, triplet):
        if not (triplet.get_t()=='C'):
            raise ValueError

        return self.__class__(
            self.__x * triplet.get_x(),
            self.__y * triplet.get_y(),
            self.__z * triplet.get_z(),
        )