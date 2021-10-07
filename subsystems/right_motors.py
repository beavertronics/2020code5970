# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib import PWMSpeedController

#*********Robot-Side Initialization***************
class Right_Motors():
	
	def __init__(self):
		#Initialize Right motors
		right_one = (wpilib.PWMVictorSPX(3))
		right_two = (wpilib.PWMVictorSPX(4))
		self.right_motor_group = wpilib.SpeedControllerGroup(
			right_one, right_two)


