import math

class Triplet:
    # __type = None
    __x = 0
    __y = 0
    __z = 0
    
    def __init__(self,x,y,z):
        # self.__type = t
        self.__x = x
        self.__y = y
        self.__z = z
    
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_z(self):
        return self.__z

    # def add_new(self,Triplet):
    #     n_x = self.__x + Triplet.get_x()
    #     n_y = self.__y + Triplet.get_y()
    #     n_z = self.__z + Triplet.get_z()
    #     return
    
    def add(self,Triplet):
        self.__x = self.__x + Triplet.get_x()
        self.__y = self.__y + Triplet.get_y()
        self.__z = self.__z + Triplet.get_z()
        
    def add_V(self,Vector):
        n_x = self.__x + Vector.get_x()
        n_y = self.__y + Vector.get_y()
        n_z = self.__z + Vector.get_z()
        return Triplet(n_x,n_y,n_z)
        
    def mul(self,a):
        self.__x = a * self.__x
        self.__y = a * self.__y
        self.__z = a * self.__z
    
    def show(self):
        # print("[",self.__x,",",self.__y,",",self.__z,"]")
        print(f"[{self.__x},{self.__y},{self.__z}]")
        
    
        

class Vector(Triplet):
    __type = 'V'
    __x = 0
    __y = 0
    __z = 0
    
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.__x = x
        self.__y = y
        self.__z = z
    
    def show(self):
        print(f"V[{self.__x},{self.__y},{self.__z}]")
        # print("V","[",self.__x,',',self.__y,',',self.__z,"]")
    
    def len(self):
        sum = 0
        sum += math.pow(self.__x,2)
        sum += math.pow(self.__y, 2)
        sum += math.pow(self.__z, 2)
        return math.sqrt(sum)
    
    def hat(self):
        l = self.len()
        self.mul(1/l)
        
    
    def mul(self,a):
        self.__x = a * self.__x
        self.__y = a * self.__y
        self.__z = a * self.__z
    
    def dot(self):
        # produit scalaire
        pass
    
    def sub(self):
        # product soustraction
        pass
    
    def cross(self):
        # produit vectoriel
        pass
    
    def times(self):
        pass
    # produit de schur

    def hat(self):
        pass
    # normalisation
    
    # def add(self,Triplet):
    #     return

    