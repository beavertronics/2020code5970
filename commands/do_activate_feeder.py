# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import ConditionalCommand
from do_feeder import Do_Feeder
from shooter import Shooter
from feeder import Feeder

class Do_Activate_Feeder(ConditionalCommand):

	def __init__(self, robot):
		print("activate_feeder init!!")
		self.do_feeder = Do_Feeder(robot)
		ConditionalCommand.__init__(self, 'Do_Activate_Feeder', self.do_feeder)
		self.requires(robot.shooter)
		self.shooter = robot.shooter

	def initialize(self):
		pass

	def execute(self):
		pass

	def condition(self):
		#XXX rpm might never exactly equal goal
		goal = self.shooter.setpoint
		rpm = self.shooter.shooter_encoder.get_encoder_rpm()
		if(rpm == goal):
			return True
		else:
			return False

	def isFinished(self):
		return False

	def end(self):
		pass

	def interrupted(self):
		self.end()


