import Triplet
class Vector(Triplet):
    __type = 'V'
    __x = 0
    __y = 0
    __z = 0
    
    def __init__(self,x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z
        
    # def _0543_add__(self, other):