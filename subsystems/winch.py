# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Winch(Subsystem):
	def __init__(self, robot):
		'''
		Command Dependencies:

		All values currently arbitary!
		'''
		#super().__init__()
		#self.shooter_motor = wpilib.VictorSP(7)
		self.winch_motor = wpilib.VictorSP(6)
		
	def roll_up(self):
		''' Rolls up winch and therefore climbs/lifts robot up '''
		self.winch_motor.set(1)

	def stop_motor(self):
		self.winch_motor.set(0)

	def unroll(self):
		self.winch_motor.set(-1)

