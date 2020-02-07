# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import logging
import time

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y | %H:%M:%S')

for i in range(1,6):
    logging.critical("No need to be so critical, I've told you " + 
            str(i) + " time(s) already!")
    time.sleep(2.5)



"""
When logger is implemented it should log everything into an external
logging file. After some amount of time (one day, week?) this file will
be deleted. Everytime the robot runs it can check age of file, delete 
anything to old?
Log messages might need full date, maybe just timestamp?
Maybe define our own logging levels?
"""
