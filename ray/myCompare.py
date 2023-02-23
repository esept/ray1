from PIL import Image

def read (path): 
    img = Image.open(path)
    print(img)
    
    try:
        # r, v, b = img.split()
        # r.show()
        # v.show()
        # b.show()
        img.show()
    except IOError:
        print("Erreur lors de l'affichage !")
        
# read("image1.png")

def imgInfo (path): 
    image = Image.open(path)
    print( "Le format de l'image :", image.format )
    print( "Le mode de l'image:", image.mode )
    print( "La taille de l'image:", image.size )
    print( "Largeur : {} pixel, hauteur : {} pixel".format( image.width, image.height) )
# imgInfo ("image1.png")

def modifImg (img):
    # Créer une copie de l’image
    img = image.copy()
    # Changer la taille (largeur, hauteur)
    size = (500, 500)
    img = img.resize( size )

def cmpImg(image1, image2):
    # pixels = img.getpixel((0,0))
    # print(pixels)
    # img.putpixel((0,0), (255, 0, 0))
    # check si img1.width = img2.width && img1.height == img2.height

    # créer une matrice img1.width*img1.height
    # créer une seconde matrice img2.width*img2.height
    img1 = Image.open(image1)
    img2 = Image.open(image2)
    

    width, height = img1.size
    img3 = Image.new('RGB', (width, height)) # diff
    # img3.show()
    cpt = 0
    for i in range(img1.width):
        for j in range(img1.height):
            px1 = img1.getpixel((i,j))
            px2 = img2.getpixel((i,j))

            if(px1!=px2):
                # r1, v1, b1 = img1.split()
                # r2, v2, b2 = img2.split()
                # r1.show()
                # v1.show()
                # b1.show()
                cpt += 1
                img3.putpixel((i,j), (r1-r2, v1-v2, b1-b2))
            else:
                img3.putpixel((i,j), (0, 0, 0))
    img3.show()

    return cpt

# def createDiff(image1, image2):
#     newImg = image1.copy()
#     return 

print(cmpImg("TEST1/image1.png", "TEST1/image2.png"))

# python3 compare.py

# https://info.blaisepascal.fr/pillow
# https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-les-bases-de-traitement-dimages-en-python-bibliothque-pillow#_Toc56500463