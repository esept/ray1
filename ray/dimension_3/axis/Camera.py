from triplet.mymath.Triplet import Triplet

class Camera:
    __from = Triplet
    __at = Triplet
    __up = Triplet
    __degre = int
    
    def __init__(self,camera_args):
        self.__from = Triplet(camera_args[0], camera_args[1], camera_args[2],'P')
        self.__at = Triplet(camera_args[3], camera_args[4], camera_args[5],'P')
        self.__up = Triplet(camera_args[6], camera_args[7], camera_args[8],'V')
        self.__degre = int(camera_args[9])
    
    def show(self):
        print("this camera look from : ",end='')
        self.__from.show()
        print("this camera look at : ", end='')
        self.__at.show()
        print("this camera up: ", end='')
        self.__up.show()
        print("degree: ",end='')
        print(self.__degre)

    def infos(self):
        self.__from.infos()
        self.__at.infos()
        self.__up.infos()
        print()
        print(self.__degre)