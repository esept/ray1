from triplet.mymath.Triplet import Triplet
from PIL import Image,ImageDraw

class Vertex(): # have to it into Triangle

    def __init__(self,nb_v,args):
        self.__l = 100
        for i in range(nb_v):
            _v = args[i]
            _v = _v.split()
            _v = list(map(int ,_v))
            v = Triplet(*_v,'P')
            self.__all_vertex.append(v)
    
    # def create_triangle(self,num_v,img,color=None):
    #     h,v = img.size
    #     draw = ImageDraw.Draw(img)
    #     xy = []
    #     for i in num_v:
    #         self.__all_vertex[i].show()
    #         xy.append(self.calcul((h/2,v/2),self.__all_vertex[i]))
    #     print(xy)
    #     draw.polygon(xy,fill=color)
    #     return img
    
    # def create_triangle(self, img, point1, point2, point3, color=None):
    #     draw = ImageDraw.Draw(img)
    #     vertices = [tuple(point1), tuple(point2), tuple(point3)]
    #     print(vertices)
    #     draw.polygon(vertices, outline='red', fill=color)
    #     img.show()
    #     return img