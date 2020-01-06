# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# toggles Shifters between low and high gear
class Do_Shifters_Toggle(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot_shifters = robot.shifters
		# uses solenoids 0 and 1
		'''
		Shifters can onlu be in two states:
			1: actuated(high gear)
			2: unactuated(low gear)

		States 1 & 2 (alternating): requires Shifters
		'''
		self.requires(self.robot_shifters)

	def initialize(self):
		# actuate solenoids for shifters
		# remain in State 1(high gear) until end of command
		# initializes on [first press] of "Joystick 1 '2' button"
		self.robot_shifters.shifters_on()
		print("shifters on!")

	def execute(self):
		# command loops continuously doing nothing until
		# [second press] of "Joystick 1 '2' button" 
		return None

	def isFinished(self):
		return None

	def end(self):
		# unactuate solenoids for shifters
		# shifts to State 2(low gear)
		# ends on [second press] of "Joystick 1 '2' button"
		self.robot_shifters.shifters_off()
		print ("shifters off!")

	def interrupted(self):
		print("Command 'shifters_toggle' interrupted!")
		self.end()

