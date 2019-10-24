#-------------------------------------------------------------------------------
# Name:        DestructibleObj
# Purpose:     Atari game
#
# Author:      tbeucher
#
# Created:     15/03/2016
# Copyright:   (c) tbeucher 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np

class DestructibleObj:

    def __init__(self, win):
        self.f = win
        self.widthObj = 50
        self.nbObj = 20
        self.createObj(self.nbObj)
        self.score = 0

    def createObj(self, nbObj):
        self.listOfObj = []
        cy1, cy2 = 100, 110
        nbLine = int(nbObj/10)
        for nbl in range(nbLine):
            for i in range(0, self.f.width, self.widthObj):
                obj = self.f.canv.create_rectangle(i, cy1, i+self.widthObj, cy2)
                #(obj, (x1, y1, x2, y2))
                self.listOfObj.append((obj, (i, cy1, i+self.widthObj, cy2)))
            cy1 += 10
            cy2 += 10

    def checkIfTouchDec(self, coordBall):
        for el in self.listOfObj:
            if coordBall[0][0] >= el[1][0] and coordBall[0][0] <= el[1][2] and coordBall[0][1] >= el[1][1] and coordBall[0][1] <= el[1][3]:
                #here add the score up
                #delete element
                self.f.canv.delete(el[0])
                self.listOfObj.remove(el)
                self.score += 1
                #reflect the ball
                #from left
                if coordBall[0][0] == el[1][0] and coordBall[1][0] < el[1][0]:
                    return "l"
                #from right
                if coordBall[0][0] == el[1][2] and coordBall[1][0] > el[1][0]:
                    return "r"
                #from up
                if coordBall[0][1] == el[1][1]:
                    return "u"
                #from down
                if coordBall[0][1] == el[1][3]:
                    return "d"
        return "n"
        
    
        
