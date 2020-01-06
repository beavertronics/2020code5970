# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib

#*********Robot-Side Initialization***************
class Right_Motors():
	
	def __init__(self):
		#Initialize Right motors
		right_front = (wpilib.VictorSP(0))
		right_mid = (wpilib.VictorSP(1))
		right_rear = (wpilib.VictorSP(2))
		self.right_motor_group = wpilib.SpeedControllerGroup(
			right_front, right_mid, right_rear)


