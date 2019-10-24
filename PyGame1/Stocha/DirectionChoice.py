#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np



def dirChoice():
    choix = 0
    alea = np.random.rand(1)
    if alea[0] >= 0 and alea[0] < 0.25:
        choix = 0 #Vers le haut
    elif alea[0] >= 0.25 and alea[0] < 0.5:
        choix = 1 #Vers le Bas
    elif alea[0] >= 0.5 and alea[0] < 0.75:
        choix = 2 #Vers la gauche
    elif alea[0] >= 0.75 and alea[0] <= 1:
        choix = 3 #Vers la droite
    else:
        print("Erreur de valeur al�atoire !")
    return choix
	
def move(objCanvas, objToMove, x, y):
    objCanvas.move(objToMove, x, y)
    objCanvas.update()
	