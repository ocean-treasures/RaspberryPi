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
	movement = False  
	speed = 250

	if distance > 0:
		movement = True # Motor will move
		#speed = 250 # 19.2 MHz / 2 / 480 = 20 kHz
		# Max speed for a motor with this driver
		
	elif distance < 0:
		movement = True 
		speed = -speed
		 # Max speed for a motor with this driver for the other direction
		distance = -distance # Making distance positive for further calculations
		
	else:
		movement = False # Motor won't move

	if movement == True: 
		duration = float(distance) 
		print("\n Moving {} seconds. \n".format(duration)) 
		# Prints on screen how much time the motor will rotate
		motors.motor2.setSpeed(speed); # Starting motor
		time.sleep(duration*0.3); # Time for motor to rotate, seconds
		motors.motor2.setSpeed(0); 
		# Turning off the motor *both motors in the driver*
	
	else:	
		pass 


def move(dist, sync=False):
    
    if sync==True :
        dist = float(dist) 
        Process(target=move_,args=[dist]).start() 
        # Starts new process to turn the motor
    
    else :
        move_(dist)


if __name__ == '__main__':
	
	dist_ = float(raw_input("Distance in cm: ")) 
	move(dist_)
