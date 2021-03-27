# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib import PWMSpeedController
#from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Left_Motors():
 
	def __init__(self):
		#Initialize Left motors
		# Two motors cause TuffBox 
		# Also 0 is generally reserved for PDP or something
		left_one = (wpilib.PWMVictorSPX(3))
		left_two = (wpilib.VictorSP(6))
		self.left_motor_group = wpilib.SpeedControllerGroup(
			left_one, left_two)

