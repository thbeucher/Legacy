
from Actions.CircleCreation import Circle

import numpy as np

class foodCircle(Circle):
    
    def __init__(self, fen):
        self.fene = fen
        self.fen = fen.fen1
        self.canv = fen.canv1
        self.size = 5
        self.color = 'green'
        self.nbFood = 10
        self.putFood()

    def putFood(self):
        #Get coords for the food
        coords = np.random.random_integers(0, self.fene.width, [self.nbFood,2])
        self.foodList = [self.drawcircleColor(el[0], el[1], self.size, self.color) for el in coords]

    def getFoodList(self):
        return self.foodList

    def deleteFood(self, foodToDelete):
        self.canv.delete(foodToDelete)
        self.foodList.remove(foodToDelete)

    def setFoodList(self, foodList):
        self.foodList = foodList
