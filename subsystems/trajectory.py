# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#Sources:
# https://github.com/robotpy/robotpy-pathfinder/blob/master/examples/tank.py

import pathfinder as pf
import math

def generate_path():
	#XXX need to pick good waypoints
	waypoints = [
		pf.Waypoint(0, 0, 0),
		pf.Waypoint(1, 1, 1),
		pf.Waypoint(2, 2, 2)
		]
	
	# This returns a tuple of TrajectoryInfo and a trajectory constituting
	# a list of points to follow over time)
	info, trajectory = pf.generate(
		waypoints,
		pf.FIT_HERMITE_CUBIC,
		#XXX not sure what that does
		pf.SAMPLES_HIGH,
		#XXX dt means change in time in seconds?
		# 50ms
		dt=0.05
		#XXX max velocity is probably in the units that your encoder and gyro
		# calculate it in
		#XXX commented out because interfering with pid testing. invalid syntax
		#max_velocity=1
		#max_acceleration=2
		#max_jerk=3
		)

	# pass in wheelbase width in meters
	#XXX wrong width
	modifier = pf.modifiers.TankModifier(trajectory).modify(1)
	return modifier

	# Do this in another file to get the trajectories
	#left_traj = modifier.getLeftTrajectory()
	#right_traj = modifier.getRightTrajectory()

