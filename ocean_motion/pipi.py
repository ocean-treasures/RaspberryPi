from __future__ import print_function
import time
#from pololu_drv8835_rpi import motors, MAX_SPEED
"""
Moving 2nd notor of pololu

"""



if __name__ == '__main__':
	#motors.setSpeeds(0, 0)
	def clockwise(distance_, steps_): #distance in m 
		#motors.motor2.setSpeed(MAX_SPEED)
		print("max")
		time.sleep(1.7)
		print(1.7)
		#motors.setSpeeds(0, 0)
		print("END")
	move = str(raw_input("R or L"))
	move = move.lower()
	print(move)
	if move == "r":
		clockwise(2.5, 5)






# print('Name:', __name__)

# def moveUp():
# 	print('moveUP')

# if __name__ == '__main__':
# 	try:
# 		turns = int(raw_input("Number of turns:"))
# 		i=0
# 		while i<turns :
# 			state_ = str(raw_input("T or F"))
# 			#print (state_)

# 			if state_ == "T" :
# 				state = True
# 				print(state)
# 				i+=1
# 				print("State is {} and you have {} turns to go".format(state,turns-i))
# 				motors.motor2.setSpeed(-MAX_SPEED)
# 				time.sleep(0.7)
# 				motors.setSpeeds(0, 0)
# 			elif state_ == "F" and i>0 :
# 				state = False
# 				print(state)
# 				i-=1
# 				print("State is {} and you have {} turns to go".format(state, turns-i))
# 				motors.motor2.setSpeed(MAX_SPEED)
# 				time.sleep(0.7)
# 				motors.setSpeeds(0, 0)
# 			else:
# 				print("Try again")

# 	finally:
# 		# Stop the motors, even if there is an exception
# 		# or the user presses Ctrl+C to kill the process.
# 		motors.setSpeeds(0, 0)
