#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
from wpilib.buttons.joystickbutton import JoystickButton
import time
from networktables import NetworkTables

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./subsystems') 
sys.path.append('./commands') 

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from left_motors import Left_Motors
from right_motors import Right_Motors
from shifters import Shifters

from drivetrain import Drivetrain

# Teleop init command
from oi import OI

class BeaverTronicsRobot(wpilib.TimedRobot): 

	def robotInit(self):
		# Instances of classes

		# Instantiate Subsystems
		self.shifters = Shifters()
		self.drivetrain = Drivetrain(self)

		# Instantiate Joysticks
		self.left_joy = wpilib.Joystick(0) 
		self.right_joy = wpilib.Joystick(1)
		
		# Instantiate Xbox
		self.xbox = wpilib.Joystick(2)

		# Instantiate OI; must be AFTER joysticks are inited
		self.oi = OI(self)

		self.timer = wpilib.Timer()
		self.loops = 0

		# untested vision
		#XXX might crash sim
		#wpilib.CameraServer.launch("vision.py:main")
		
	def autonomousInit(self):
		Scheduler.getInstance().removeAll()
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		
	def autonomousPeriodic(self):
		Scheduler.getInstance().run()

	def teleopInit(self):
		self.loops = 0
		self.timer.reset()
		self.timer.start()
		Scheduler.getInstance().removeAll()
		Scheduler.getInstance().enable()

	def teleopPeriodic(self):
		Scheduler.getInstance().run()

		# Keeping track of TimedRobot loops through code
		self.loops += 1
		if self.timer.hasPeriodPassed(1):
			self.logger.info("%d loops / second", self.loops)
			self.loops = 0

	def disabledInit(self):
		Scheduler.getInstance().removeAll()

	def disabledPeriodic(self):
		return None

	def testInit(self):
		pass

	def testPeriodic(self):
		pass

if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
