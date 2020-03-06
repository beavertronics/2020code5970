# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import cv2
import sys
import numpy as np
from math import sin, radians, sqrt
import time
import mmap
import json
import logging

class Camera():
	def __init__(self, cam_index):
		self.cam_index = cam_index
		self.cam = cv2.VideoCapture(self.cam_index)
		if not self.cam.isOpened():
			sys.stderr.write("No camera could be opened for capture\n")
			exit(1)
		self.debug = False

	def set_debug(self, on_or_off):
		self.debug = on_or_off

	def setup(self):
		contrast = self.cam.get(11)
		new_con = self.cam.set(11, 0.1)
		if self.debug:
			print("old contrast " + (str(contrast)))
			print("new contrast " + (str(new_con))) #-trast

	def read(self):
		img = self.cam.read()
		return img
	
	def shutdown(self):
		cv2.destroyAllWindows()
		self.cam.release()

class Rosie_Jetson():
	''' This is all the processing functions the Jetson will run.'''

	def __init__(self):
		self.cam = Camera(1)

	# get feed from camera
	def get_feed(self):
		self.retval, self.frame = self.cam.read()

	# hsv filtering
	def hsv_frame(self):
		hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
		return(hsv_frame)

	# filter by color (green)
	# green filter range (temporary values): [0,0,0] [180,255,255]
	def color_mask(self):
		hsv_frame = self.hsv_frame()
		frame = self.frame
		#lower_bound = np.array([60,0,254])
		#upper_bound = np.array([65,5,255])
		lower_bound = np.array([46, 50, 0])
		upper_bound = np.array([80, 255, 255])
		color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
		return(color_mask)

	# other filters (erode etc)
	def erode(self):
		color_mask = self.color_mask()
		kernel = np.ones((5, 5), np.uint8)
		erosion = cv2.erode(color_mask, kernel, iterations=1)
		return(erosion)

	def dilate(self):
		erosion = self.erode()
		kernel = np.ones((5, 5), np.uint8)
		dilation = cv2.dilate(erosion, kernel, iterations=1)
		return(dilation)

	# make object out of white pixel things
	# but not too small of pixel things
	# takes abstract filter and makes a concrete object
	def find_contours(self):
		image = self.dilate()
		contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, 
			cv2.CHAIN_APPROX_SIMPLE)
		return(contours)

	def largest_contour(self):
		contours = self.find_contours()
		areas = [cv2.contourArea(c) for c in contours]
		max_index = np.argmax(areas)
		largest_contour=contours[max_index]
		return(largest_contour)

	def bounding_rectangle(self):
		largest_contour = self.largest_contour()
		x, y, w, h = cv2.boundingRect(largest_contour)
		rectangle = [x, y, w, h]
		return(rectangle)
	
	# find location of object
	# return the location / send to the roborio

def find_filter():
	# Capture an image from the camera; 0 = built in webcam or external camera
	cap = cv2.VideoCapture(1)
	ret, frame = cap.read()
	
	# Create windows for display
	cv2.namedWindow('HSV_filter')
	cv2.namedWindow('min')
	cv2.namedWindow('max')

	# Min HSV trackbars
	cv2.createTrackbar('minH','min', 0, 180, lambda x:None)
	cv2.createTrackbar('minS','min', 0, 255, lambda x:None)
	cv2.createTrackbar('minV','min', 0, 255, lambda x:None)
	# Max HSV trackbars
	cv2.createTrackbar('maxH','max', 180, 180, lambda x:None)
	cv2.createTrackbar('maxS','max', 255, 255, lambda x:None)
	cv2.createTrackbar('maxV','max', 255, 255, lambda x:None)
	
	keypressed = 1
	while(True):
		# Read a frame from the video capture
		ret, frame = cap.read()
		
		# Create HSV converted frame
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# Update lower and upper HSV values from trackbar
		lowerHSV = numpy.array([cv2.getTrackbarPos('minH','min'),
			cv2.getTrackbarPos('minS','min'),cv2.getTrackbarPos('minV','min')])
		upperHSV = numpy.array([cv2.getTrackbarPos('maxH','max'),
			cv2.getTrackbarPos('maxS','max'),cv2.getTrackbarPos('maxV','max')])
		
		# Create HSV mask and filter
		HSV_mask = cv2.inRange(hsv, lowerHSV, upperHSV)
		HSV_filter = cv2.bitwise_and(frame,frame, mask=HSV_mask)
		
		# Show image
		cv2.imshow('HSV_filter', HSV_filter)
		
		# Wait for button press
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
	# Destroy windows
	cv2.destroyAllWindows()
	cap.release()

# instantiate daisy as a rosie_jetson
daisy = Rosie_Jetson()
find_filter()
#while(True):
#    # Capture frame-by-frame
#	daisy.get_feed()
#	mask = daisy.color_mask()
#	rectangle = daisy.bounding_rectangle()
#	test = cv2.bitwise_and(daisy.frame, daisy.frame, mask= mask)
#	cv2.rectangle(test, (rectangle[0],rectangle[1]), (rectangle[0]+rectangle[2],rectangle[1]+rectangle[3]), (255,255,255), 2)
#    # Display the resulting frame
#	cv2.imshow('frame',daisy.frame)
#	cv2.imshow('test',test)
#	if cv2.waitKey(1) & 0xFF == ord('q'):
#		break
#
## When everything done, release the capture
#daisy.cam.shutdown()
