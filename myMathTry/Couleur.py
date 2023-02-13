class Couleur(Triplet):

    def __init__(self, t, x, y, z):
        Triplet.__init__(self, 'C', x, y, z)

    def add(self, Triplet):
        n_x = self.__x + Triplet.get_x()
        n_y = self.__y + Triplet.get_y()
        n_z = self.__z + Triplet.get_z()
        return self.__class__(n_x,n_y,n_z)

    # Produit de Shur
    def times(self, Triplet):
        return self.__class__(
            self.__x * Triplet.get_x(),
            self.__y * Triplet.get_y(),
            self.__z * Triplet.get_z(),
        )