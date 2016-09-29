#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

from naoProxy import NaoProxy
import time
from random import choice
from Crypto.Random.random import randint
from ImageHandler import ImageHandler
    
class Program():
    
    def __init__(self, NaoIP):
        self.nao = NaoProxy(NaoIP)
        self.imgHandler = ImageHandler()
        
#         self.nao.preloadBehavior("rightHand")
#         self.nao.preloadBehavior("leftHand")
#         self.nao.preloadBehavior("recogWord")
    
    def scriptIf(self):
        
        self.nao.say("Si dicen 'negro', levanto mi mano derecha. Si no, levanto mi mano izquierda.")
        
#         self.nao.setVocabulary(["blanco", "negro"])
#         word = self.nao.runBehavior("recogWord")
        
        word = "negro";
        
#         if (word == "negro"):
#             self.nao.runBehavior("rightHand")
#         else:
#             self.nao.runBehavior("leftHand")
        
        self.nao.say("Eso fue una condición. Dije que si algo pasaba, haría una cosa, pero si esa condición no se compila, haría otra cosa. Las estructuras condicionales son la manera en que las computadoras toman decisiones.")
        time.sleep(1)
        
        self.nao.say("Ahora, pongamos lo que acabo de decir en lo que parece código.")
        self.imgHandler.showImage("pseudcodigoIf.png")
        time.sleep(2)
        
        self.nao.say("Ahora juguemos un poco con esta estructura condicional.")
        self.imgHandler.showImage("codigojuegoIf.png")
        self.nao.say("Voy a sacar cartas al azar. Pueden ser blancas o negras. Si es negra, ganan un punto. Si no, entonces pierden un punto.")
        time.sleep(0.5)
        self.nao.say("Empecemos.")
        time.sleep(1)
        
        score = 0
        for x in range(0,4):
            if randint(0,1) == 1:
                chosen = "negra"
            else:
                chosen = "blanca"
                
            self.nao.say("Saqué una carta " + chosen)
            
            if chosen == "negra":
                score += 1
            else:
                score -= 1
            
            self.nao.say("El marcador es: " + score)
            
        self.nao.say("Ha terminado el juego. Su marcador final es:" + score)
        
        self.nao.say("Ahora que saben lo que son las estructuras condicionales, pasemos a lo siguiente.")
        
    def run(self):
        self.scriptIf()

program = Program("10.15.94.137")
print("listo")
program.run()  


#nao = NaoProxy("10.15.94.137")
#nao.setVocabulary(["blnco", "negro"])
#for i in range(1,5):
#    word = nao.recognizeWord()
#    print(word)
#nao.closeConnections()
