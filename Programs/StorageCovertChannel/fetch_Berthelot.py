 ############################################################################
#                                                                           #
#   Team:       Mayans                                                      #
#   Authors:    Justin Berthelot, Dawson Markham, Emily Rumfola             #
#   Date:       04/05/19                                                    #
#   Program: FTP (storage) Covert Channel                                   #
#   Description: Program joins FTP server and goes to the directory as      #
#		    specified by mode. A list of files is then made and     #
#		    their permissions are translated to binary. Then binary #
#		    message is decoded as specified by mode by implementing #    #
#		    a binary decoder.                                       #
#                                                                           #
############################################################################

###LIBRARIES###
from ftplib import FTP
from sys import stdout

###VARIABLES###

# Determines the type of decoding
#   '10' : 10-bit-concatenated ASCII data
#   '7'  : 7-bit ASCII data
#   (string)
METHOD = "7"
# Directory name
#   (Directory to switch to)
DIRNAME = "7"
# 7-bit or 8-bit binary
#   (integer)
BIT_TYPE = 7
# Server name
HOSTNAME = "jeangourd.com"
# User name
USERNAME = "anonymous"
# Initialize lists
data = []

###FUNCTIONS###

# Binary conversion
def BinDecode(data):
    global BIT_TYPE
    # Loops over the data in increments
    for i in range(0,len(data),BIT_TYPE):
        # prints the ASCII equivalent character
        stdout.write(chr(int(data[i:i+BIT_TYPE], 2)))

def CovertDecoder():
    # Use global variables
    global METHOD, HOSTNAME, USERNAME, DIRNAME

    bindata = ""
    # Assume 'jeangourd.com' host with username anonymous
    #   and no password
    ftp = FTP(HOSTNAME)
    ftp.login(user=USERNAME)

    # 7-bit
    if METHOD == "7":
        # Change to the '7' directory
        ftp.cwd(DIRNAME)
        # Store the list of files in a Python list
        ftp.dir(data.append)
        # Loop over the files in the list
        for line in data:
            # Ignore data that has any bit set in the first
            #   3 places
            if line[0:3] == "---":
                # Loop over the last 7 permission characters
                for character in line[3:10]:
                    # Bit set: 1
                    if character != "-":
                        bindata += "1"
                    # Bit not set: 0
                    else:
                        bindata += "0"
    # 10-bit
    elif METHOD == "10":
        # Change to the '10' directory
        ftp.cwd(DIRNAME)
        # Store the list of files in a Python list
        ftp.dir(data.append)
        # Loop over the files in the list
        for line in data:
            # Loop over the first 10 characters
            for character in line[0:10]:
                # Bit set: 1
                if character != "-":
                    bindata += "1"
                # Bit not set: 0
                else:
                    bindata += "0"
    # Exit 'formally'
    ftp.close()
    # Print the decoded binary data (via stdout)
    BinDecode(bindata)

###MAIN###
CovertDecoder()
