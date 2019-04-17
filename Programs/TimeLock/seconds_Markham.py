###############################################
# Dawson Markham
# 4/15/2019
# 
# Program calculates the number of seconds
#	bewteen two times
###############################################

# Libraries
import sys
import time
import hashlib

# Constants
DEBUG     = True			# True -> debug active
TEST_TIME = "2013 05 06 07 043 25"      # Time used as current if debug is active

# Function returns the number of seconds
def getSec(time_str):
        date_time = time_str		# Create list of the date
        list_date  = date_time.split()

	# Get the number of seconds and create a time_struct
        time_sec  = time.mktime((int(list_date[0],10), int(list_date[1],10), int(list_date[2],10), int(list_date[3],1
        time_date = time.localtime(time_sec)
 
 	# If Daylight savings has changed the number of seconds, correct seconds
	if time_date.tm_isdst:
	        time_sec -= 3600*time_date.tm_isdst
	
	# Return the number of seconds
	return time_sec

# Get the number of seconds for epoch
epoch_time = getSec(sys.stdin.read())

# If debugging, set the test time as current time, else use the current time
if DEBUG:
	current_time = getSec(TEST_TIME)
else:
        current_time = time.time()

# Get the elapsed time as string and display
elapsed_time = '{}'.format(current_time - epoch_time)
print elapsed_time

