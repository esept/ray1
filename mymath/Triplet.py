import math
class Triplet:
    __type = None
    __x = 0
    __y = 0
    __z = 0
    
    def __init__(self, t, x, y, z):
        self.__type = t
        self.__x = x
        self.__y = y
        self.__z = z
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z

    def add(self, Triplet):
        
        n_x = self.__x + Triplet.get_x()
        n_y = self.__y + Triplet.get_y()
        n_z = self.__z + Triplet.get_z()
        return self.__class__(n_x,n_y,n_z)
        
    
    def mul(self, a):
        return self.__class__(self.__x*a,
                              self.__y*a,
                              self.__z*a)

    def dot(self,Triplet):
        sum = 0
        sum += self.__x * Triplet.get_x()
        sum += self.__y * Triplet.get_y()
        sum += self.__z * Triplet.get_z()
        return sum

    def sub(self,Triplet):
        return self.add(Triplet.mul(-1))

    def cross(self,Triplet):# produit vectoriel
        return self.__class__('V',
            self.__y * Triplet.get_z() - self.__z * Triplet.get_y(),
            self.__z * Triplet.get_x() - self.__x * Triplet.get_z(),
            self.__x * Triplet.get_y() - self.__y * Triplet.get_x()
        )

    def times(self,Triplet):
        return self.__class__(
            self.__x * Triplet.get_x(),
            self.__y * Triplet.get_y(),
            self.__z * Triplet.get_z(),
        )
    
    def hat(self):
        l = self.len()
        self.mul(1/l)
    
    def len(self):
        sum = 0
        sum += math.pow(self.__x, 2)
        sum += math.pow(self.__y, 2)
        sum += math.pow(self.__z, 2)
        return math.sqrt(sum)
    
    
    def show(self):
        print(f"[{self.__x},{self.__y},{self.__z}]")

