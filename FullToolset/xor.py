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
KEYNAME     = 'key' # Filename for the key

# Prints a description
def PrintHelp():
    print "Usage: 'python xor.py <keyfile> <normalfile>'"

# XOR Function
def XOR(keyfile, myfile):
    # Open key file
    try:
        key_fl = open(keyfile, 'r')
    except:
        print "Could not open {}!".format(keyfile)
        exit(1)
    # Open normal file
    try:
        norm_fl = open(myfile, 'r')
    except:
        print "Could not open {}!".format(myfile)
        exit(1)
    
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
            # Store the next byte of each file
            text_tmp = norm_fl.read(1)
            key_tmp  = key_fl.read(1)

            # If the input complete, break from loop
            if not text_tmp:
                break

            # If end of key file has been reached, close and reopen
            if not key_tmp:
                key_fl.close()
                key_fl = open(keyfile, 'r')

            # Append the character to the buffers                                     
            text_buff.append(text_tmp)
            key_buff.append(key_tmp)
        
        # XOR the corresponding characters and add to converted string
        for i in range(0,len(text_buff)):
            converted += chr(ord(text_buff[i]) ^ ord(key_buff[i]))

        # If input has been complete, break loop
        if not text_tmp: 
            break

    norm_fl.close()
    # Print the converted string
    print converted

def Main():
    # Check to make sure that the correct number of arguments were provided
    if (len(sys.argv) >= 3):
        # KeyFile
        keyfile = sys.argv[1]
        # NormalFile
        myfile = sys.argv[2]
        XOR(keyfile, myfile)
    else:
        PrintHelp()

############
#   MAIN   #  
###########
Main()
