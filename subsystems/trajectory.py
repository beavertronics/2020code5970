# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#Sources:
# https://github.com/robotpy/robotpy-pathfinder/blob/master/examples/tank.py

import pathfinder as pf
import math
import matplotlib.pyplot as plt

def generate_path():
	#XXX need to pick good waypoints
	# waypoints initialize at 0, 0
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
		dt=0.05, 
		#XXX max velocity is probably in the units that your encoder and gyro
		# calculate it in
		max_velocity=1,
		max_acceleration=2,
		max_jerk=3
		)

	# pass in wheelbase width in meters
	#XXX wrong width
	modifier = pf.modifiers.TankModifier(trajectory).modify(1)
	mx, my = zip(*[(m.y, m.x) for m in points])
	plt.scatter(mx, my, c="r")

	# plot the trajectory
	x, y = zip(*[(seg.y, seg.x) for seg in trajectory])
	plt.plot(x, y)

	# annotate with time
	for i in range(0, len(trajectory), int(0.5 / dt)):
		plt.annotate(
			"t=%.2f" % (i * dt,),
			xy=(x[i], y[i]),
			xytext=(-20, 20),
			textcoords="offset points",
			arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
		)

	plt.show()
	return modifier

	# Do this in another file to get the trajectories
	#left_traj = modifier.getLeftTrajectory()
	#right_traj = modifier.getRightTrajectory()

if __name__ == "__main__":
	generate_path()

