from naoqi import ALProxy, ALModule, ALBroker
from threading import Semaphore
from time import sleep

memory = None
class NaoProxy(ALModule):
	
	def __init__(self, IP):
		ALModule.__init__(self, "NaoModule1")
		
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
		memory.subscribeToEvent("TouchChanged","NaoModule1","onTouched")
		self.touchSemaphore.acquire()
		
		return self.touchedSensors
	
	def onTouched(self, strVarName, value, subscriberName):
		"""	
			Called when sensor is touched
		"""
		memory.unsubscribeToEvent("TouchChanged","NaoModule1")
		
		self.touchedSensors = []
		
		for p in value:
			if (p[1]):
				self.touchedSensors.append(p[0])
				
		if len(self.touchedSensors) != 0:
			self.touchSemaphore.release()
		else:
			memory.subscribeToEvent("TouchChanged","NaoModule1","onTouched")
			
	def recognizeWord(self, vocabulary):
		self.speechRecognition.pause(True)
		self.speechRecognition.setVocabulary(vocabulary, False)
		self.speechRecognition.pause(False)
		
		memory.subscribeToEvent("WordRecognized","NaoModule1","onWordRecognized")
		self.wordSemaphore.acquire()
 		
		return self.recognizedWord
 	
	def onWordRecognized(self, name, value, subscriber):
		"""	
			Called when word is recognized
		"""
		memory.unsubscribeToEvent("WordRecognized","NaoModule1")
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
