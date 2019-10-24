#-------------------------------------------------------------------------------
# Name:        MoveActionBar
# Purpose:     Atari game
#
# Author:      tbeucher
#
# Created:     15/03/2016
# Copyright:   (c) tbeucher 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class MoveActionBar:

    def __init__(self, win):
        self.f = win
        self.sizeB = 60
        self.rec = win.canv.create_rectangle(win.width/2-self.sizeB/2, win.height-10, win.width/2+self.sizeB/2, win.height, fill="black")
    
    def moveUp(self, event):
        print("up")

    def moveDown(self, event):
        print("down")

    def moveLeft(self, event):
        oC = self.f.canv.coords(self.rec)
        if oC[0] > 0:
            nC = (oC[0]-10, oC[1], oC[2]-10, oC[3])
            self.f.canv.coords(self.rec, nC)
            self.f.showAndRefreshScreen()

    def moveRight(self, event):
        oC = self.f.canv.coords(self.rec)
        if oC[2] < self.f.width:
            nC = (oC[0]+10, oC[1], oC[2]+10, oC[3])
            self.f.canv.coords(self.rec, nC)
            self.f.showAndRefreshScreen()

    def checkToReflectSimple(self, coordBall):
        cB = self.f.canv.coords(self.rec)
        if coordBall[0][0] >= cB[0] and coordBall[0][0] <= cB[2] and coordBall[0][1] >= cB[1] and coordBall[0][1] <= cB[3]:
            return True
        else:
            return False

    def checkToReflect(self, coordBall, mv):
        cB = self.f.canv.coords(self.rec)
        #if we decide to divided the bar into 3 sections
        sizeS = self.sizeB/3
        if coordBall[1] == cB[1]:
            if coordBall[0] >= cB[0] and coordBall[0] < cB[0] + sizeS:
                #come from the left
                if mv[0] > 0:
                    #thinner angle
                    return [mv[0]/2, -mv[1]]
                #come from the right
                else:
                    #broader angle
                    return [mv[0], -mv[1]/2]
            elif coordBall[0] >= cB[0] + sizeS and coordBall[0] <= cB[0] + 2*sizeS:
                return [mv[0], -mv[1]]
            elif coordBall[0] > cB[0] + 2*sizeS and coordBall[0] <= cB[2]:
                if mv[0] > 0:
                    return [mv[0], -mv[1]/2]
                else:
                    return [mv[0]/2, -mv[1]]
            else:
                return [0, 0]
        else:
            return [0, 0]
        
