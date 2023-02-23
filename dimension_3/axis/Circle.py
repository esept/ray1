from triplet.mymath import Triplet
from PIL import Image,ImageDraw

class Circle:
    __x: int
    __y: int
    __r: int
    __s: int
    
    def __init__(self,Triplet,r,scala):
        self.__x = Triplet.get_x()
        self.__y = Triplet.get_y()
        self.__r = r
        self.__s = scala
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_r(self):
        return self.__r
    
    def show(self):
        print("circle:[x=",self.__x,",y=",self.__y,",r=",self.__r,"]")
    
    def draw_circle(self,img,color):
        h,v = img.size
        draw = ImageDraw.Draw(img)
        xy1 = [h/2 + self.__r * self.__s,v/2 + self.__r * self.__s]
        xy2 = [h/2 - self.__r * self.__s,v/2 - self.__r * self.__s]
        draw.ellipse([*xy2,*xy1], fill=color)
        return img