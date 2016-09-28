#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

from naoProxy import NaoProxy
from ImageHandler import ImageHandler
from naoqi import ALBroker
from finchController import FinchController
from time import sleep
from Crypto.Random.random import randint


class Program():
    
    def __init__(self):
        self.imgHandler = ImageHandler()
            
    def strings_to_num(self, argument):
        switcher = {
            "uno": 1,
            "dos": 2,
            "tres": 3,
            "cuatro": 4,
            "cinco": 5,
        }
        return switcher.get(argument, 1)
        
    def finchGame(self, loopWord):
        fControl = FinchController()
        fControl.__init__()
        
        x = self.strings_to_num(loopWord)
        
        fControl.makeLoop(x)
        fControl.close()
            
    
    def scriptIf(self):
        self.imgHandler.showImage("Slide1.JPG")
        self.nao.postureProxy.post.goToPosture("Stand", 1.0)
        self.nao.say("Buenos días! Mi nombre es Nao")   
        self.imgHandler.showImage("Slide2.JPG")
        self.nao.say("El día de hoy, seré su profesor de programación. Espero se diviertan y aprendan mucho.")
        self.imgHandler.showImage("Slide3.JPG")
        self.nao.textAnimatedToSpeech.say("^start() La programación, es un tema es muy interesante para mí, pues gracias a la programación, yo existo, puedo hablar, me puedo mover y puedo pensar. Aparte de éstas tareas sencillas, también puedo hacer cosas más complicadas, como hacer yoga y bailar. Y todo esto gracias a la magia de la programación. Les enseñaré. Espero no caerme, ja já ja. ")
        self.nao.runBehavior("tai")
        self.imgHandler.showImage("Slide4.JPG")
        self.nao.textAnimatedToSpeech.say("¿Que les pareció?, Interesante? Cosas como éstas y muchas más se pueden lograr a través de la programación. Hoy les enseñaré a programar, en el lenguaje llamado páiton. Los temas que les enseñaré, hoy son: Variables, condicionales, ciclos y listas.")
        self.imgHandler.showImage("Slide5.JPG")
        self.nao.textAnimatedToSpeech.say("Les explicaré, poco a poco y de forma entretenida. ¿Qué les parece si empezamos con un juego? Para esto, necesitarée un voluntario.")
        self.nao.turn()
        self.nao.behaviorManager.post.runBehavior("turn")
        self.imgHandler.showImage("Slide6.JPG")
        self.nao.say("Aquí tenemos la lista de todos los alumnos. Eligiré una persona al azar.")
        self.nao.say("Pamela! Mi elección es Pamela. ¿Te gustaría jugar conmigo? Pasa al frente por favor Pamela.")
        self.nao.unturn()
        self.nao.behaviorManager.post.runBehavior("relax")
        self.imgHandler.showImage("Slide7.JPG")
        self.nao.textAnimatedToSpeech.say("Pamela, haremos lo siguiente: en mi cabeza tengo 3 botones, uno en atrás, uno en medio y uno adelante. Cuando levante mi brazo izquierdo, deberás presionar el botón delantero. Cuando levante mi brazo derecho, deberás presionar mi botón trasero. Correcto?.")
        self.nao.textAnimatedToSpeech.say("Comencemos.") 
        self.gameIf()
        self.nao.textAnimatedToSpeech.say("Pamela, muchas gracias por jugar conmigo. Lo has hecho muy bien! Por favor pasa a sentarte.")
        self.nao.postureProxy.post.goToPosture("Stand", 1.0)
        self.nao.say("Pamela, muchas gracias por jugar conmigo. Lo has hecho muy bien! Por favor pasa a sentarte para explicarles un poco.")
       
        word = self.nao.recognizeWord(["uno", "dos", "tres", "cuatro", "cinco"])
        self.finchGame(word) # Call the finch game
        sleep(8)
        
    def run(self, IP):
        broker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)
        
        try:
            global NaoModule1
            NaoModule1 = NaoProxy(IP)
            self.nao = NaoModule1
            self.nao.preloadBehavior("rightHand")
            self.nao.preloadBehavior("leftHand")

            
            self.scriptIf()
            self.imgHandler.exit()
        except:
            pass
        
        broker.shutdown()

    def gameIf(self):
        for x in range(0,5):
            choice = randint(1,2)
            
            intento=0
            if choice == 1:
                self.nao.runBehavior("rightHand")
                
                sensors = []
                while "Head/Touch/Front" not in sensors and "Head/Touch/Rear" not in sensors and intento < 5:
                    sensors = self.nao.awaitTouchedSensors()
                    print(sensors)
                    intento = intento+1
                    
                if "Head/Touch/Rear" in sensors:
                    self.nao.say("Correcto")
                else:
                    self.nao.say("Incorrecto")
            if choice == 2:
                self.nao.runBehavior("leftHand")
                
                sensors = []
                while "Head/Touch/Front" not in sensors and "Head/Touch/Rear" not in sensors and intento < 5:
                    sensors = self.nao.awaitTouchedSensors()
                    print(sensors)
                    intento = intento+1
                    
                if "Head/Touch/Front" in sensors:
                    self.nao.say("Correcto")
                else:
                    self.nao.say("Incorrecto")

NaoModule1 = None
program = Program()
program.run("10.15.94.137")
