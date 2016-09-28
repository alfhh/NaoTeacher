#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

from naoProxy import NaoProxy
from ImageHandler import ImageHandler
from naoqi import ALBroker 

class Program():
    
    def __init__(self):
        self.imgHandler = ImageHandler()
    
    def scriptIf(self):
        
        self.nao.say("Si dicen 'negro', levanto mi mano derecha. Si no, levanto mi mano izquierda.")
        
        word = self.nao.recognizeWord(["blanco", "negro"])
        
        if (word == "negro"):
            self.nao.runBehavior("rightHand")
        else:
            self.nao.runBehavior("leftHand")
        
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
