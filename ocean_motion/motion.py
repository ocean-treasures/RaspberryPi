from __future__ import print_function
from pololu_drv8835_rpi import motors, MAX_SPEED
from multiprocessing import Process 
import time
"""
Moving 2nd motor of pololu_drv8835_rpi driver
Positive value means clockwise rotation
Negative value means counterclockwise rotation

Time = 1, second(s)
Axle d = 0.3, cm
Rotates 8 times
Rope diameter = 0.1, cm
Distance = 9, cm

"""

def move_(distance):
	"""
		Moving the motor
		"distance" - number, cm
		Positive or negative for direction of the rotation
		
	"""
	movement = False  # Defining boolean variable 
	speed = 0 # Defining integer variable "speed"

	if distance > 0:
		movement = True # Motor will move
		speed = 480 # 19.2 MHz / 2 / 480 = 20 kHz
		# Max speed for a motor with this driver
		
	elif distance < 0:
		movement = True # Motor will move
		speed = -480 # Max speed for a motor with this driver for the other direction
		distance = -distance # Making distance positive for further calculations
		
	else:
		movement = False # Motor won't move

	if movement == True: # Should motor move?
		duration = float(distance*0.112) # Duration with axle with d=3cm
		print("\n\n Moving {} seconds. \n\n".format(duration)) 
		# Prints on screen how much time the motor will rotate
		motors.motor2.setSpeed(speed); # Starting motor
		time.sleep(duration); # Time for motor to rotate, seconds
		motors.motor2.setSpeed(0); # Turning off the motor *both motors in the driver*
	else:	
		pass #movement = false

def move(dist):
	dist = float(dist) # Changes given value to float type
	Process(target=move_,args=[dist]).start() # Starts the process of turning the motor

if __name__ == '__main__':
	dist_ = float(raw_input("Distance in cm: ")) # Just for testing the code, standard input (keyboard) 
	move(dist_) # Starting the function
