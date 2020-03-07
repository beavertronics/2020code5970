# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import ctre

#*********Robot-Side Initialization***************
class Right_Motors():
	
	def __init__(self):
		#Initialize Right motors
		right_one = (ctre.WPI_VictorSPX(1))
		right_two = (ctre.WPI_VictorSPX(2))
		self.right_motor_group = wpilib.SpeedControllerGroup(
			right_one, right_two)


