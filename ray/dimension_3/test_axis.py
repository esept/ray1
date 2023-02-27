from axis.Camera import Camera
# from axis.Vertex import Vertex
from axis.Circle import Circle
from PIL import Image,ImageDraw
from triplet.mymath.Triplet import Triplet
from math_lib.Vecteur import Vecteur
import re # expr. regulières
import traceback

def create_new_image(size_h,size_v):
    new_img = Image.new('RGB',(size_h,size_v),color=(0,0,0))
    return new_img

def save_image(new_img,path):
    new_img.save(path)

def test_circle(img, spheres):
    for s in spheres:
        t = Triplet(s[0],s[1],s[2],'P') 
        c = Circle(t,s[3],100) # s[3] = rayon
        c.draw_circle(img,(0,255,255))
    return img

# tenir compte du dégré
def create_triangle(img, pt1, pt2, pt3, color=None):
    draw = ImageDraw.Draw(img)
    vertices = [tuple(pt1), tuple(pt2), tuple(pt3)]
    # print(vertices)
    draw.polygon(vertices, outline='red', fill=color)
    # img.show()
    return img

def test_triangle(img, triangle_pts, vertex):
    # for i in range(len(triangle_pts)):
    #     print(triangle_pts[i])
    # for e in vertex:
    #     print(e)
    img = create_triangle(img, 
        # vertex[triangle_pts[0]],
        # vertex[triangle_pts[1]],
        # vertex[triangle_pts[2]],
        #testing...
        # [vertex[triangle_pts[0]][0]+20, vertex[triangle_pts[0]][1]+100],
        # [vertex[triangle_pts[1]][0]+20, vertex[triangle_pts[1]][1]+400],
        # [vertex[triangle_pts[2]][0]+200, vertex[triangle_pts[2]][1]+300],
        [vertex[triangle_pts[0]][0], vertex[triangle_pts[0]][1]],
        [vertex[triangle_pts[1]][0], vertex[triangle_pts[1]][1]],
        [vertex[triangle_pts[2]][0], vertex[triangle_pts[2]][1]],
        (255,0,0) 
    ) 
    return img

def test_camera(camera_args=[0, 0, 4, 0, 0, 0, 0, 1, 0, 45]):
    _camera = Camera(camera_args)
    # _camera.show()

#parse un fichier et crée une image
def parse_file(openfile="TEST3/test1.scene"):
    # initialisation des valeurs par défaut
    width, height = 0, 0
    filename = "output.png"
    camera_infos = []
    # camera_position = [0, 0, 4]
    # camera_lookat = [0, 0, 0]
    # camera_up = [0, 1, 0]
    # camera_fov = 45
    declared_objs = 0
    sources_of_ligth = 0
    maxverts = 0

    # couleurs par défaut
    ambient = [0, 0, 0]
    diffuse = [0, 0, 0]
    specular = [0, 0, 0]
    shininess = 10

    # lumières par défaut
    directional = [[0, 0, 0], [0, 0, 0]]
    point = [[0, 0, 0], [0, 0, 0]]

    # obj de scènes (triangles ou sphères)
    vertex = []
    triangles = []
    spheres = []

    plane = []

    try:
        # on parse d'abord le fichier ...
        # ouverture et lecture du fichier
        with open(openfile, "r") as file:
            lines = file.readlines()

        cpt_lig = 0
        # parcours des lignes du fichier
        for line in lines:
            cpt_lig += 1
            # suppression des commentaires
            line = re.sub(r"#.*", "", line).strip()

            # taille de l'image
            if line.startswith("size"):
                _, w, h = line.split()
                width = int(w)
                height = int(h)

            # nom de fichier de sortie
            elif line.startswith("output"):
                _, filename = line.split()

            # infos de la caméra
            elif line.startswith("camera"):
                _, cx, cy, cz, ux, uy, uz, mx, my, mz, fov = line.split()
                camera_infos = [float(cx), float(cy), float(cz),  # cam_pos
                    float(ux), float(uy), float(uz), # cam_lookat
                    float(mx), float(my), float(mz), # cam_up
                    float(fov) # cam_fov
                ]
                # camera_position = [float(cx), float(cy), float(cz)]
                # camera_lookat = [float(ux), float(uy), float(uz)]
                # camera_up = [float(mx), float(my), float(mz)]
                # camera_fov = int(fov)

            # infos de la lumière ambiante
            elif line.startswith("ambient"):
                _, r, g, b = line.split()
                ambient = [float(r), float(g), float(b)]
            
            # infos de la réflexion diffuse
            elif line.startswith("diffuse"):
                _, r, g, b = line.split()
                diffuse = [float(r), float(g), float(b)]

            # infos de la réflexion spéculaire
            elif line.startswith("specular"):
                _, r, g, b = line.split()
                specular = [float(r), float(g), float(b)]

            # infos de la réflexion shininess
            elif line.startswith("shininess"):
                _, s = line.split()
                shininess = s

            # infos de la lumière directionnelle
            elif line.startswith("directional"):
                sources_of_ligth += 1
                _, dx, dy, dz, r, g, b = line.split()
                directional = [[float(dx), float(dy), float(dz)], [float(r), float(g), float(b)]]

            # infos de la lumière ponctuelle
            elif line.startswith("point"):
                sources_of_ligth += 1
                _, px, py, pz, r, g, b = line.split()
                point = [[float(px), float(py), float(pz)], [float(r), float(g), float(b)]]
            
            # récup. de la val. maxverts
            elif line.startswith("maxverts"):
                _, mv = line.split()
                maxverts = mv

            # coords des points
            elif line.startswith("vertex"):
                _, vx, vy, vz = line.split()
                vertex.append([float(vx), float(vy), float(vz)])
            
            # infos de la lumière ponctuelle
            elif line.startswith("tri"):
                _, tx, ty, tz = line.split()
                triangles.append([int(tx), int(ty), int(tz)])
            
            # infos de la sphère
            elif line.startswith("sphere"):
                _, sx, sy, sz, r = line.split()
                spheres.append([float(sx), float(sy), float(sz), float(r)])
            
            # infos du plan
            elif line.startswith("plane"):
                _, px, py, pz, pu, pv, pw = line.split()
                plane.append([float(px), float(py), float(pz), float(pu), float(pv), float(pw)])

            # checking on: ambient + diffuse, sources of color, < maxverts
            # if()
        
        my_img = create_new_image(width,height)
        test_camera(camera_infos) # camera_infos
        test_circle(my_img, spheres)    
        for tri in triangles:
            test_triangle(my_img, tri, vertex) # img, pts du triangle, liste de tous les pts
          
        save_image(my_img,filename)

        # affichage des infos
        print(filename)
        print(width*height)
        # print(camera_fov)
        print(declared_objs)
        print(sources_of_ligth)
        
    except Exception as e:
        tb = traceback.format_exc()
        print("\nSOME ERROR <<", type(e).__name__, ">> OCCURED.")
        print(tb)
        exit()
    
parse_file("OTHER_TESTS_SCENE/t2")