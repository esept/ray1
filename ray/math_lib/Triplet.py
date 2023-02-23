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

    def get_t(self):
        return self.__type

    def mul(self, a):
        return self.__class__(self.__x*a,
            self.__y*a,
            self.__z*a)

    def __str__(self):
        return self.__type + f" {self.__x} {self.__y} {self.__z}"
