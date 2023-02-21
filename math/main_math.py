# from math1 import Triplet
# from math1 import Vector
from mymath import *

def create_(tab):
    if tab[0] == 'V':
        var = Vector(int(tab[1]),int(tab[2]),int(tab[3]))
    else:
        var = 3
    return var


def test_add():
    p1 = Triplet(1,1,1,'P')
    p2 = Triplet(1,2,1,'P')
    p3 = p1.add(p2)
    p3.show()
    v1 = Triplet(1,1,1,'V')
    v2 = Triplet(1,2,1,'V')
    v3 = v1.add(v2)
    v3.show()
    c1 = Triplet(1,1,1,'C')
    c2 = Triplet(2,2,2,'C')
    c3 = c1.add(c2)
    c3.show()
   
def test_sub():
    p1 = Triplet(1,1,1,'P')
    p2 = Triplet(1,2,1,'P')
    p3 = p1.sub(p2)
    p3.show()
    v1 = Triplet(1,1,1,'V')
    v2 = Triplet(1,2,1,'V')
    v3 = v1.sub(v2)
    v3.show()
    c1 = Triplet(1,1,1,'C')
    c2 = Triplet(2,2,2,'C')
    c3 = c1.sub(c2)
    # c3.show()

def test_mul():
    n1 = 3
    p1 = Triplet(1,1,1,'P')
    p3 = p1.mul(n1)
    p3.show()
    v1 = Triplet(1,1,1,'V')
    v3 = v1.mul(n1)
    v3.show()
    c1 = Triplet(1,1,1,'C')
    c3 = c1.mul(n1)
    c3.show()

def test_dot():
    p1 = Triplet(1,1,1,'P')
    p2 = Triplet(1,2,1,'P')
    p3 = p1.dot(p2)
    # p3.show()
    v1 = Triplet(1,1,1,'V')
    v2 = Triplet(1,2,1,'V')
    v3 = v1.dot(v2)
    # v3.show()
    c1 = Triplet(1,1,1,'C')
    c2 = Triplet(2,2,2,'C')
    c3 = c1.dot(c2)
    # c3.show()
    print(p3,v3,c3)

def test_cross():
    p1 = Triplet(1,1,1,'P')
    p2 = Triplet(1,2,1,'P')
    p3 = p1.cross(p2)
    # p3.show()
    v1 = Triplet(1,1,1,'V')
    v2 = Triplet(1,2,1,'V')
    v3 = v1.cross(v2)
    v3.show()
    c1 = Triplet(1,1,1,'C')
    c2 = Triplet(2,2,2,'C')
    c3 = c1.cross(c2)
    # c3.show()

def test_times():
    p1 = Triplet(1,1,1,'P')
    p2 = Triplet(1,2,1,'P')
    p3 = p1.times(p2)
    # p3.show()
    v1 = Triplet(1,1,1,'V')
    v2 = Triplet(1,2,1,'V')
    v3 = v1.times(v2)
    # v3.show()
    c1 = Triplet(1,1,1,'C')
    c2 = Triplet(2,2,2,'C')
    c3 = c1.times(c2)
    c3.show()

def test_len():
    p1 = Triplet(1,1,1,'P')
    p3 = p1.len()
    v1 = Triplet(1,1,1,'V')
    v3 = v1.len()
    c1 = Triplet(1,1,1,'C')
    c3 = c1.len()
    print(p3,v3,c3)

def test_hat():
    p1 = Triplet(1,1,1,'P')
    p3 = p1.hat()
    v1 = Triplet(1,1,1,'V')
    v3 = v1.hat()
    c1 = Triplet(1,1,1,'C')
    c3 = c1.hat()
    v3.show()
    # print(p3,v3,c3)


def test_all():
    # test_add()
    test_sub()
    # test_mul()
    # test_dot()
    # test_cross()
    # test_times()
    # test_len()
    # test_hat()
    
if __name__ == '__main__':
    test_all()
    