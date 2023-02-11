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
        
    def check_type(self,param_type,this_type,func_name):
        if self.__type == this_type or param_type == this_type:
            print("Non "+func_name+" en "+ this_type)
            return
    
    def check_same_type(self,param_type):
        if self.__type != param_type :
            print("Error: note same type"+self.get_t()+" "+param_type)
            return
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    
    def get_t(self):
        return self.__type

    def add(self, Triplet):
        # self.check_type(Triplet.get_t, 'P', sys._getframe().f_code.co_name)
        self.check_same_type(Triplet.get_t())
        if( self.__type == 'P' and Triplet.get_t() == 'P'):
            new_t = 'V'
        else:
            new_t = self.__type
        n_x = self.__x + Triplet.get_x()
        n_y = self.__y + Triplet.get_y()
        n_z = self.__z + Triplet.get_z()
        return self.__class__(n_x,n_y,n_z,new_t)
        
    
    def mul(self, a):
        return self.__class__(self.__x*a,
                              self.__y*a,
                              self.__z*a,
                              self.__type
        )

    def dot(self,Triplet):
        sum = 0
        sum += self.__x * Triplet.get_x()
        sum += self.__y * Triplet.get_y()
        sum += self.__z * Triplet.get_z()
        return sum

    def sub(self,Triplet):
        return self.add(Triplet.mul(-1))

    def cross(self,Triplet):# produit vectoriel
        return self.__class__(
            self.__y * Triplet.get_z() - self.__z * Triplet.get_y(),
            self.__z * Triplet.get_x() - self.__x * Triplet.get_z(),
            self.__x * Triplet.get_y() - self.__y * Triplet.get_x(),
            'V'
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
        self.check_type(Triplet.get_t, 'P', sys._getframe().f_code.co_name)
        self.check_type(Triplet.get_t, 'C', sys._getframe().f_code.co_name)

        sum = 0
        sum += math.pow(self.__x, 2)
        sum += math.pow(self.__y, 2)
        sum += math.pow(self.__z, 2)
        return math.sqrt(sum)
    
    def get_this(self):
        return [self.__x,self.__y,self.__z]
    
    def show(self):
        print(f"[{self.__x},{self.__y},{self.__z},{self.__type}]")

