############################################################################
#                                                                           #
#   Team:       Mayans                                                      #
#   Authors:    Justin Berthelot, Dawson Markham, Emily Rumfola             #
#   Date:       04/23/19                                                    #
#   Program: Chat (Timing) Covert Channel                                   #
#   Description: Program connects to a host via a specified port. The time  #
#		   intervals betweeen received characters is monitered and  #
#		   the resulting binary message is decoded into ASCII. If   #
#		   DEBUG is set to true the time intervals can be viewed.   #
#                                                                           #
############################################################################

# IMPORT LIBRARIES
import socket
from time import time
from binascii import hexlify, unhexlify
import sys


# CONSTANTS
DEBUG = False	    # Set to true to receive output of intervals
ONE   = 0.1	    # Time that represents 1
ZERO  = 0.025	    # Time that represents 0
HOST  = "localhost" # Host name
PORT  = 1337	    # Port number
BITS  = 8	    # Decode as 7-bit or 8-bit

# CovertTiming Function
def CovertTiming():
	# GLOBAL VARIABLES
	global DEBUG, ONE, ZERO, HOST, PORT, BITS

	# Attempt to connect to host, close program if connection fails
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
	except:
		print "\nConnection Failed\n"
		exit(1)

	# Notify user of connection
	print "\nConnected to server\n"

	# Variables
	covert_bin = ""	    	# Store binary message
	covert = ""	    	# Store translated message
	i = 0		    	# Counter
	if DEBUG:		# Create list if in debug mode
		intervals = []

	# Wait for and store data
	data = s.recv(4096)

	# As long as the received data is not "EOF" continue listening
	while (data.rstrip("\n") != "EOF"):
		sys.stdout.write(data)		# Print data as it is received
		sys.stdout.flush()
		t0 = time()			# Save the start time
		data = s.recv(4096)		# Listen for next piece of data
		t1 = time()			# Save the end time
		delta = round(t1 - t0, 4)	# Calculate the wait time to 4 decimal places
		
		# If in Debug mode, store the elapsed time
		if DEBUG:
			intervals.append(delta)
		
		# If not in Debug mode, translate time to a bit
		else:
			if (delta >= ONE):
				covert_bin += "1"
			else:
				covert_bin += "0"

	# Notify user that connection has closed
	print "\n\nDisconnected from server\n"
	
	# If in debug mode, display informatiom
	if DEBUG:
		print "Host:    " + HOST
		print "Host_IP: " + socket.gethostbyname(HOST)
		print "Port:	 {}".format(PORT)
		print "Time Intervals:"
		print intervals
	
	# Go through the binary message, and convert to ASCII
	for i in range(0,len(covert_bin),BITS):
		b = covert_bin[i:i+BITS]	# Take string of the length of BITS (7 or 8)
		n = int("0b{}".format(b), 2)	# Format as binary string
		
		# Attemp to convert to ASCII, if unable to do so, inform user with '?'
		try:
			covert += unhexlify("{0:x}".format(n))
		except TypeError:
			covert += "?"
	
		# Check that the message has not ended, if it has, then break
		if (covert[-3:] == "EOF"):
			break
	
	# Display the decoded message
	print covert[:-3] + "\n"

########
# MAIN #
########

CovertTiming()	# Run CovertTiming Function
