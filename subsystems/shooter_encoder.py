# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Outline:
	# need to measure encoder count
	# convert to rpm

import wpilib
import math

#XXX may be better to inherit subsystem, although no commands directly use 
# encoder. But inheriting wpilib.Encoder is only necessary if we need to 
# overwrite a function used in the original encoder class, which it looks
# like we do not.
class Shooter_Encoder(wpilib.Encoder):
	def __init__(self, DIO_1, DIO_2):
		wpilib.Encoder.__init__(self, DIO_1, DIO_2)
		# Constants
		pulses_per_rev = 12
		# gear_reduction = #XXX

		#XXX Set this value based on the encoder’s rated Pulses per Revolution 
		# and factor in gearing reductions following the encoder shaft
		self.setDistancePerPulse(pulses_per_rev)

	#XXX getRate returned in (units used in setDistancePerPulse) / second 
	def get_encoder_rpm(self):
		angular_velocity_rpm = self.getRate()
		return angular_velocity_rpm
