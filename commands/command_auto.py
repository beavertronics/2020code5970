# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

class Command_Auto(Command):
	''' 
	Robot should drive across the field (under trench or through middle),
	line up, and shoot all balls it is carrying. Optionally pick up more after.
	'''

	def __init__(self, robot):
		Command.__init__(self, name='Command_Auto')
		# Recognize as a wpilib command
		#print("command_auto init")
		# Command.__init__(self)
		#self.requires(robot.#XXX)
		#self.#XXX = robot.something
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		pass
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		return False

	def end(self):
		pass
	
	def interrupted(self):
		self.end()
