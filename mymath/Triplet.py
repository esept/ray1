import math
import sys

# sys._getframe().f_code.co_name

class Triplet:
    __type = None
    __x = 0
    __y = 0
    __z = 0
    
    def __init__(self, x, y, z,t = None):
        self.__type = t
        self.__x = x
        self.__y = y
        self.__z = z
        
    def check_type(self, this_type, param_type=None):
        if (param_type == None and self.__type == this_type) :
            return False
        elif self.__type == this_type or param_type == this_type:
            return False
        else:
            return True
    
    def check_same_type(self,param_type):
        if self.__type != param_type :
            return False
        else:
            return True
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    
    def get_t(self):
        return self.__type

    def add(self, Triplet):
        '''
        :param Triplet:
        :return: new Triplet after addition
        '''
        if( self.__type == 'P' and Triplet.get_t() == 'P'):
            new_t = 'V'
        else:
            new_t = self.__type
        n_x = self.__x + Triplet.get_x()
        n_y = self.__y + Triplet.get_y()
        n_z = self.__z + Triplet.get_z()
        return self.__class__(n_x,n_y,n_z,new_t)

    def mul(self, a):
        # Multiplication par un scalaire
        return self.__class__(self.__x*a,
                              self.__y*a,
                              self.__z*a,
                              self.__type
        )

    def dot(self,Triplet):
        # Produit scalaire
        if (not self.check_type('P', Triplet.get_t()) or  not self.check_type('C', Triplet.get_t())):
            print("Interdit")
            return
        sum = 0
        sum += self.__x * Triplet.get_x()
        sum += self.__y * Triplet.get_y()
        sum += self.__z * Triplet.get_z()
        return sum

    def sub(self,Triplet):
        # Soustraction
        if( not self.check_type('C', Triplet.get_t)):
            print("Interdit")
            return
        return self.add(Triplet.mul(-1))

    def cross(self,Triplet):
        # produit vectoriel
        if (not self.check_type('P', Triplet.get_t()) or not self.check_type('C', Triplet.get_t())):
            print("Interdit")
            return
        return self.__class__(
            self.__y * Triplet.get_z() - self.__z * Triplet.get_y(),
            self.__z * Triplet.get_x() - self.__x * Triplet.get_z(),
            self.__x * Triplet.get_y() - self.__y * Triplet.get_x(),
            'V'
        )

    def times(self,Triplet):
        # Produit de Schur
        if (not self.check_type('V', Triplet.get_t()) or not self.check_type('P', Triplet.get_t())):
            print("Interdit")
            return
        return self.__class__(
            self.__x * Triplet.get_x(),
            self.__y * Triplet.get_y(),
            self.__z * Triplet.get_z(),
            self.__type
        )
    
    def hat(self):
        # Normalisation
        l = self.len()
        if l == 0:
            return None
        return self.mul(1/l)
    
    def len(self):
        if (not self.check_type('P', Triplet.get_t) or not self.check_type('C', Triplet.get_t)):
            print("Interdit")
            return 0
        else:
            sum = 0
            sum += math.pow(self.__x, 2)
            sum += math.pow(self.__y, 2)
            sum += math.pow(self.__z, 2)
            return math.sqrt(sum)
    
    def get_this(self):
        return [self.__x,self.__y,self.__z]
    
    def show(self):
        print(f"{self.__type} {float(self.__x)} {float(self.__y)} {float(self.__z)}")
