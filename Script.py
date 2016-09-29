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
    
    def getRamdomStuden(self):
        return "Pamela"
    
    def getRamdomStuden2(self):  
        return "Paco"
        
    def finchGame(self, loopWord):
        fControl = FinchController()
        fControl.__init__()
        
        x = self.strings_to_num(loopWord)
        
        fControl.makeLoop(x)
        fControl.close()
            
    
    def scriptIf(self):
#         self.imgHandler.showImage("Slide1.JPG")
#         self.nao.postureProxy.post.goToPosture("Stand", 1.0)
#         self.nao.say("Buenos días! Mi nombre es Nao")   
#         self.imgHandler.showImage("Slide2.JPG")
#         self.nao.say("El día de hoy, seré su profesor de programación. Espero se diviertan y aprendan mucho.")
#         self.imgHandler.showImage("Slide3.JPG")
#         self.nao.textAnimatedToSpeech.say("^start() La programación, es un tema es muy interesante para mí, pues gracias a la programación, yo existo, puedo hablar, me puedo mover y puedo pensar. Aparte de éstas tareas sencillas, también puedo hacer cosas más complicadas, como hacer yoga y bailar. Y todo esto gracias a la magia de la programación. Les enseñaré. Espero no caerme, ja já ja. ")
        #self.nao.runBehavior("tai")
#         self.imgHandler.showImage("Slide4.JPG")
#         self.nao.textAnimatedToSpeech.say("¿Que les pareció?, Interesante? Cosas como éstas y muchas más se pueden lograr a través de la programación. Hoy les enseñaré a programar, en el lenguaje llamado páiton. Los temas que les enseñaré, hoy son: Variables, condicionales, ciclos y listas.")
#         self.imgHandler.showImage("Slide5.JPG")
#         self.nao.textAnimatedToSpeech.say("Les explicaré, poco a poco y de forma entretenida. ¿Qué les parece si empezamos con un juego? Para esto, necesitarée un voluntario.")
#         self.nao.turn()
#         self.nao.behaviorManager.post.runBehavior("turn")
#         self.imgHandler.showImage("Slide6.JPG")
#         self.nao.say("Aquí tenemos la lista de todos los alumnos. Eligiré una persona al azar.")
#         
#         seletedStudent = self.getRamdomStuden()
#         
#         self.nao.say("Mi elección es" + seletedStudent + ". ¿Te gustaría jugar conmigo? Pasa al frente por favor"+ seletedStudent + " .")
#         self.nao.unturn()
#         self.nao.textToSpeech.post.say(seletedStudent +  ", haremos lo siguiente: en mi cabeza tengo 3 botones, uno en atrás, uno en medio y uno adelante. Cuando levante mi brazo izquierdo, deberás presionar el botón delantero. Cuando levante mi brazo derecho, deberás presionar mi botón trasero. Correcto?.")
# 
#         self.nao.postureProxy.post.goToPosture("Sit", 1.0)
# 
#         self.imgHandler.showImage("Slide7.JPG")
# 
#         self.nao.textAnimatedToSpeech.say("Comencemos.") 
        #self.gameIf()
        #self.nao.postureProxy.post.goToPosture("Stand", 1.0)
