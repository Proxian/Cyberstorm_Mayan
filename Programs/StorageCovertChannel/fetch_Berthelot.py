 ################################################################
#                                                               #
#   Authors: Justin Berthelot                                   #
#   Date: 04/02/19                                              #
#                                                               #
#   Description: ["FTP (storage) Covert Channel"] Connects      #
#                   via FTP to 'jeangourd.com' with username    #
#                   'anonymous' and no password. Uses file      #
#                   permissions in binary as the method for     #
#                   encoded data.                               #
################################################################

###LIBRARIES###
from ftplib import FTP
from sys import stdout

###VARIABLES###

# Determines the type of decoding
#   'False' : 10-bit-concatenated ASCII data
#   'True'  : 7-bit ASCII data
METHOD = True

# Initialize lists
data = []
bindata = []

###FUNCTIONS###

# 7-bit binary conversion
def BinDecode(data):
    # Loops over the data in 7-bit increments
    for i in range(0,len(data),7):
        # prints the ASCII equivalent character
        stdout.write(chr(int(data[i:i+7], 2)))

def CovertDecoder():
    # Use global variable
    global METHOD

    # Assume 'jeangourd.com' host with username anonymous
    #   and no password
    ftp = FTP("jeangourd.com")
    ftp.login(user="anonymous")

    # 7-bit
    if METHOD:
        # Change to the '7' directory
        ftp.cwd("7")
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
                        bindata.append("1")
                    # Bit not set: 0
                    else:
                        bindata.append("0")
    # 10-bit
    else:
        # Change to the '10' directory
        ftp.cwd("10")
        # Store the list of files in a Python list
        ftp.dir(data.append)
        # Loop over the files in the list
        for line in data:
            # Loop over the first 10 characters
            for character in line[0:10]:
                # Bit set: 1
                if character != "-":
                    bindata.append("1")
                # Bit not set: 0
                else:
                    bindata.append("0")
    # Exit 'formally'
    ftp.close()
    # Print the decoded binary data (via stdout)
    BinDecode("".join(bindata))

###MAIN###
CovertDecoder()
