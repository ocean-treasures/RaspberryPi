from __future__ import print_function
import time
from pololu_drv8835_rpi import motors, MAX_SPEED
"""
Moving 2nd motor of pololu_drv8835_rpi driver package

Move - moves 2nd motor of driver pololu_drv8835_rpi clockwise with positive
and counter clockwise with negative value of distance

"""

def move(distance):
	"""
	Distance - number, cm
	Move the motor up
	Additional weight makes easier or harder motor's movement
	Needs calibration
	
	"""
	if distance > 0:
		speed = 480
	elif distance < 0:
		speed = -480
		distance = -distance
	else:
		print("Not moving!")
	duration = float(distance*0.112)
	print(duration)
	motors.motor2.setSpeed(speed);
	time.sleep(duration);
	motors.motor2.setSpeed(0);
	pass


def check_step(duration, speed):
	# duration = 1 # seconds
	# speed = 480 # MAX_SPEED
	# step = 9 # cm
	motors.motor2.setSpeed(speed);
	time.sleep(duration);
	motors.motor2.setSpeed(0);
