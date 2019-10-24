import tkinter as tk
import time
from Stocha.DirectionChoice import dirChoice
from FoodClass.FoodCircle import foodCircle
from Actions.CircleCreation import Circle


class fenetreC:
    
    def __init__(self):
        self.width = 500
        self.height = 500
        self.fen1 = tk.Tk()
        self.canv1 = tk.Canvas(self.fen1, width = self.width, height = self.height)
        self.canv1.pack()
        
fene = fenetreC()

cir1 = Circle(fene)

food = foodCircle(fene)
cir1.setFood(food)

#for i in range(20):
    #time.sleep(0.5)
    #choix = dirChoice()
    #cir1.rootProc(choix)
    #cir1.grow2()
               
fene.fen1.mainloop()
