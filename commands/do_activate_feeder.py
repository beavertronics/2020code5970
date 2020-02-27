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
		self.rpm_lower = 0
		self.rpm_upper = 1000

	def condition(self):
		rpm = self.shooter.shooter_encoder.get_encoder_rpm()
		if(rpm in self.shooter.setpoint_range):
			shoot = True
		else:
			shoot = False
		return shoot

	def execute(self):
		self.feeder.activate_feeder() 

	def isFinished(self):
		pass

	def end(self):
		pass

	def interrupted(self):
		self.end()


