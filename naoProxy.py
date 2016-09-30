from naoqi import ALProxy, ALModule, ALBroker
from threading import Semaphore
from time import sleep
import math
import almath as m # python's wrapping of almath

class NaoProxy(ALModule):
	""" Class representing a Nao robot, in charge of executing several actions.

	This class inherits from naoqi.ALModule, in order to be able to execute and
	detect several events triggered by the robot.
	"""
	
	def __init__(self, IP):
		""" Initiates a new instance of the NaoProxy class.

		Args:
			IP: The IP of the robot that will be connected.
		"""

		#Initiate parent class
		ALModule.__init__(self, "NaoModule1")
		
		#Get all necesary proxys
		self.memory = ALProxy("ALMemory")
		self.behaviorManager = ALProxy("ALBehaviorManager")
		self.speechRecognition = ALProxy("ALSpeechRecognition")
		self.textToSpeech = ALProxy("ALTextToSpeech")
		self.textAnimatedToSpeech = ALProxy("ALAnimatedSpeech")		
		self.postureProxy = ALProxy("ALRobotPosture")
		self.motionProxy = ALProxy("ALMotion")
		
		#Setup to be able to detect touched sensors
		self.touchedSensors = []
		self.touchSemaphore = Semaphore(0)
		
		#Setup to be able to detect recognized words.
		self.recognizedWord = None
		self.wordSemaphore = Semaphore(0)
		
	def awaitTouchedSensors(self):
		""" Waits for a sensor to be touched and returns the ones that were touched.

		This methosd uses an auxiliary method, called onTouched, to asynchronously
		insert the detected sensors into self.touchedSensors. onTouched will release
		the semaphore when the list is ready.

		Returns:
			A list containing all the sensors that are being touched when the event is
			triggered.
		"""

		#Subscribe to the event and wait for onTouched to finish its work.
		self.memory.subscribeToEvent("TouchChanged","NaoModule1","onTouched")
		self.touchSemaphore.acquire()
		
		return self.touchedSensors
	
	def onTouched(self, strVarName, value, subscriberName):
		"""	Called when sensor is touched, and stores such sensors.

		This method is auxiliary to self.awaitTouchedSensors, and will release the
		corresponding semaphore once self.touchedSensors has the complete list of
		sensors that have been activated.

		This method eventually unsubscribes the robot from the TouchChanged event,
		since it only needs to be activated once.

		This method has the arguments required by the "ThouchChanged" event.
		"""

		#Unsubscribe to prevent repetitions and conflicts.
		self.memory.unsubscribeToEvent("TouchChanged","NaoModule1")
		
		#Reset the list and fill it with touched sensors
		self.touchedSensors = []
		for p in value:
			if (p[1]):
				self.touchedSensors.append(p[0])
				
		if len(self.touchedSensors) != 0:
			#The list has been filled
			self.touchSemaphore.release()
		else:
			#The event was triggered signaling that sensors were released, instead of
			#pressed, so it subscribes the event again in order to actually be able
			#to detect pressed sensors.
			self.memory.subscribeToEvent("TouchChanged","NaoModule1","onTouched")
			
	def recognizeWord(self, vocabulary):
		""" Waits for a word to be recognized and returns it.

		This method uses an auxiliary method, called onWordRecognized, to 
		asynchronously insert the detected word into self.recognizedWord. 
		onWordRecognized will release the semaphore when the word is ready.

		Args:
			vocabulary: A list of words that are candidates to be recognized.

		Returns:
			A string with the recognized word.
		"""

		#Set the robot's vocabulary
		self.speechRecognition.pause(True)
		self.speechRecognition.setVocabulary(vocabulary, False)
		self.speechRecognition.pause(False)
		
		#Subscribe the the event and wait for onWordRecognized to finish its work.
		self.memory.subscribeToEvent("WordRecognized","NaoModule1","onWordRecognized")
		self.wordSemaphore.acquire()
		
		return self.recognizedWord
	
	def onWordRecognized(self, name, value, subscriber):
		"""	Called when a word is recognized, and stores such word.

		This method is auxiliary to self.recognizeWord, and will release the
		corresponding semaphore once self.recognizedWord has the word sotred.

		This method unsubscribes the robot from the WordRecognized event, since it
		only needs one word, and not a sequence.

		This method has the arguments required by the "WordRecognized" event.
		"""

		self.memory.unsubscribeToEvent("WordRecognized","NaoModule1")
		self.recognizedWord = value
		self.wordSemaphore.release()
		
	def say(self, string):
		""" Makes the robot say something.

		Args:
			string: phrease to be spoken.
		"""
		self.textToSpeech.say(string)
		
	def turn(self):
		self.motionProxy.wakeUp()
		self.postureProxy.goToPosture("StandInit", 0.5)
		self.motionProxy.setMoveArmsEnabled(True, True)
		self.motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
		X = 0.0
		Y = 0.0
		Theta = (math.pi/3.0)*(-1.0)
		self.motionProxy.post.moveTo(X, Y, Theta)
		self.motionProxy.waitUntilMoveIsFinished()
		
	def unturn(self):
		self.motionProxy.wakeUp()
		self.postureProxy.goToPosture("StandInit", 0.5)
		self.motionProxy.setMoveArmsEnabled(True, True)
		self.motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
		X = 0.0
		Y = 0.0
		Theta = (math.pi/3.0)
		self.motionProxy.post.moveTo(X, Y, Theta)
		self.motionProxy.waitUntilMoveIsFinished()

	def preloadBehavior(self, behaviorName):
		""" Proloads a behavior into the robot.

		Args:
			behaviorName: Name fot he behavior to be preloaded.
		"""
		self.behaviorManager.preloadBehavior(behaviorName)
		
	def runBehavior(self, behaviorName):
		""" Runs a behavior

		Args:
			behaviorName: Name fot he behavior to be run.
		"""
		self.behaviorManager.runBehavior(behaviorName)
