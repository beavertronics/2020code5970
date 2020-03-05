# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
from networktables import NetworkTables

class Do_Auto(Command):
	''' 
	Robot should drive across the field (under trench or through middle),
	line up, and shoot all balls it is carrying. Optionally pick up more after.
	'''

	def __init__(self, robot):
		Command.__init__(self, name='Do_Auto')
		print("Do_Auto init")
		self.dt = robot.drivetrain
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		table = NetworkTables.getTable('SmartDashboard')
		initial_pos = table.getData('initial_pos')
		#XXX Doing this will start the path following immediately. May want this
		# in the execute or something
		path = self.dt.which_path(initial_pos)
	
	def execute(self):
		"""Called iteratively by Scheduler"""
		pass

	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		#XXX should be over when auto is over
		pass

	def end(self):
		self.dt.stop_motors()
	
	def interrupted(self):
		self.end()
