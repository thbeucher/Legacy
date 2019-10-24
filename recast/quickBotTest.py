#quickBotTest

import recastai as re
try:
    import tkinter as tk #python3
except:
    import Tkinter as tk #python2
from collections import deque
#from SpellChecker import correction
from BrowserAcces import Browser


class MyBot:
    def __init__(self):
        self.token = 'a3338eb1d90ffcfea15a3f03e35d4bc3'
        self.client = re.Client(self.token, 'en')
        self.response = self.client.text_converse("hi")
        self.my_conv_token = self.response.conversation_token

        self.memoryDict = {}

        self.intentAnalyse = []

    def setQuestion(self, question):
        self.response = self.client.text_converse(question, conversation_token=self.my_conv_token)

    def getReponse(self):
        return self.response.reply() if self.response.reply() != None else "connection pb"

    def getMemory(self):
        mem = self.response.get_memory()
        if len(mem) > 0:
            for el in self.response.get_memory():
                elmts = vars(el)
                self.memoryDict[elmts['name']] = elmts

    def getAnalyse(self, request):
        response = self.client.text_request(request)
        [self.intentAnalyse.append((el.slug, el.confidence)) for el in response.intents]
        entities = [(el.name, el.raw, el.confidence) for el in response.entities]
        rep = self.client.text_converse(request, conversation_token=self.my_conv_token).reply()
        return self.intentAnalyse, entities, rep

class Chat:

    def __init__(self, numLignChat=10, numCaractByLign=50):
        '''
        Creates a window
        '''
        self.win = tk.Tk()

        self.numLignChat = numLignChat
        self.numCaractByLign = numCaractByLign

        self.conv = deque(["\n" for i in range(self.numLignChat)], maxlen=self.numLignChat)

        self.create_view()

        self.bot = MyBot()

        self.browser = Browser()
        self.getArival, self.getDeparture = False, False

    def create_view(self):
        '''
        Creates the chat interface and bind events
        '''
        self.l1 = tk.Label(self.win, text="Welcome to chat world")
        self.l1.pack()

        self.ta1 = tk.Text(self.win,height=self.numLignChat, width=self.numCaractByLign)
        self.ta1.pack()

        self.e1a = tk.StringVar()
        self.e1 = tk.Entry(self.win, textvariable=self.e1a)
        self.e1.bind('<Return>', self.exeConv)
        self.e1.bind('<Button-1>', self.clearE1)
        self.e1.pack()
        self.e1a.set("type here...")

    def clearE1(self, event):
        '''
        Uses to clear entry text when focus on
        '''
        self.e1a.set("")

    def preprocess(self, inp):
        '''
        Uses to split entry string in order to fit the text screen size
        '''
        nbLine = len(inp) // self.numCaractByLign
        start, end = 0, 0
        outp = []
        for i in range(nbLine):
            end = inp[:(i+1)*self.numCaractByLign].rfind(" ")
            outp.append(inp[start:end] + "\n")
            start = end
        outp.append(inp[end:])
        return outp

    def printConv(self, newEl):
        '''
        Uses to print the conversation

        Input: -newEl - String - text to print
        '''
        newElp = self.preprocess(newEl)
        [self.conv.append(el) for el in newElp]
        self.ta1.delete(0.0, tk.END)
        for i, el in enumerate(self.conv):
            self.ta1.insert(float(i+1), el)
            if "Bot" in el or (not "me" in el and "Bot" in self.conv[i-1]):
                self.ta1.tag_add("BotTag", str(i+1)+".0", str(i+1)+"."+str(len(el)))
                self.ta1.tag_configure("BotTag", foreground='blue')
        self.win.update()

    def exeConv(self, event):
        '''
        Uses to converse with the bot
        Fire when the user write something and validate with enter key
        '''
        inp = self.e1.get()
        myQ = "me: " + inp + "\n"
        self.e1a.set("")
        self.printConv(myQ)

        if len(inp) > 0:
            self.bot.setQuestion(inp)
            reponse = self.bot.getReponse()
            reponse = "Bot: " + reponse + "\n"
            self.printConv(reponse)

        #if self.bot.response.action.slug == "greetings" and self.bot.response.action.done:
        if self.bot.response.action.slug == "agree" and self.bot.response.action.done:
            #j'attends la fin de la conversation pour rendre possible l'utilisation des
            #boite itinerary et adress afin de tester l'analyseur de text de manière separe
            #et aussi de tester la validation d'etape
            rep = "Bot: " + "Now you can ask for an itinary, where do you want to go?" + "\n"
            self.printConv(rep)
            self.e1.bind('<Return>', self.exeConvPart2)

    def exeConvPart2(self, event):
        '''
        Uses to continue the conversation but here it use the text analyser of the API
        '''
        inp = self.e1.get()
        myQ = "me: " + inp + "\n"
        self.e1a.set("")
        self.printConv(myQ)
        boite, entities, rep = self.bot.getAnalyse(inp)
        reponse = "Bot: " + rep + "\n"
        tmp = False
        if True in [True for el in boite if "itinerary" in el] and self.getArival == False:
            self.arrival = [el[1] for el in entities if "location" in el]
            if len(self.arrival) > 0:
                self.getArival = True
            tmp = True
        if True in [True for el in boite if "adress" in el] and self.getDeparture == False:
            self.departure = [el[1] for el in entities if "location" in el]
            if len(self.departure) > 0:
                self.getDeparture = True
            tmp = True
        if tmp:
            self.printConv(reponse)
        if self.getArival and self.getDeparture:
            self.browser.getItineraire(self.departure, self.arrival)


win = Chat()
win.win.mainloop()
