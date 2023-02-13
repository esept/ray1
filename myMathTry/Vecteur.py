class Vecteur(Point, Couleur):

    def __init__(self, t, x, y, z):
        Triplet.__init__(self, 'V', x, y, z)

    def dot(self,Triplet):
        sum = 0
        sum += self.__x * Triplet.get_x()
        sum += self.__y * Triplet.get_y()
        sum += self.__z * Triplet.get_z()
        return sum

    def cross(self,Triplet):# produit vectoriel
        return self.__class__('V',
            self.__y * Triplet.get_z() - self.__z * Triplet.get_y(),
            self.__z * Triplet.get_x() - self.__x * Triplet.get_z(),
            self.__x * Triplet.get_y() - self.__y * Triplet.get_x()
        )
    
    def len(self):
        sum = 0
        sum += math.pow(self.__x, 2)
        sum += math.pow(self.__y, 2)
        sum += math.pow(self.__z, 2)
        return math.sqrt(sum)
    
    def hat(self):
        l = self.len()
        self.mul(1/l)

    # Produit de Shur
    def times(self,Triplet):
        return