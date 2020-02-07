# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import cv2
# numpy pronounced (NUM-PI)
import numpy as np
import mmap
import json
import logging
from camera import Camera

class Rosie_Jetson():
    ''' This is all the processing functions the Jetson will run.'''

    def __init__(self):
        self.cam = Camera()

    # get feed from camera
    def get_feed(self):
        while True:
            self.retval, self.frame = self.cam.read()
            if not self.retval:
                #XXX error message w logger?
                # send to drivestation also
                time.sleep(1)
                continue

	# hsv filtering
	def hsv_frame(self):
		hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
		return(hsv_frame)

	# filter by color (green)
	# green filter range (temporary values): [0,0,0] [180,255,255]
	def color_mask(self):
		hsv_frame = hsv_frame()
		frame = self.frame
		lower_bound = np.array([75, 100, 150])
		upper_bound = np.array([95, 255, 255])
		color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
		return(color_mask)

    # other filters (erode etc)
	def erode(self):
		color_mask = self.color_mask()
		kernel = np.ones((5, 5), np.uint8)
		erosion = cv2.erode(color_mask, kernel, iterations=1)
		return(erosion)

	def dilate(self):
		erosion = erode()
		kernel = np.ones((5, 5), np.uint8)
		dilation = cv2.dilate(erosion, kernel, iterations=1)
		return(dilation)

	# make object out of white pixel things
	# but not too small of pixel things
	# takes abstract filter and makes a concrete object
	def find_contours(self):
		image = dilate()
		contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, 
				cv2.CHAIN_APPROX_SIMPLE)
		return(contours)

	def largest_contour(self):
		contours = find_contours()
		areas = [cv2.contourArea(c) for c in contours]
		max_index = np.argmax(areas)
		largest_contour=contours[max_index]
		return(largest_contour)

	def bounding_rectangle(self):
		largest_contour = largest_contour()
		x, y, w, h = cv2.boundingRect(cnt)
		rectangle = [x, y, w, h]
		return(rectangle)
	
	# find location of object
    # return the location / send to the roborio
