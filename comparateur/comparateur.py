import PIL
import operator
from PIL import Image
import sys

def compare_2_image_pil(path1,path2):
    img1 = Image.open(path1)
    px1 = img1.load()
    img2 = Image.open(path2)
    px2 = img2.load()
    new_img = Image.new("RGB",img1.size)
    h,v = img1.size
    ok = 0
    for i in range(h):
        for j in range(v):
            newpix = (px1[i,j][0] - px2[i,j][0],
                      px1[i,j][1] - px2[i,j][1],
                      px1[i,j][2] - px2[i,j][2])
            if(operator.ne(newpix,(0,0,0))):
                ok += 1
            new_img.putpixel((i,j),newpix)
    return new_img,ok

def compare_2_image_cv2(path1, path2):
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    h, v, c = img1.shape
    newimg = np.zeros((h, v, c), np.uint8)
    for i in range(h):
        for j in range(v):
            newimg[i][j] = img1[i][j] - img2[i][j]
            print(img1[i][j][0],img2[i][j][0])
            print(img1[i][j][1], img2[i][j][1])
            print(img1[i][j][2], img2[i][j][2])
            print("=========")
    return newimg

if __name__ == '__main__':
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    # new,ok = compare_2_image_pil("./image1.png","./image2.png")
    new,ok = compare_2_image_pil(path1,path2)
    # new.show()
    new.save("newimage.png")
    if (ok <= 1000):
        print("ok")
        print(ok)
    else:
        print("ko")
        print(ok)

