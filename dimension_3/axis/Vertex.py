from triplet.mymath import Triplet
from PIL import Image,ImageDraw

class Vertex():
    __all_vertex = []
    
    def __init__(self,nb_v,args):
        self.__l = 100
        for i in range(nb_v):
            _v = args[i]
            _v = _v.split()
            _v = list(map(int ,_v))
            v = Triplet(*_v,'P')
            self.__all_vertex.append(v)
            
    def show(self):
        for i in range(len(self.__all_vertex)):
            self.__all_vertex[i].show()
    
    def calcul(self,hv,Triplet):
        x = Triplet.get_x()
        y = Triplet.get_y()
        return (hv[0] + x*self.__l,hv[1] + y*self.__l)
    
    def create_triangle(self,num_v,img,color=None):
        h,v = img.size
        draw = ImageDraw.Draw(img)
        xy = []
        for i in num_v:
            self.__all_vertex[i].show()
            xy.append(self.calcul((h/2,v/2),self.__all_vertex[i]))
        print(xy)
        draw.polygon(xy,fill=color)
        return img