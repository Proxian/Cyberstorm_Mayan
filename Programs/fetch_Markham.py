########################################################################
# Team:    Mayans
# Name:    Dawson Markham
# Date:    4/5/2019
# Program: FTP (storage) Covert Channel
# Descritption: Program joins FTP server and goes to the directory as
#		specified by mode. A list of files is then made and 
#		their permissions are translated to binary. Then binary
#		message is decoded as specified by mode by implementing
#		a binary decoder.
########################################################################

# Import libraries
from ftplib import FTP
import sys

# CONTROL VARIABLES
mode = "7" 			# Modes are: 7 or 10
server = "jeangourd.com"	# FTP server
ftp_user = "anonymous"		# Username

###############
#  FUNCTIONS  #
###############

# 7-Bit Decoder
def Bit_7():
        # Set an empty string
	decoded = ""

        # Go through input in groups of seven characters, convert to appropiate character and add to string
        for i in range(0, len(cipher), 7):
                temp =  cipher[i:i+7]
		decoded = decoded + chr(int(temp, base=2))

	# Display decoded string
	print decoded

# 8-Bit Decoder
def Bit_8():
        # set an empty string
        decoded = ""

	# Go through input in groups of 8 characters, convert to appropriate character and add to string
        for i in range(0, len(cipher), 8):
                temp =  cipher[i:i+8]
                decoded = decoded + chr(int(temp, base=2))

	# Display decoded string
	print decoded

###############
#    MAIN     #
###############

# Join and login to server
ftp = FTP(server)
ftp.login(user=ftp_user)

# Use mode to go to specified directory
if (mode == "7"):
	ftp.cwd("7")

elif (mode == "10"):
	ftp.cwd("10")

else:
	print "Incorrect mode: Please use the character 7 or the character 10"
	ftp.quit()
	exit

# Create list of files
files = []
ftp.dir(files.append)

# Create empty string to hold binary string
cipher = ""

# Convert the permissions of each file to binary
for i in range (0, len(files)):
	binary = ""		# Reset as empty string

	# Go through the  first 10 character of the line (the permissions
	for j in range(0,10):			
		if (files[i][j] != '-'):	# If not '-', add 1 
			binary = binary + '1'
		else:				# Add 0 otherwise
			binary = binary + '0'
	
	# If mode is 7-Bit, append the last 7 bits to cipher if the first three bits do not contain a 1
	if (mode == '7'):
		if (binary[0] != '1' and  binary[1] != '1' and binary[2] != '1'):
			cipher = cipher + binary[3:]
	# Else, add 10-bit binary to cipher
	else:
		cipher = cipher + binary

# Close FTP connection
ftp.quit()	

# Check if cipher contains a multiple of 7 or 8 bits
if ((len(cipher) % 7) == 0 or (len(cipher) % 8) == 0 ):
	# Check if 7-Bit Decoder can be used
	if ((len(cipher) % 7) == 0 ):
        	Bit_7()

	# Check if 8-Bit Decoder can be used
	if ((len(cipher) % 8) == 0 ):
		Bit_8()

# Else, use both decoders
else:
	print "7-Bit:"
	Bit_7()
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "8-Bit:"
	Bit_8()