#         self.nao.say(seletedStudent + ", muchas gracias por jugar conmigo. Lo has hecho muy bien! Por favor pasa a sentarte para explicarles un poco.")
#         self.nao.textAnimatedToSpeech.say("Analicemos como es que se codificaría éste juego.")
        self.imgHandler.showImage("Slide15.jpg")
        #self.nao.turn()
        #self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Lo que tenemos a continuación es el código del juego que acabamos de jugar. Podemos ver como se tiene la diferente ruta de acciones dependiendo de que fué lo que sucedio durante el juego.")
        #self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Aqui tenemos otro ejemplo del tema de condicionales. Las condicionales nos sirven para tomar decisiones dependiendo de si cierta condición se cumple o no.")
        self.imgHandler.showImage("Slide9.JPG")
        self.nao.textToSpeech.post.say("Una condicional está compuesta de una pregunta y de dos acciones, la acción seleccionada depende de la respuesta a la pregunta inicial. Veamos un ejemplo. La pregunta aquí es, ¿Tienes diez o más pesos? Si la respuesta es sí, entonces ejecutamos la acción de Acción, comprar un dulce; si la respuesta es nó, habrá que ejecutar la acción de buscar más dinero. En la presentación pueden ver como se haría esta pregunta, o condicional en programación. El juego de hace rato, en donde tocaban los botones de mi cabeza, depende de los condicionales para funcionar.") 
        #self.nao.unturn()
         
        self.nao.textAnimatedToSpeech.say("Los condicionales son muy útiles, ya que nos ayudan a usar otras herramientas, como los ciclos, o como yo los conozco..")
        self.imgHandler.showImage("Slide10.JPG")
        self.imgHandler.showImage("Slide11.JPG")
        self.nao.textAnimatedToSpeech.say("Los ciclos sirven para repetir una acción un número determinado de veces. Los ciclos utilizan el concepto de condicionales que vimos anteriormente. ¿Recuerdan bien las partes de un condicional? Un condicional tiene una pregunta y dos acciones, las cuales dependen de la respuesta. Por lo tanto, al usar un while necesitamos de un condicional, y si este condicional nos regresa una respuesta positiva entonces la acción se repetirá, de lo contrario el ciclo termina. Les daré un ejemplo de un ciclo. Condición: Mientras el robot Nao tenga batería, Acción a repetir: Hablar, Acción de final de ciclo: Apagar Nao. Realicemos otra actividad, esta vez seleccionaré a otro de ustedes.")
        
        seletedStudent = self.getRamdomStuden2()
        
        self.imgHandler.showImage("Slide12.JPG")
        self.nao.textAnimatedToSpeech.say( seletedStudent + " puedes venir al frente.")
        
        self.imgHandler.showImage("Slide13.JPG")
        self.nao.textAnimatedToSpeech.say("Para este ejercicio también necesito la ayuda de mi buen amigo, el robot finch, el cual dará un número de vueltas dependiendo del número que tu me digas.")
        self.nao.textAnimatedToSpeech.say("Por favor dime un número de 1 al 5.")
         
        #word = self.nao.recognizeWord(["uno", "dos", "tres", "cuatro", "cinco"])
        #self.finchGame(word) # Call the finch game

        
        self.nao.textAnimatedToSpeech.say("Perfecto, muchas gracias " + seletedStudent + " puedes volver a tu lugar, muchas gracias por tu ayuda robot Finch.")

        
        self.nao.textAnimatedToSpeech.say("¿Se dieron cuenta como la programación nos ayuda realizar cosas increibles?")
         
        self.nao.textAnimatedToSpeech.say("Nunca duden del poder de la programación, ya que ustedes con su gran capacidad mental y la programación, pueden crear cualquier cosa.")
         
        self.imgHandler.showImage("Slide14.JPG")
        self.nao.textAnimatedToSpeech.say("Les quiero agradecer por su cooperación y por ponerme atención, con esto daremos por terminada la clase. Espero que hayan aprendido mucho.")
        self.nao.textAnimatedToSpeech.say("¿Se dieron cuenta como la programación nos ayuda realizar cosas increibles?")
        #self.nao.postureProxy.post.goToPosture("LyingBelly", 1.0)
        self.nao.say("Por ahora les agradezco y me retiro a dormir un momento pues me encuentro muy cansado. Hásta pronto.")

         
        
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
studentList = ['Virgilio', 'Adrián', 'Luz Valeria', 'César', 'Marian', 'Kelly', 'Alex', 'Andrés', 'Fanny', 'María De Los Ángeles' , 'Frida', 'Glen', 'Juan Ángel', 'Maricris', 'Yander', 'Diego', 'Valeria', 'Dana', 'Daniela', 'Angel', 'Valentina', 'Marcelo', 'Ericka', 'Daniel', 'Luis', 'Pamela', 'Paco']
