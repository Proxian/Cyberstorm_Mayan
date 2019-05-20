###############################################################################
#									      #
# Team: Mayans 								      #
# Name: Dawson Markham    						      #
# Date: 4/21/2019							      #
# Description: Chat-Client program can take more than two timings and attempt #
#		decryption for every combination of timings.		      #
#									      #
###############################################################################

# IMPORT
import socket
from time import time
from binascii import hexlify, unhexlify
import sys

# CONSTANTS
DEBUG = True
TIME  = [0.025, 0.1, 0.125, 0.15]
HOST  = "localhost"
PORT  = 1337
BITS  = 8
ONE   = None
ZERO  = None

# Get indexes
if (ONE != None and ZERO != None):
	one  = TIME.index(ONE)
	zero = TIME.index(ZERO)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))
except:	
	print "\nConnection Failed\n"
	exit(1)

print "\nCONNECTED...\n"

# Initialize Variables
msg_time = ""
covert_bin = ""
covert = ""
if DEBUG:
	intervals = []
i = 0

# Get first charcater
data = s.recv(4096)

# As long as the received data is not "EOF" continue listening
while (data.rstrip("\n") != "EOF"):
	sys.stdout.write(data)          # Print data as it is received
        sys.stdout.flush()
        t0 = time()                     # Save the start time
        data = s.recv(4096)             # Listen for next piece of data
        t1 = time()                     # Save the end time
        delta = round(t1 - t0, 4)       # Calculate the wait time to 4 decimal places
    
        # If in Debug mode, store the elapsed time
        if DEBUG:
	        intervals.append(delta)
        # If not in Debug mode, translate time to a bit
#       else:
        if (delta >= TIME[len(TIME)-1]):
	        msg_time += "{}".format(len(TIME)-1)
        elif (delta < TIME[1]):
	        msg_time += "0"
	else:
		i = 0
		for i in range(1,len(TIME)-1):				# Store the index number (time>= index and time <index+1)
			if (delta >= TIME[i] and delta < TIME[i+1]):
				msg_time += "{}".format(i)
print "\n\nDISCONNECTED\n"
s.close()

# If in debug mode, display informatiom
if DEBUG:
        print "Host:    " + HOST
        print "Host_IP: " + socket.gethostbyname(HOST)
        print "Port:     {}".format(PORT)
	print "Times:   ",
	print TIME
	print "msg_time:" + msg_time
        print "Time Intervals:"
	print intervals

# If ONE and ZERO not scpecified, go through every iteration
if (ONE == None or ZERO == None):
	j = 0
	for j in range(0,len(TIME)):
		k = 0
		for k in range(0,len(TIME)):
			if (j == k):	# The same timing cannot be one and zero
				pass
			
			else:	
				covert_bin = ""
				m = 0
				for m in range(0, len(msg_time)):
					if (int(msg_time[m],10) == j): # Treat j as ONE
						covert_bin += "1"
					elif (int(msg_time[m],10) == k): # Treat k as ZERO
						covert_bin += "0"
				n = 0
				covert = ""
				for n in range(0,len(covert_bin),BITS):
					b = covert_bin[n:n+BITS]
					c = int("0b{}".format(b), 2)    # Format as binary string
	
					# Attempt to decode into ASCII
					try:
					 	covert += unhexlify("{0:x}".format(c))
					except TypeError:
						covert += "?"

					if (covert[-3:] == "EOF"): # Break if end of file
						break
				
				# Display combination and resulting message
				print "\n1: {}".format(TIME[j])
				print "0: {}\n".format(TIME[k])

				print covert[:-3] + "\n"

# Else, use only the specified ONE and ZERO
else:
	# Store binary
	covert_bin = ""
	m = 0
	for m in range(0,len(msg_time)):
		if (int(msg_time[m],10) == one):	# Check if the same index for one or zero
			covert_bin += "1"		
		elif (int(msg_time[m],10) == zero):
			covert_bin += "0"

	n = 0
	covert = ""	# Store ASCII
	for n in range(0,len(covert_bin),BITS):
		b = covert_bin[n:n+BITS]
		c = int("0b{}".format(b), 2)    # Format as binary string

		# Attempt ASCII conversion
		try:
		 	covert += unhexlify("{0:x}".format(c))
		except TypeError:
			covert += "?"

		if (covert[-3:] == "EOF"):	# Break if end of file
			break

	print covert[:-3] + "\n"
