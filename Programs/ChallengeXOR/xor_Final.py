##############################################################################
#									     #
#  Team:  Mayans							     #
#  Names: Dawson Markham, Justin Berthelot, Emily Rumfola, Ryan Utley,       #
#               Matthew Eldridge, Caleb Snook, Valentin Le Gall              #
#  Date:  5/1/2019							     #
#									     #
#  Description: Program takes user input performs an XOR operation using a   #
#		 file listed as 'key'.					     #
##############################################################################

# LIBRARIES
import sys

# CONSTANTS
BUFFER_SIZE = 4096  # Size is in bytes
KEYNAME     = 'stegfile2' # Filename for the key

# XOR Function
def XOR():
	# Open key file
	key_fl = open(KEYNAME, 'r')

	# Initialize Variables
	converted = ''
	text_pos = 0
	key_pos  = 0

	# Loop until input has ended
	while True:
		# Reset buffers
		text_buff = []
		key_buff  = []

		# Fill buffers
		while (len(text_buff) < BUFFER_SIZE):
			text_tmp = sys.stdin.read(1) # Store the next byte of each file
			key_tmp  = key_fl.read(1)

			if not text_tmp:   # If the input complete, break from loop
				break

			if not key_tmp:		# If end of key file has been reached,
				key_fl.close()  #	close and reopen
				key_fl = open(KEYNAME, 'r')
							
			text_buff.append(text_tmp) # Append the character to the buffers
			key_buff.append(key_tmp)
		
		# XOR the corresponding characters and add to converted string
		for i in range(0,len(text_buff)):
			converted += chr(ord(text_buff[i]) ^ ord(key_buff[i]))

		# If input has been complete, break loop
		if not text_tmp: 
			break
	
	# Print the converted string
	print converted

############
#   MAIN   #  
###########
XOR()
