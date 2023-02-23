import sys
from Vecteur import *

def build_object(s):
    data = s.split(" ")
    if data[0] == 'P':
        obj_type = Point
    elif data[0] == 'V':
        obj_type = Vecteur
    elif data[0] == 'C':
        obj_type = Couleur
    else:
        print("Argument non autorisé !")
        return
    
    obj = obj_type(float(data[1]), float(data[2]), float(data[3]))
    return obj

def main():
    data = sys.argv[1].split(",") 
    operation = data[1]
    o1 = build_object(data[0])
    if(operation=="mul" and len(data[2])==1 and data[2].isdigit()):
        o2 = float(data[2])
    else:
        o2 = build_object(data[2])

    try:
        o3 = getattr(o1, operation)(o2)
        print(o3)
    except:
        print("Interdit")

if __name__ == "__main__":
    main()