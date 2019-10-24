


class Circle:
    
    def __init__(self, fen1):
        self.nom = "circle"
        self.fen = fen1
        self.canv = fen1.canv1
        self.sizeI = 20
        self.c1 = self.drawcircle(fen1.width/2, fen1.height/2, self.sizeI)
        self.moveScale = 5
        self.size = 1
        self.growSize = 5
        self.event()
        
    def drawcircle(self, x,y,rad):
        cir = self.canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='black')
        return cir

    def drawcircleColor(self, x,y,rad, color):
        cir = self.canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill=color)
        return cir
        
    def grow(self):
        #not working well
        self.size += self.growSize
        self.canv.itemconfig(self.c1, width=self.size)

    def grow2(self):
        coords = self.canv.coords(self.c1)
        self.canv.coords(self.c1, (coords[0]-self.growSize, coords[1]-self.growSize, coords[2]+self.growSize, coords[3]+self.growSize))
        
    #===========================================================================
    # def moveForWard(self, objCanvas, objToMove, x, y):
    #     objCanvas.move(objToMove, x, y)
    #     objCanvas.update()
    #===========================================================================
        
    def moveUp(self):
        self.canv.move(self.c1, 0, -self.moveScale)
        self.canv.update()
    
    def moveDown(self):
        self.canv.move(self.c1, 0, self.moveScale)
        self.canv.update()
    
    def moveLeft(self):
        self.canv.move(self.c1, -self.moveScale, 0)
        self.canv.update()
    
    def moveRight(self):
        self.canv.move(self.c1, self.moveScale, 0)
        self.canv.update()
        
    def rootProc(self, choix):
        if choix == 0:
            self.moveUp()
        elif choix == 1:
            self.moveDown()
        elif choix == 2:
            self.moveLeft()
        elif choix == 3:
            self.moveRight()
        else:
            print("Erreur de route !")
            
    def moveUpEvent(self, event):
        if not self.checkBordure()==3:
            self.moveUp()
            self.checkIfFoodHere()
            
    def moveDownEvent(self, event):
        if not self.checkBordure()==4:
            self.moveDown()
            self.checkIfFoodHere()

    def moveLeftEvent(self, event):
        if not self.checkBordure()==1:
            self.moveLeft()
            self.checkIfFoodHere()

    def moveRightEvent(self, event):
        if not self.checkBordure()==2:
            self.moveRight()
            self.checkIfFoodHere()
            
    def event(self):
        self.fen.fen1.bind("<Up>", self.moveUpEvent)
        self.fen.fen1.bind("<Down>", self.moveDownEvent)
        self.fen.fen1.bind("<Left>", self.moveLeftEvent)
        self.fen.fen1.bind("<Right>", self.moveRightEvent)

    def setFood(self, food):
        self.food = food
        
    def checkIfFoodHere(self):
        foodList = self.food.getFoodList()
        for el in foodList:
            coordFood = self.canv.coords(el)
            coordPredator = self.canv.coords(self.c1)
            if(coordFood[0]>=coordPredator[0] and coordFood[1]>=coordPredator[1] and coordFood[2]<=coordPredator[2] and coordFood[3]<=coordPredator[3]):
                self.grow2()
                self.food.deleteFood(el)

    def checkBordure(self):
        coords = self.canv.coords(self.c1)
        maxc = self.fen.width
        xCenter = coords[0] + (coords[2]-coords[0])/2
        yCenter = coords[1] + (coords[3]-coords[1])/2
        if(xCenter<=1):
            return 1
        if(xCenter>=maxc-1):
            return 2
        if(yCenter<=1):
            return 3
        if(yCenter>=maxc-1):
            return 4
        return 0
