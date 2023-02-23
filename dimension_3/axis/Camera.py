from triplet.mymath import Triplet
class Camera:
    __from = Triplet
    __at = Triplet
    __up = Triplet
    __degre = int
    
    def __init__(self,camera_args):
        self.__from = Triplet(int(camera_args[0]), int(camera_args[2]), int(camera_args[4]),'P')
        self.__at = Triplet(int(camera_args[6]), int(camera_args[8]), int(camera_args[10]),'P')
        self.__up = Triplet(int(camera_args[12]), int(camera_args[14]), int(camera_args[16]),'V')
        self.__degre = int(camera_args[18:])
        
    
    def show(self):
        print("this camera look from : ",end='')
        self.__from.show()
        print("this camera look at : ", end='')
        self.__at.show()
        print("this camera up: ", end='')
        self.__up.show()
        print("degree: ",end='')
        print(self.__degre)

    