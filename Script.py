#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

from naoProxy import NaoProxy
from ImageHandler import ImageHandler
from naoqi import ALBroker
from finchController import FinchController
from time import sleep
from Crypto.Random.random import randint, choice
import new


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
#         self.imgHandler.showImage("Slide2.JPG")
#         self.nao.postureProxy.post.goToPosture("Stand", 1.0)
#         self.nao.say("buenos días! mi nombre es nao")   
#         self.nao.postureProxy.post.goToPosture("Stand", 1.0)
#         self.imgHandler.showImage("Slide2.JPG")
#         self.nao.say("el día de hoy, seré su profesor de programación. espero se diviertan y aprendan mucho.")
#         self.imgHandler.showImage("Slide3.JPG")
#         self.nao.textAnimatedToSpeech.say("^start() la programación, es un tema muy interesante para mí, pues gracias a la programación, yo existo, puedo hablar, me puedo mover y puedo pensar. aparte de éstas tareas sencillas, también puedo hacer cosas más complicadas, como hacer yoga y bailar. y todo esto gracias a la magia de la programación. les enseñaré. espero no caerme, ja já ja. ")
        #self.nao.runBehavior("tai")
#         self.imgHandler.showImage("Slide4.JPG")
#         self.nao.textAnimatedToSpeech.say("¿que les pareció?, interesante? cosas como éstas y muchas más se pueden lograr a través de la programación. hoy les enseñaré a programar, en el lenguaje llamado páiton. los temas que les enseñaré, hoy son: variables, condicionales, ciclos y listas.")
#         self.nao.textAnimatedToSpeech.say("les explicaré, poco a poco y de forma entretenida. ¿qué les parece si empezamos con un juego?")
#         self.imgHandler.showImage("Slide5.JPG")
#         self.nao.textAnimatedToSpeech.say(" para esto, necesitarée un voluntario.")
#         self.nao.turn()
#         self.nao.behaviorManager.post.runBehavior("turn")
#         self.imgHandler.showImage("Slide6.JPG")
        #self.nao.say("aquí tenemos la lista de todos los alumnos. eligiré una persona al azar.")
        seletedstudent = self.getRamdomStuden()
        #sleep(2)
        #self.nao.say("mi elección es" + seletedstudent + "." + seletedstudent + "¿te gustaría jugar conmigo? pasa al frente por favor "+ seletedstudent + ".")
        #self.nao.unturn()
#         self.imgHandler.showImage("Slide7.JPG")
#         self.nao.textToSpeech.post.say(seletedstudent +  ", haremos lo siguiente: en mi cabeza tengo 3 botones, uno en atrás, uno en medio y uno adelante. cuando levante mi brazo izquierdo, deberás presionar el botón delantero. cuando levante mi brazo derecho, deberás presionar mi botón trasero. correcto?.")
#         self.nao.postureProxy.post.goToPosture("Sit", 1.0)
#         self.imgHandler.showImage("Slide18.JPG")
#         self.nao.textAnimatedToSpeech.say("comencemos.") 
#         self.gameIf()
        #self.nao.postureProxy.post.goToPosture("Stand", 1.0)
#         self.nao.say(seletedstudent + ", muchas gracias por jugar conmigo. lo has hecho muy bien! por favor pasa a sentarte para explicarles un poco.")
        #self.imgHandler.showImage("Slide8.JPG")
