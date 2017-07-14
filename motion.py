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

def move_sync(speed, duration):
	try:
		motors.motor2.setSpeed(speed);
		time.sleep(duration);
	except:
		pass
	finally:
		motors.motor2.setSpeed(0);

def move(speed, duration, async=True):
	now = time.time()
	p = Process(target=move_sync, args=[speed, duration])
	p.start()
	if not async:
		p.join()
	return speed, duration, now