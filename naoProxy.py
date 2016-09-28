from naoqi import ALProxy, ALModule, ALBroker
from threading import Semaphore
from time import sleep

memory = None
class NaoProxy(ALModule):
	
	def __init__(self, IP):
		ALModule.__init__(self, "NaoProxy")
		
		global memory
		memory = ALProxy("ALMemory")
		
		self.behaviorManager = ALProxy("ALBehaviorManager")
		self.speechRecognition = ALProxy("ALSpeechRecognition")
		self.textToSpeech = ALProxy("ALTextToSpeech")
		
		self.touchedSensors = []
		self.touchSemaphore = Semaphore(0)
		
		self.recognizedWord = None
		self.wordSemaphore = Semaphore(0)
		
	def awaitTouchedSensors(self):
		memory.subscribeToEvent("TouchChanged","NaoProxy","onTouched")
		self.touchSemaphore.acquire()
		
		return self.touchedSensors
	
	def onTouched(self, strVarName, value, subscriberName):
		"""	
			Called when sensor is touched
		"""
		memory.unsubscribeToEvent("TouchChanged","NaoProxy")
		
		self.touchedSensors = []
		
		for p in value:
			if (p[1]):
				self.touchedSensors.append(p[0])
				
		if len(self.touchedSensors) != 0:
			self.touchSemaphore.release()
		else:
			memory.subscribeToEvent("TouchChanged","NaoProxy","onTouched")
			
	def recognizeWord(self, vocabulary):
		self.speechRecognition.pause(True)
		self.speechRecognition.setVocabulary(vocabulary, False)
		self.speechRecognition.pause(False)
		
		memory.subscribeToEvent("WordRecognized","NaoProxy","onWordRecognized")
		self.wordSemaphore.acquire()
 		
		return self.recognizedWord
 	
	def onWordRecognized(self, name, value, subscriber):
		"""	
			Called when word is recognized
		"""
		
		self.recognizedWord = value[0]
		self.wordSemaphore.release()
		
	def say(self, string):
		self.textToSpeech.say(string)
		
	def setVocabulary(self, vocabulary):
		self.speechRecognition.setVocabulary(vocabulary, False)
		
	def preloadBehavior(self, behaviorName):
		self.behaviorManager.preloadBehavior(behaviorName)
		
	def runBehavior(self, behaviorName):
		self.behaviorManager.runBehavior(behaviorName)
		
# IP = "10.15.94.137"
# broker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559) 
# try:
# 	NaoProxy = NaoProxy(IP)
# 	for i in range(0,5):
# 		print(NaoProxy.recognizeWord(["si","no"]))
# 		sleep(1)
# except:
# 	pass
# broker.shutdown()
