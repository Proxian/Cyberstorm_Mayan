 ############################################################################
#                                                                           #
#   Team:       Mayans                                                      #
#   Authors:    Justin Berthelot                                            #
#   Date:       05/01/19                                                    #
#   Program: FTP (storage) Covert Channel                                   #
#                                                                           #
############################################################################

###LIBRARIES###
from ftplib import FTP
import sys
import time
import hashlib

###VARIABLES###

# Use arbitrary time
DEBUG     = True
TEST_TIME = "2017 03 23 18 02 06"
EPOCH_TIME = "1970 01 01 00 00 00"

# Lockout time
VALID_TIME = 60

# Port
PORT = 21

# Server name
HOSTNAME = "jeangourd.com"

# User name
USERNAME = "anonymous"

# FUNCTIONS

# Function gets the number of seconds from a date string ("YYYY MM DD HH mm ss")
def getSec(date_time):

    # Split string into list
    list_date  = date_time.split()

    # Convert date to number of seconds and convert back to date in local time
    time_sec  = time.mktime((int(list_date[0],10), int(list_date[1],10), int(list_date[2],10), int(list_date[3],10), int(list_date[4],10), int(list_date[5],10), 0, 0, 0))
    time_date = time.localtime(time_sec)

    # If date given is changed by daylight saving time, correct the change
    if time_date.tm_isdst:
        time_sec -= 3600*time_date.tm_isdst
    
    # Return the number of seconds
    return time_sec


# Function gets time difference, creates hash and forms code
def timeLock(epoch_time):
    global VALID_TIME

    epoch_time = getSec(epoch_time)
    # Read epoch date from input
    #epoch_time = getSec(sys.stdin.read())

    # Get 'current' time
    if DEBUG:
        #print "Current time: {}".format(TEST_TIME)
        current_time = getSec(TEST_TIME)
    else:
        current_time = time.time()
            
    # Calculate elapsed time and create string to the current minute in seconds
    elapsed = current_time - epoch_time
    elapsed_str = '{}'.format(int(elapsed - elapsed % VALID_TIME))

    # Create double hash of time found
    hash_str = hashlib.md5(hashlib.md5(elapsed_str).hexdigest()).hexdigest() 
    
    # Display elapsed time and  hash if debugging
    #if DEBUG:
        #print elapsed_str
        #print hash_str

    # Initialize Variables
    num_code = ""	 # Store the numeric characters of the code
    letter_code = "" # Store the alpha characters of the code

    # Search for the first two alpha characters of the hash and save them
    for i in range(0,len(hash_str)):
        last_pos = i		                # Save position
        if (hash_str[i].isalpha()):		# Check if alpha
            letter_code += hash_str[i]
        if (len(letter_code) == 2):		# Check how many characters have been found
            break
    
    # Reset counter
    i = 0

    # Search for numeric characters needed to fill code
    for i in range(len(hash_str)-1,0,i-1):
        if (not hash_str[i].isalpha()):		    # If not alpha, then numeric
            num_code += hash_str[i]   	            # Append current hash character 
        if (len(num_code) + len(letter_code) == 4): # Check if the code can be filled
            break

    # If the code can not be filled, resume alpha search and append to end of num_code until code can be filled
    if (len(num_code) + len(letter_code) != 4):

        # Reset counter
        i = 0
        for i in range(last_pos+1, len(hash_str)):
            if (hash_str[i].isalpha()):		   # Check if alpha
                num_code += hash_str[i]
            if (len(num_code) +len(letter_code) == 4): # Check if code can be filled
                break

    # Create code and display
    code = letter_code+num_code
    return code;

TLPass = timeLock(EPOCH_TIME)
PASSWORD = "" + TLPass

# Connect to the FTP server
#ftp = FTP(HOSTNAME)
#ftp.port = PORT
#ftp.login(user=USERNAME, passwd=PASSWORD)
