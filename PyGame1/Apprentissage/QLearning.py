import numpy as np


class QLearning:

    def __init__(self):
        self.nom = "QLearning"
        #learning rate
        self.lr = 0.8
        #discount factor
        self.df = 0.1
        #decrease step
        self.ds = 0.99

    def setStatePlat(self):
        #must be set before using getState
        platList = []
        for i in range(self.fen.width**2):
            platList.append(i)
        self.plat = np.asarray(platList).reshape(self.fen.width, self.fen.width)

    def getState(self, obj):
        coord = self.fen.canv1.coords(obj)
        xCenter = coord[0] + (coord[2]-coord[0])/2
        yCenter = coord[1] + (coord[3]-coord[1])/2
        pos = self.plat[xCenter, yCenter]
        return pos

    def setFen(self, fen):
        #must be set before using QL
        self.fen = fen

    def setCir(self, cir):
        #must be set before using QL
        self.cir = cir

    def QL1(self):
        #Knowing the number of possible states
        self.Q = np.zeros((self.fen.width, 4))
        self.s = self.getState(self.cir)
        #for e-greedy policy
        eps = 1
        for i in range(15):
            c = np.random.rand()
            if c < self.eps:
                #exploration
                a = np.ceil(np.random.rand()*4)
            else:
                #exploitation
                break
            eps = eps*self.ds
        
