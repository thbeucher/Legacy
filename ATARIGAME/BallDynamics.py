#-------------------------------------------------------------------------------
# Name:        BallDynamics
# Purpose:     Atari game
#
# Author:      tbeucher
#
# Created:     15/03/2016
# Copyright:   (c) tbeucher 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np

class Ball:

    def __init__(self, win, moveBar, decor):
        self.f = win
        self.moveBar = moveBar
        self.dec = decor
        self.sizeB = 10
        self.ball = self.f.drawcircleColor(self.f.height/2+5, self.f.width/2, self.sizeB)
        self.fixedObjToCheck()
        #[t, t-1]
        self.coordBall = [np.asarray([self.f.height/2+5, self.f.width/2]), np.asarray([self.f.height/2+6, self.f.width/2+1])]

    def fixedObjToCheck(self):
        self.leftWall = [0, 0, 0, self.f.height]
        self.rightWall = [self.f.width, self.f.width, 0, self.f.height]
        self.roof = [0, self.f.width, 0, 0]
        self.ground = [0, self.f.width, self.f.height, self.f.height]

    def moveBall(self):
        mv = self.coordBall[0] - self.coordBall[1]
        self.coordBall[1] = self.coordBall[0]
        touchDec = self.dec.checkIfTouchDec(self.coordBall)
        touchBar = self.moveBar.checkToReflect(self.coordBall[0], mv)
        if self.checkIfTouch(self.ground):
            return True
        elif touchDec != "n":
            if touchDec == "l" or touchDec == "r":
                self.coordBall[0] = self.coordBall[0] + [-mv[0], mv[1]]
            elif touchDec == "u" or touchDec == "d":
                self.coordBall[0] = self.coordBall[0] + [mv[0], -mv[1]]
        elif touchBar != [0, 0]:
            self.coordBall[0] = self.coordBall[0] + touchBar
        elif self.checkIfTouch(self.leftWall) or self.checkIfTouch(self.rightWall):
            self.coordBall[0] = self.coordBall[0] + [-mv[0], mv[1]]
        elif self.checkIfTouch(self.roof):# or self.moveBar.checkToReflectSimple(self.coordBall):
            self.coordBall[0] = self.coordBall[0] + [mv[0], -mv[1]]
        else:
            self.coordBall[0] = self.coordBall[0] + mv
        if self.coordBall[0][0] < 0 or self.coordBall[0][0] > self.f.width or self.coordBall[0][1] < 0 or self.coordBall[0][1] > self.f.height:
            self.coordBall[0] = self.coordBall[0] - mv
        newCoord = (self.coordBall[0][0] - 10, self.coordBall[0][1] - 10, self.coordBall[0][0] + 10, self.coordBall[0][1] + 10)
        self.f.canv.coords(self.ball, newCoord)
        return False

    def checkIfTouch(self, obj):
        if self.coordBall[0][0] >= obj[0] and self.coordBall[0][0] <= obj[1] and self.coordBall[0][1] >= obj[2] and self.coordBall[0][1] <= obj[3]:
            return True
        else:
            return False

        



        