#         self.nao.turn()
#         self.nao.behaviorManager.post.runBehavior("turn")
#         self.nao.say("El juego que acabamos de jugar, es una representación de el tema de condicionales.")
#         self.imgHandler.showImage("Slide9.JPG")
#         self.nao.say("Podemos ver como se tiene la diferente ruta de acciones dependiendo de qué fué lo que sucedió durante el juego.")
#         self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Aqui tenemos otro ejemplo del tema de condicionales. Las condicionales nos sirven para tomar decisiones dependiendo de si cierta condición se cumple, ó nó.")
        self.imgHandler.showImage("Slide10.JPG")
        self.nao.textToSpeech.post.say("Una condicional está compuesta de una pregunta y de dos acciones, la acción seleccionada depende de la respuesta a la pregunta inicial. ") 
        self.nao.unturn()
        self.nao.textAnimatedToSpeech.say("Veamos un ejemplo. Si tenemos once pesos y nos hacemos la pregunta: ¿Tienes diez o más pesos?")
        self.imgHandler.showImage("Slide11.JPG")
        self.nao.textAnimatedToSpeech.say("Como once es más que diéz, la respuesta a esta pregunta es afirmativa.")
        self.imgHandler.showImage("Slide12.JPG")
        self.nao.textAnimatedToSpeech.say("entonces ejecutamos la acción de Acción, comprar un dulce.")
        self.imgHandler.showImage("Slide13.JPG")
        self.nao.textAnimatedToSpeech.say("De lo contrario si comenzamos con cinco pesos")
        self.imgHandler.showImage("Slide14.JPG")
        self.textAnimatedToSpeech.say("Ya que cinco es menor a diéz, la respuesta ahora sería ahora negativa y por lo tanto")
        self.imgHandler.showImage("Slide15.JPG")
        self.textAnimatedToSpeech.say("habrá que ejecutar la acción de buscar más dinero.") 
        self.imgHandler.showImage("Slide16.JPG")
        self.textAnimatedToSpeech.say("Ahora les enseñare cómo quedaria el código de esta condicional.") 
        self.imgHandler.showImage("Slide17.JPG")
        self.textAnimatedToSpeech.say("En la presentación pueden ver el pedazo de código que representaría la pequeña ruta de decisiones de lo que explicamos anteriormente. Qué les parece? sencillo?")
        self.imgHandler.showImage("Slide18.JPG")
        self.textAnimatedToSpeech.say("Ahora volvámos al código que usamos cuando jugué con " + seletedstudent + ". Vemos aquí como se hacen también diferentes preguntas para saber que es lo que debe hacerse dependiendo de las condiciones.")
        self.nao.textAnimatedToSpeech.say("Las condicionales son muy útiles, ya que nos ayudan a usar otras herramientas, como los ciclos. Veremos en esta ocasión un ciclo muy sencillo llamado guail.")
        self.imgHandler.showImage("Slide19.JPG")
        self.nao.textAnimatedToSpeech.say("Los ciclos nos sirven para repetir una acción un número determinado de veces.")
        self.imgHandler.showImage("Slide20.JPG")
        self.nao.textAnimatedToSpeech.say("Los ciclos utilizan el concepto de condicionales que vimos anteriormente. ¿Recuerdan bien las partes de un condicional? Un condicional tiene una pregunta y dos acciones, las cuales dependen de la respuesta. Por lo tanto, al usar un guail necesitamos de un condicional, Si este condicional nos regresa una respuesta positiva entonces la acción se repetirá, de lo contrario el ciclo termina. Les daré un ejemplo de un ciclo. Condición: Mientras el robot Nao tenga batería, Acción a repetir: Hablar, Acción de final de ciclo: Apagar Nao.") 
        self.nao.textToSpeech.post.say("Veamos el flujo de este ejemplo.")
        self.imgHandler.showImage("Slide21.JPG")
        self.nao.turn()
        self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Comenzamos el robot con cién porciento de batería.")
        self.imgHandler.showImage("Slide22.JPG")
        self.nao.textAnimatedToSpeech.say("Ya que seguimos teniendo batería al darnos cuenta de que es mayor que cero,")
        self.imgHandler.showImage("Slide23.JPG")
        self.nao.textAnimatedToSpeech.say("el robot sigue hablando.")
        self.imgHandler.showImage("Slide24.JPG")
        self.nao.textAnimatedToSpeech.say("Posteriormente volveremos a hacernos la misma pregunta.")
        self.imgHandler.showImage("Slide25.JPG")
        self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Esta vez el robot se encuentra con ochenta porciento de batería.")
        self.imgHandler.showImage("Slide26.JPG")
        self.nao.textAnimatedToSpeech.say("Ya que seguimos teniendo batería al darnos cuenta de que es mayor que cero,")
        self.imgHandler.showImage("Slide27.JPG")
        self.nao.textAnimatedToSpeech.say("el robot sigue hablando.")
        self.imgHandler.showImage("Slide28.JPG")
        self.nao.textAnimatedToSpeech.say("Posteriormente volveremos a hacernos la misma pregunta.")
        self.imgHandler.showImage("Slide29.JPG")
        self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Esta vez el robot se encuentra con cuarenta porciento de batería.")
        self.imgHandler.showImage("Slide30.JPG")
        self.nao.textAnimatedToSpeech.say("Ya que seguimos teniendo batería al darnos cuenta de que es mayor que cero,")
        self.imgHandler.showImage("Slide31.JPG")
        self.nao.textAnimatedToSpeech.say("el robot sigue hablando.")
        self.imgHandler.showImage("Slide32.JPG")
        self.nao.textAnimatedToSpeech.say("Posteriormente volveremos a hacernos la misma pregunta.")
        self.imgHandler.showImage("Slide33.JPG")
        self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Finalmente el robot se queda sin batería.")
        self.nao.textAnimatedToSpeech.say("Ya que la batería es cero,")
        self.imgHandler.showImage("Slide34.JPG")
        self.nao.textAnimatedToSpeech.say("el robot deja de hablar y se apaga.")
        self.imgHandler.showImage("Slide35.JPG")
        self.nao.behaviorManager.post.runBehavior("turn")
        self.nao.say("Así quedaría el código de éste ciclo.")
        self.nao.unturn()
        self.nao.textAnimatedToSpeech.say("Realicémos otra actividad, esta vez seleccionaré a otro de ustedes.")
        seletedStudent = self.getRamdomStuden2()
        self.imgHandler.showImage("Slide36.JPG")
        sleep(2)
        self.nao.textAnimatedToSpeech.say( "Mi elección es " + seletedStudent + ". Puedes venir al frente porfavor?")
        self.imgHandler.showImage("Slide37.JPG")
