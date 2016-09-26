from finchRobot.finch import Finch
from time import sleep

#Main function for the race track driver example program."""

class FinchController():
    
    def __init__(self):
        #Initialize the finch
        self.finch = Finch()
        
        
    def close(self):
        #Close the connection with Finch
        self.finch.close()
        print "Connection with Finch Robot terminated"    
    
    def run(self):
        #Set both wheels to one-half forward throttle for 1.5s
        self.finch.wheels(0.5,0.5)
        self.finch.led(0, 255, 255)
        sleep(1.5)
        
        # Now set the left wheel at half throttle, right wheel off to turn
        self.finch.wheels(0.5,0)
        self.finch.led(0, 255, 0)
        sleep(1.28)
        
        
        self.finch.wheels(0.5,0.5)
        self.finch.led(0, 255, 255)
        sleep(1.5)
        
        
        self.finch.wheels(0.5,0)
        self.finch.led(0, 255, 0)
        sleep(1.28)
        
        
        self.finch.wheels(0.5,0.5)
        self.finch.led(0, 255, 255)
        sleep(1.5)
        
        
        self.finch.wheels(0.5,0)
        self.finch.led(0, 255, 0)
        sleep(1.28)
        
        
        self.finch.wheels(0.5,0.5)
        self.finch.led(0, 255, 255)
        sleep(1.5)
        
        
        self.finch.wheels(0.5,0)
        self.finch.led(0, 255, 0)
        sleep(1.28)
