#This file controls Nao Robot and Finch robot to give a programming class

from finchController import FinchController

print "Starting..."

#-------------------- Create connection with the Finch robot
fControl = FinchController()
fControl.__init__()

print "Connection with Finch robot complete"

fControl.makeLoop(3)
fControl.close()

print "Done"