#         self.nao.textAnimatedToSpeech.say("Para este ejercicio también necesito la ayuda de mi buen amigo, el robot finsh, el cual dará un número de vueltas dependiendo del número que tu me digas.")
#         word = ["", 0];
#         while(word[1] < 0.5):
#             self.nao.textAnimatedToSpeech.say("Por favor dime un número de 1 al 5.")       
#             word = self.nao.recognizeWord(["uno", "dos", "tres", "cuatro", "cinco"])
#             self.finchGame(word) # Call the finch game
#             print(word)
#             self.nao.textAnimatedToSpeech.say(word[0])
#         self.nao.textAnimatedToSpeech.say("Perfecto, muchas gracias " + seletedStudent + ", puedes volver a tu lugar, muchas gracias por tu ayuda robot Finsh.")
#         self.imgHandler.showImage("Slide16.JPG")
#         self.nao.textAnimatedToSpeech.say("Por último, queda el tema de Listas.")
#         self.imgHandler.showImage("Slide17.JPG")
#         self.nao.textAnimatedToSpeech.say("Las Listas sirven para almacenar una secuencia de variables. Lo importante de las listas es que, son ordenadas, o sea que mantiene una secuencia definida, y que cada variable puede ser accedida con su posición.")
#         choice = randint(2,25)
#         print(studentList[choice])
#         self.nao.textAnimatedToSpeech.say("Por ejemplo, puedo saber que en el número " + str(choice + 1) + " está " + studentList[choice] + ", y que antes de " + studentList[choice] + " está " +     studentList[choice - 1] + ", y que después está " + studentList[choice + 1] + ".")
#         self.imgHandler.showImage("Slide17.JPG")
#         self.nao.textAnimatedToSpeech.say("Realicémos otra actividad. Voy a seleccionar a alguien con su número, esta persona tendrá que pasar al frente y decir un numero de alguien más, no el suyo éh! Con eso, esa persona pasará y dirá otro número")
#         choice = randint(1,28)
#         newchoice = choice;
#         print(studentList[choice])
#         for _ in range(0,2):
#             self.nao.textAnimatedToSpeech.say(studentList[newchoice] + ", por favor pasa al frente")
#             choice = newchoice;
#             self.nao.textAnimatedToSpeech.say(studentList[choice] + ", por favor dime un número entre 1 y 27, que no sea tu número de la lista")
#             word = ["", 0];
#             while(word[1] < 0.5):
#                 word = self.nao.recognizeWord(map(str, range(1,28)))
#                 print(word)
#             newchoice = int(word[0]) - 1
#             while(newchoice == choice):
#                 self.nao.textAnimatedToSpeech.say(studentList[choice] + ", que no sea tu número de la lista")
#                 word = ["", 0];
#                 while(word[1] < 0.5):
#                     word = self.nao.recognizeWord(map(str, range(1,28)))
#                     print(word)
#                 newchoice = int(word[0]) - 1
#         self.nao.textAnimatedToSpeech.say(studentList[newchoice] + ", por favor quédate en tu lugar")
#         self.nao.textAnimatedToSpeech.say("Como pudieron ver, es muy fácil obtener datos de una lista, y por eso es una de las estructuras básicas de la programación.")
#         self.nao.textAnimatedToSpeech.say("¿Se dieron cuenta como la programación nos ayuda realizar cosas increibles?")
#         self.nao.textAnimatedToSpeech.say("Nunca duden del poder de la programación, ya que ustedes con su gran capacidad mental y la programación, pueden crear cualquier cosa.")
#         self.imgHandler.showImage("Slide14.JPG")
#         self.nao.textAnimatedToSpeech.say("Con esto daremos por terminada la clase. Espero que hayan aprendido mucho.")
#         self.nao.postureProxy.post.goToPosture("LyingBelly", 1.0)
#         self.nao.say("Por ahora les agradezco y me retiro a dormir un momento pues me encuentro muy cansado. Hásta pronto.")
#          
        
    def run(self, IP):
        broker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)
        
        try:
            global NaoModule1
            NaoModule1 = NaoProxy(IP)
            self.nao = NaoModule1
            self.scriptIf()
            self.imgHandler.exit()
        except:
            self.imgHandler.exit()
            pass
        
        broker.shutdown()

    def gameIf(self):
        for x in range(0,5):
            choice = randint(1,2)
            intento=0
            if choice == 1:
                self.nao.behaviorManager.post.runBehavior("rightHand")
                
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
                self.nao.behaviorManager.post.runBehavior("leftHand")
                
                sensors = []
                while "Head/Touch/Front" not in sensors and "Head/Touch/Rear" not in sensors and intento < 5:
                    sensors = self.nao.awaitTouchedSensors()
                    print(sensors)
                    intento = intento+1
                    
                if "Head/Touch/Front" in sensors:
                    self.nao.say("Correcto")
                else:
                    self.nao.say("Incorrecto")

studentList = ['Virgilio', 'Adrián', 'Luz Valeria', 'César', 'Marian', 'Kelly', 'Alex', 'Andrés', 'Fanny', 'María De Los Ángeles' , 'Frida', 'Glen', 'Juan Ángel', 'Maricris', 'Yander', 'Diego', 'Valeria', 'Dana', 'Daniela', 'Angel', 'Valentina', 'Marcelo', 'Ericka', 'Daniel', 'Luis', 'Pamela', 'Paco']
NaoModule1 = None
program = Program()
program.run("10.15.94.137")
