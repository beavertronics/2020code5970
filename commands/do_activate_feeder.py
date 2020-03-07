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

	def condition(self):
		''' If this returns True then it runs the execute()'''
		#XXX setpoint_range MUST be tested!
		rpm = self.shooter.shooter_encoder.get_encoder_rpm()
		pwm_volts = self.shooter.convert_rpm_to_pwm(rpm)
		if(self.shooter.setpoint_range[0] < pwm_volts and
			self.shooter.setpoint_range[1] > pwm_volts):
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


