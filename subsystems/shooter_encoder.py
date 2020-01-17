# vim: set sw=4 noet ts=4 fileencoding-utf-8:

# Outline:
    # need to measure encoder count
    # convert to rpm

import wpilib
import math

class Shooter_Encoder(wpilib.Encoder):
    
    # Constants
    pulses_per_rev = 12

    def __init__(self, DIO_1, DIO_2):
		super().__init__(DIO_1, DIO_2)
        self.setDistancePerPulse(pulses_per_rev)

    def get_encoder_rpm(self):
        angular_velocity_rpm = self.getRate()
        return angular_velocity_rpm
