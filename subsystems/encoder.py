# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import math

class My_Arm_Encoder(wpilib.Encoder):
	""" Source for PID Loop """

	# Class constants; change if encoder or drive ratios change
	CLICKS_PER_360         = 12
	DEGREE_PER_CLICK       = 360.0 / CLICKS_PER_360
	DRIVE_RATIO            = 1.0/403.2
	# 30 in. arm
	# 139.34 degrees total rotation
	# 12 counts per revolution = 3 pulses per revolution
	# encoder count for arm 0-453
	FINAL_DEGREE_PER_CLICK = DEGREE_PER_CLICK * DRIVE_RATIO

	def __init__(self, DIO_1, DIO_2):
		super().__init__(DIO_1, DIO_2)
		# Amount some gear in motor configuration turns per encoder click
		self.setDistancePerPulse(self.FINAL_DEGREE_PER_CLICK)
	
	def get_new_rate(self):
		#distance_per_seconds = self.getRate()
		distance_per_seconds = super().getRate()
		clicks_per_sec = (
			distance_per_seconds / self.getDistancePerPulse()
			)
		# XXX for debugging
		#print("Overwritten getRate of arm encoder: " + str(clicks_per_sec))
		return clicks_per_sec

	def get_angle(self):
		distance = super().getDistance()
		angular_distance = distance * math.pi
