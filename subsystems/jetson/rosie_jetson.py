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

    # filter by color (green)
    # other filters (erode etc)
    # make object out of white pixel things but not too small of pixel things
    # find location of object
    # return the location / send to the roborio
