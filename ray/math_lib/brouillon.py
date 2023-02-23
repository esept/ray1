# def check_validity(self, triplet):
    #     if (not (triplet.get_t == 'P' or triplet.get_t() == 'V')):
    #         return False
    #     return True

    # some kind of redefinition (surcharge)
    # def sub(self, triplet, isVector=None): 
    #     if (not (triplet.get_t == 'P' or triplet.get_t() == 'V')):
    #         print("Interdit")
    #         return

    #     #triplet = point ou vecteur
    #     n_x = self.get_x() - triplet.get_x()
    #     n_y = self.get_y() - triplet.get_y()
    #     n_z = self.get_z() - triplet.get_z()

    #     if(isVector):
    #         return Point('P', n_x, n_y, n_z)
    #     return Vecteur('V', n_x, n_y, n_z)


    # def create_(tab):
    # if tab[0] == 'V':
    #     var = Vector(int(tab[1]),int(tab[2]),int(tab[3]))
    # else:
    #     var = 3
    # return var

# if __name__ == '__main__':
    # n1 = Triplet(1,1,1)
    # n2 = Triplet(1,2,3)
    # n3 = Triplet(2,3,4)
    # v1 = Triplet('V',1,0,0)
    # v2 = Triplet('V',0,1,0)
    # v3 = v1.cross(v2)
    # v1.show()
    # v2.show()
    # v3.show()
    # n1.show()
    # n2.show()
    # n3.show()
    #

# print('c\'est un V')
        # try:
        #     # print(self.__x, self.__y, self.__z)
        #     print(self.get_x(), self.get_y(), self.get_z())
        # except:
        #     print("what's going on here ?")


# def add(self, triplet): # Point
    #     # triplet doit être un vecteur !
    #     if not ((self.get_t()=='P' and triplet.get_t()=='V') or (self.get_t()=='V' and triplet.get_t()=='V')):
    #         raise ValueError
        
    #     n_x = self.get_x() + triplet.get_x()
    #     n_y = self.get_y() + triplet.get_y()
    #     n_z = self.get_z() + triplet.get_z()
    #     return Point(n_x, n_y, n_z)