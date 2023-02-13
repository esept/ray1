class Point(Triplet):

    def __init__(self, t, x, y, z):
        Triplet.__init__(self, 'P', x, y, z)

    def sub(self,Triplet):
        return self.add(Triplet.mul(-1))