from naoqi import ALProxy
import time

class NaoProxy():
	
	def __init__(self, IP):
		#self.memory = ALProxy("ALMemory", IP, 9559)

		
		#self.speechRecognition = ALProxy("ALSpeechRecognition", IP, 9559)
		#self.speechRecognition.setLanguage("Spanish")
		#self.speechRecognition.pause(True)
		
		#self.memory.subscribeToEvent("WordRecognized", "naoProxy", "wordRecognized")
		
		self.behaviorManager = ALProxy("ALBehaviorManager", IP, 9559)
		#for behaviorName in self.behaviorManager.getInstalledBehaviors():
		#	self.behaviorManager.preloadBehavior(behaviorName)

		self.textToSpeech = ALProxy("ALTextToSpeech", IP, 9559)

	def say(self, string):
		self.textToSpeech.say(string)
		
	def setVocabulary(self, vocabulary):
		self.speechRecognition.setVocabulary(vocabulary, False)
		
	def preloadBehavior(self, behaviorName):
		self.behaviorManager.preloadBehavior(behaviorName)
		
	def runBehavior(self, behaviorName):
		self.behaviorManager.runBehavior(behaviorName)