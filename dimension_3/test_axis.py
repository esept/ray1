from axis import Camera,Vertex
from axis import Circle
from PIL import Image,ImageDraw
from triplet.mymath import Triplet

def create_new_image(size_h,size_v):
    new_img = Image.new('RGB',(size_h,size_v),color=(0,0,0))
    return new_img

def save_image(new_img,path = "./output.png"):
    new_img.save(path)

def test_circle(img):
    t = Triplet(0,0,0,'P')
    c1 = Circle(t,2,100)
    c1.draw_circle(img,(0,255,255))
    return img

def test_triangle(img):
    vertex_nb = 4
    vertex1 = "-1 -1 0"
    vertex2 = "+1 -1 0"
    vertex3 = "+1 +1 0"
    vertex4 = "-1 +1 0"
    _myV = Vertex(vertex_nb,[vertex1,vertex2,vertex3,vertex4])
    _myV.show()
    _myV.create_triangle([0,1,2],img,(255,0,0))
    _myV.create_triangle([0,2,3],img,(255,0,0))
    return _img

def test_camera():
    camera_args = "0 0 4 0 0 0 0 1 0 45"
    _camera = Camera(camera_args)
    _camera.show()

if __name__ == '__main__':
    my_img = create_new_image(640,480)
    test_camera()
    test_circle(my_img)
    save_image(my_img,"test_axis_circle.png")