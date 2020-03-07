# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib import XboxController
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

# Button commands
from command_intake_pickup import Command_Intake_Pickup
from command_shoot import Command_Shoot
from do_big_climb import Do_Big_Climb
from do_little_climb import Do_Little_Climb
from do_winch import Do_Winch
from command_climb_up import Command_Climb_Up
from command_climb_down import Command_Climb_Down

#XXX For testing
from do_shoot import Do_Shoot
from do_activate_feeder import Do_Activate_Feeder
from do_carrier import Do_Carrier
from do_intake import Do_Intake
from do_big_climb_test import Do_Big_Climb_Test
from do_little_climb_test import Do_Little_Climb_Test

# Non-button commands

class OI():
	def __init__(self, robot):

		self.robot = robot

		self.left_joy = self.robot.left_joy 
		self.right_joy = self.robot.right_joy 
		self.xbox = self.robot.xbox

		# First character indicates self.right or self.left, 
		# second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is self.left top 0 


		'''
		JoystickButton and Xbox button assignments
		'''
		# I think ltop1 is left trigger. Vice versa for right
		ltop1 = JoystickButton(self.left_joy, 1)
		ltop2 = JoystickButton(self.left_joy, 2)
		ltop3 = JoystickButton(self.left_joy, 3)
		ltop4 = JoystickButton(self.left_joy, 4)
		ltop5 = JoystickButton(self.left_joy, 5)
		ltop6 = JoystickButton(self.left_joy, 6)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		rtop4 = JoystickButton(self.right_joy, 4)
		rtop5 = JoystickButton(self.right_joy, 5)
		rtop6 = JoystickButton(self.right_joy, 6)

		xboxX = JoystickButton(self.xbox, 3)
		xboxY = JoystickButton(self.xbox, 4)
		xboxB = JoystickButton(self.xbox, 2)
		xboxA = JoystickButton(self.xbox, 1)
		xboxLB = JoystickButton(self.xbox, 5)
		xboxRB = JoystickButton(self.xbox, 6)
		#xbox_left_XY = self.xbox.getY(9)
		#self.xbox_XY = JoystickButton(self.xbox, 9)
		self.xbox_left_XY = self.xbox.getX()
		xboxBACK = JoystickButton(self.xbox, 7)
		xboxSTART = JoystickButton(self.xbox, 8)


#		# whenActive and whenInactive allows toggle between 2 commands

		'''
		Joystick 0 / Left Joystick Commands
		'''

		'''
		Joystick 1 / Right Joystick Commands
		'''

		rtop1.whenPressed(Do_Feeder(self.robot))

#		# Button 2 toggles shifters
#		rtop2.toggleWhenPressed(Do_Shifters_Toggle(self.robot))
#
		'''
		Joystick 2 / Xbox Controller Commands
		'''	
#		# In frame
		#XXX The INTENDED commands for comp
		xboxY.whileHeld(Do_Winch(self.robot))
		#xboxX.whileHeld(Command_Shoot(self.robot))
		#xboxA.whileHeld(Do_Big_Climb(self.robot))
		#xboxB.whileHeld(Do_Little_Climb(self.robot))
		xboxRB.whileHeld(Command_Intake_Pickup(self.robot))
		xboxLB.whileHeld(Do_Carrier(self.robot))

		#XXX debugging motor controller positions
		#XXX Do_Activate_Feeder needs testing
		#xboxA.whileHeld(Do_Activate_Feeder(self.robot))
		#xboxB.whileHeld(Do_Carrier(self.robot))
		xboxX.whileHeld(Do_Shoot(self.robot))
		#xboxY.whileHeld(Do_Intake(self.robot))

		# CLIMBER
		# A was actuating biggum
		#xboxA.whileHeld(Command_Climb_Up(self.robot))
		# B was unactuating biggum
		#xboxA.whenReleased(Command_Climb_Down(self.robot))
		# on second try, A actuated both and B unactuated both
		# before, A was big and B was little
		xboxA.whileHeld(Do_Big_Climb_Test(self.robot))
		xboxB.whileHeld(Do_Little_Climb_Test(self.robot))
