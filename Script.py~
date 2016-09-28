#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

from naoProxy import NaoProxy
from ImageHandler import ImageHandler
from naoqi import ALBroker 


class Program():
    
    def __init__(self):
        self.imgHandler = ImageHandler()
    
    def scriptIf(self):
        
        self.nao.postureProxy.post.goToPosture("Stand", 1.0)
        self.nao.say("Buenos días! Mi nombre es Nao")   
        self.nao.say("El día de hoy, seré su profesor de programación. Espero se diviertan y aprendan mucho.")
        self.nao.textAnimatedToSpeech.say("^start() La programación, es un tema es muy interesante para mí, pues gracias a la programación, yo existo, puedo hablar, me puedo mover y puedo pensar. Aparte de éstas tareas sencillas, también puedo hacer cosas más complicadas, como hacer yoga y bailar. Y todo esto gracias a la magia de la programación. Les enseñaré. Espero no caerme, ja já ja. ")
        self.nao.runBehavior("tai")
        self.nao.textAnimatedToSpeech.say("¿Que les pareció?, Interesante? Cosas como éstas y muchas más se pueden lograr a través de la programación. Hoy les enseñaré a programar, en el lenguaje llamado páiton. Los temas que les enseñaré, hoy son: Variables, condicionales, ciclos y listas.")
        self.nao.textAnimatedToSpeech.say("Les explicaré, poco a poco y de forma entretenida. ¿Qué les parece si empezamos con un juego? Para esto, necesitarée un voluntario")
        self.nao.turn()
        self.nao.runBehavior("turn")
        self.nao.textAnimatedToSpeech.say("Les explicaré, poco a poco y de forma entretenida. ¿Qué les parece si empezamos con un juego? Para esto, necesitarée un voluntario")
        self.nao.unturn()
        
    def run(self, IP):
        broker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)
        
        try:
            global NaoModule1
            NaoModule1 = NaoProxy(IP)
            self.nao = NaoModule1
            self.nao.preloadBehavior("rightHand")
            self.nao.preloadBehavior("leftHand")
            
            self.scriptIf()
        except:
            pass
        
        broker.shutdown()

NaoModule1 = None
program = Program()
program.run("10.15.94.137")
