#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Atari game
#
# Author:      tbeucher
#
# Created:     15/03/2016
# Copyright:   (c) tbeucher 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import time

tmp = os.getcwd()
path = tmp[:tmp.rfind("\\")] + "/LIB/"
sys.path.append(path)

from Windows import Window
from MoveActionBar import MoveActionBar
from BallDynamics import Ball
from DestructibleObj import DestructibleObj

def main():
    w = Window()
    mo = MoveActionBar(w)
    decor = DestructibleObj(w)
    ball = Ball(w, mo, decor)
    w.showAndRefreshScreen()
    w.event(mo.moveUp, mo.moveDown, mo.moveLeft, mo.moveRight)
    stopC = False
    while stopC == False and decor.score < decor.nbObj:
        stopC = ball.moveBall()
        w.showAndRefreshScreen()
        time.sleep(0.005)
    w.closeWindow()
    print("Votre score est de : ", decor.score)
    #w.win.mainloop()


if __name__ == '__main__':
    main()
