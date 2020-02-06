# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import math

class Carrier_Encoder(wpilib.Encoder):
    def __init__(self, DIO_1, DIO_2):
        super().__init__(DIO_1, DIO_2)

        # Constants
        pulses_per_rev = 12
        # gear_reduction = 1:1

        self.setDistancePerPulse(pulses_per_rev)

    def get_encoder_rpm(self):
        angular_velocity_rpm = self.getRate()
        return angular_velocity_rpm
